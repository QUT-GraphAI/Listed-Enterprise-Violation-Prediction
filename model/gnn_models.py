import torch
import torch.nn as nn
import torch.nn.functional as F
from torch_geometric.nn import RGATConv

"""
Dimension-level Risk Perception Module (DRPM)
    """
class DRPM(nn.Module):
    def __init__(self, in_channels, num_relations):
        super(DRPM, self).__init__()
        self.W_g = nn.Linear(in_channels, in_channels)
        self.W_r = nn.ModuleList([nn.Linear(in_channels, in_channels) for _ in range(num_relations)])
        self.W_d = nn.Linear(in_channels, in_channels)

    def forward(self, x_target, x_neighbors, edge_types):
        g_i = torch.sigmoid(self.W_g(x_target))

        c_j = torch.empty_like(x_neighbors)
        for i, rel in enumerate(edge_types):
            c_j[i] = self.W_r[rel](x_neighbors[i])

        a_ij = F.softmax(g_i * c_j, dim=0)

        h_k = torch.sum(a_ij * x_neighbors, dim=0, keepdim=True)
        return self.W_d(h_k)

"""
    Long-hop Risk Perception Module (LRPM) with Linear Self-Attention
    """
class LRPM(nn.Module):
    def __init__(self, in_channels, num_heads=4):
        super(LRPM, self).__init__()
        self.W_q = nn.Linear(in_channels, in_channels)
        self.W_k = nn.Linear(in_channels, in_channels)
        self.W_v = nn.Linear(in_channels, in_channels)
        self.W_o = nn.Linear(in_channels, in_channels)
        self.beta = nn.Parameter(torch.tensor(0.5))

    def forward(self, x_target, x_all):
        Q = F.normalize(self.W_q(x_target), p=2, dim=-1)
        K = F.normalize(self.W_k(x_all), p=2, dim=-1)
        V = self.W_v(x_all)

        N = x_all.size(0)
        K_sum = K.sum(dim=0, keepdim=True)
        KV = torch.matmul(K.transpose(-2, -1), V)

        D = 1 + (1 / N) * torch.matmul(Q, K_sum.transpose(-2, -1))
        Z = self.beta * (1 / D) * (V.mean(dim=0, keepdim=True) + (1 / N) * torch.matmul(Q, KV)) + (
                    1 - self.beta) * x_target

        return self.W_o(Z)

"""
    Relational Graph Dimension and Linear Attention Network (RGDLAN)
    """
class RGDLAN(nn.Module):
    def __init__(self, in_channels, num_relations, num_heads=4):
        super(RGDLAN, self).__init__()
        self.rgat = RGATConv(in_channels, in_channels, num_relations=num_relations)
        self.drpm = DRPM(in_channels, num_relations)
        self.lrpm = LRPM(in_channels, num_heads)
        self.W_direct = nn.Linear(in_channels, in_channels)

    def forward(self, x, edge_index, edge_type, target_idx=0):
        mask = (edge_index[0] == target_idx)
        neighbors_idx = edge_index[1][mask]
        n_edge_types = edge_type[mask]

        d_rgat = self.rgat(x, edge_index, edge_type)[target_idx].unsqueeze(0)
        h_drpm = self.drpm(x[target_idx].unsqueeze(0), x[neighbors_idx], n_edge_types)
        p_lrpm = self.lrpm(x[target_idx].unsqueeze(0), x)

        return self.W_direct(d_rgat + h_drpm + p_lrpm)

"""
    Hypergraph Multi-Attention Refined Network (HMARN)
    """
class HMARN(nn.Module):
    def __init__(self, in_channels, num_hyperedge_types):
        super(HMARN, self).__init__()
        self.beta = nn.Parameter(torch.tensor(0.5))
        self.W_1 = nn.Linear(in_channels, in_channels)
        self.W_2 = nn.Linear(in_channels, 1)
        self.W_3 = nn.Linear(in_channels, in_channels)
        self.gamma = nn.Parameter(torch.ones(num_hyperedge_types))

    def forward(self, x, hyperedges, he_types):
        m_k_list, X_k_list = [], []

        for he in hyperedges:
            nodes = x[he]
            target = nodes[0].unsqueeze(0)

            concat_feat = torch.cat([target.expand(len(he), -1), nodes], dim=-1)
            a_ij = F.softmax(F.leaky_relu(self.beta * concat_feat.sum(dim=-1)), dim=0).unsqueeze(1)

            m_k_list.append(F.relu(torch.sum(a_ij * nodes, dim=0, keepdim=True)))
            X_k_list.append(nodes.mean(dim=0, keepdim=True))

        X_k_tensor = torch.cat(X_k_list, dim=0)
        a_k = F.softmax(self.W_2(torch.tanh(self.W_1(X_k_tensor))), dim=0)

        z_common = torch.zeros(1, x.size(-1), device=x.device)
        for idx, (m_i_k, he_type) in enumerate(zip(m_k_list, he_types)):
            z_common += m_i_k * a_k[idx] * self.gamma[he_type]

        return self.W_3(z_common)