import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression, LogisticRegression
import random
import pickle
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from sklearn.manifold import TSNE
from sklearn.metrics import accuracy_score as acc, confusion_matrix
from sklearn.metrics import recall_score as rec
from sklearn.metrics import precision_score as pre
from sklearn.metrics import f1_score as f1
from sklearn.metrics import roc_auc_score as roc
from scipy.stats import gmean


class model_calibration:
    def __init__(self, m):
        self.m = m
        self.delta = np.zeros((m, 2))

    def fit(self, y_ml, y_llm, y_true):
        for i in range(self.m):
            for l in range(2):
                mask = (np.floor(y_ml * self.m) == i) & (y_llm == l)
                if np.sum(mask) > 0:
                    tmp = np.mean(y_true[mask] - y_ml[mask])
                    self.delta[i, l] = tmp

    def predict(self, y_ml, y_llm):
        y_pred = np.zeros_like(y_ml)
        for i in range(self.m):
            for l in range(2):
                mask = (np.floor(y_ml * self.m) == i) & (y_llm == l)
                y_pred[mask] = y_ml[mask] + self.delta[i, l]

        return y_pred

def train_acc(model, model_name_string, y_train_ml, y_train_llm, y_train_true):
    model.fit(y_train_ml, y_train_llm, y_train_true)

    y_train_pred_score = model.predict(y_train_ml, y_train_llm)

    y_train_pred_label = (y_train_pred_score>0.5).astype(int)
    acc_train = np.mean(y_train_pred_label==y_train_true)
    print('method: '+model_name_string+' \n train acc = ',acc_train)
    return y_train_pred_label



def valid_acc(model, model_name_string,
              y_valid_ml, y_valid_llm, y_valid_true):
    model.fit(y_valid_ml, y_valid_llm, y_valid_true)

    y_valid_pred_score = model.predict(y_valid_ml, y_valid_llm)
    y_valid_pred_label = (y_valid_pred_score > 0.5).astype(int)

    ac = acc(y_valid_true, y_valid_pred_label)
    pr = pre(y_valid_true, y_valid_pred_label)
    re = rec(y_valid_true, y_valid_pred_label)
    f = f1(y_valid_true, y_valid_pred_label)
    rc = roc(y_valid_true, y_valid_pred_score)
    tn, fp, fn, tp = confusion_matrix(y_valid_true, y_valid_pred_label).ravel()
    specificity = tn / (tn + fp)
    g_mean = np.sqrt(re * specificity)

    print(
        f"method: {model_name_string}  acc={ac:.4f}  pre={pr:.4f}  recall={re:.4f}  f1={f:.4f}  auc={rc:.4f}  g_mean={g_mean:.4f}")


    return ac,pr,re,f,rc,g_mean



def test_acc(model, model_name_string,
              y_test_ml, y_test_llm, y_test_true):
    model.fit(y_test_ml, y_test_llm, y_test_true)

    y_test_pred_score = model.predict(y_test_ml, y_test_llm)
    y_test_pred_label = (y_test_pred_score > 0.5).astype(int)
    ac = acc(y_test_true, y_test_pred_label)
    pr = pre(y_test_true, y_test_pred_label)
    re = rec(y_test_true, y_test_pred_label)
    f = f1(y_test_true, y_test_pred_label)
    rc = roc(y_test_true, y_test_pred_score)
    tn, fp, fn, tp = confusion_matrix(y_test_true, y_test_pred_label).ravel()
    specificity = tn / (tn + fp)
    g_mean = np.sqrt(re * specificity)

    print(
        f"method: {model_name_string}  acc={ac:.4f}  pre={pr:.4f}  recall={re:.4f}  f1={f:.4f}  auc={rc:.4f}  g_mean={g_mean:.4f}")

    return ac,pr,re,f,rc,g_mean