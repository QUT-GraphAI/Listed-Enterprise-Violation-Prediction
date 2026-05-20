# RGDLAN and HMARN: A Dual-Path Graph Neural Approach with Multi-Agent Systems for Listed Enterprise Violation Prediction

This repository contains the official **key code modules** and **partial desensitized data** for the paper **"RGDLAN and HMARN: A Dual-Path Graph Neural Approach with Multi-Agent Systems for Listed Enterprise Violation Prediction"**, submitted to *Information Sciences*.

> **🚧 Work in Progress:** This repository is actively maintained. We will continue to refine the code, improve documentation, and update additional supplementary scripts in the future.

## 📖 Introduction
This work proposes a novel dual-path graph neural approach combined with a Large Language Model (LLM) based Multi-Agent system for predicting violations of listed enterprises. 
- **HMARN (Hypergraph Multi-Attention Refined Network):** Models common risks among enterprises.
- **RGDLAN (Relational Graph Dimension and Linear Attention Network):** Models direct contagion risks.
- **LLM-MA & Calibration:** A multi-agent system that provides expert reviews and calibrates the GNN-EVP model for enhanced performance.

## 📁 Repository Structure

### 💻 Key Code Modules
We have open-sourced the essential code modules of our proposed framework to facilitate understanding and reproducibility:
* `gnn_models.py`: Contains the core PyTorch implementations of the Graph Neural Networks, including the Dimension-level Risk Perception Module (DRPM), Long-hop Risk Perception Module (LRPM), and the HMARN architecture.
* `llm_prompt.py`: Contains the carefully designed prompt templates and agent roles (finance, ceo, news, laws, vios) for the multi-agent system.
* `calibration_model.py`: The implementation of the LLM-based calibration method (`model_calibration` class) used to align and fuse the outputs from the GNN models and the LLM Multi-Agent system.

### 📊 Data
**⚠️ Data Availability Notice:** The original complete dataset is sourced from the **CSMAR (China Stock Market & Accounting Research)** database. Due to strict copyright restrictions and data privacy policies, we cannot distribute the raw database. Instead, we have released a **partial, desensitized subset** of the data. This subset is fully compatible with the provided code and sufficient for demonstrating the model's functionality.

* `enterprise_data.csv`: A desensitized subset of the enterprise dataset containing key features (e.g., Total Assets, Cash Ratio, Operating Profit Margin), violation labels, and node indices (`graph_id`).
* `graph_triple.nt`: The topological structure data represented as relational triples (subject, predicate, object) used to construct the relational graphs.

## 🛠️ Dependencies
To run the code, please ensure your environment matches the following dependencies. You can install them via pip:

```bash
# Python Environment Requirements
pip install numpy==1.22.3
pip install pandas==1.2.5
pip install scikit-learn==1.2.2
pip install matplotlib==3.7.1
pip install networkx==2.8.8
pip install py2neo==2021.2.3
pip install pypinyin==0.49.0
pip install tqdm==4.65.0

# PyTorch & PyTorch Geometric (Ensure compatibility with your CUDA version)
pip install torch==1.10.0
pip install torch-geometric==2.2.0
pip install torch-sparse==0.6.13
