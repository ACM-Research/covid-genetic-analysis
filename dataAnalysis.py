# -*- coding: utf-8 -*-
"""
Created on Sun Apr 11 21:51:39 2021

@author: mansu
"""
from sklearn.metrics import accuracy_score
from sklearn import metrics
import numpy as np

def accuracy (true_labels, pred_labels):
  print(accuracy_score(true_labels, pred_labels, normalize=True))
  return accuracy_score(true_labels, pred_labels, normalize=False)

def purity (true_labels, pred_labels):
  contingency_matrix = metrics.cluster.contingency_matrix(true_labels, pred_labels)
  return np.sum(np.amax(contingency_matrix, axis=0)) / np.sum(contingency_matrix)

# add a "main" function to call the other two