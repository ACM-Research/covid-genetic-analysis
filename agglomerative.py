# -*- coding: utf-8 -*-
"""
Created on Sun Apr 11 21:37:39 2021

@author: mansu
"""

from sklearn.cluster import AgglomerativeClustering
import numpy as np
import matplotlib.pyplot as plt
import Levenshtein as lev
from Bio import SeqIO
from sklearn.preprocessing import normalize
import os
      
def agglomerative():
        
    os.chdir("Sequences by Month")
    
    sampleArray = []
    f1 = open("refSeq.txt","r")
    ref_seq = f1.read()
    
    f2 = open("varSeq.txt","r")
    var_seq = f2.read()
    ratios_r = []
    ratios_v = []
    sampleString = ""
    combinedArr = []
    
    for record in SeqIO.parse("all200Sequences.fasta", "fasta"):
      sampleString = str(record.seq)
      sampleArray.append(sampleString)
    
    
    for i in sampleArray:
      Ratio = lev.ratio(ref_seq, i)
      ratios_r.append(Ratio)
      Ratio = lev.ratio(var_seq, i)
      ratios_v.append(Ratio)
    
    ratios_r_normal = np.random.normal(ratios_r)
    #print(ratios_r_normal)
    
    # for clustering around 0 (subtract the mean from each value)
    avg = sum(ratios_r_normal) / len(ratios_r_normal)
    ratios_r_normal = [i - avg for i in ratios_r_normal]
    
    
    ratios_v_normal = np.random.normal(ratios_v)
    #print(ratios_v_normal)
    
    avg = sum(ratios_v_normal) / len(ratios_v_normal)
    ratios_v_normal = [i - avg for i in ratios_v_normal]
    sequenceArrays = []
    sampleString1 = ""
    
    for record in SeqIO.parse("all200Sequences.fasta", "fasta"):  
      sampleString1 = str(record.description)
      sequenceArrays.append(sampleString1)
    combinedArr = np.stack((ratios_r_normal, ratios_v_normal), axis= -1)
    
    combinedArr_normalized = normalize(combinedArr)
    
    ac4_1 = AgglomerativeClustering(n_clusters=4, affinity='l1', linkage='average')
    ac4_2 = AgglomerativeClustering(n_clusters=4, linkage='average')
    
    plt.figure(figsize =(6, 6)) 
    plt.scatter(ratios_r_normal, ratios_v_normal, c = ac4_1.fit_predict(combinedArr_normalized), cmap ='rainbow') 
    plt.grid(True, linewidth = .5)
    plt.xlabel('Normalized Reference Sequence')
    plt.ylabel('Normalized Uk B.1.1.7 Sequence')
    plt.title('Ref Sequence vs Uk B.1.1.7')
    
    
    plt.figure(figsize =(6, 6)) 
    plt.scatter(ratios_r_normal, ratios_v_normal, c = ac4_2.fit_predict(combinedArr_normalized), cmap ='rainbow') 
    plt.grid(True, linewidth = .5)
    plt.xlabel('Normalized Reference Sequence')
    plt.ylabel('Normalized Uk B.1.1.7 Sequence')
    plt.title('Ref Sequence vs Uk B.1.1.7')
    
    plt.show() 
    
    return ac4_1, ac4_2