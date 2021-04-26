# -*- coding: utf-8 -*-
"""
Created on Sun Apr 11 21:54:29 2021

@author: mansu
"""

import agglomerative as ag
import kMeans as k
import conversion as con
import dataAnalysis as da
import numpy as np
from Bio import SeqIO
import plotly.graph_objects as go
import pandas as pd

#os.chdir("Sequences by Month")

sequencesArray = []
sampleString1 = ""

for record in SeqIO.parse("Sequences by Month/all200Sequences.fasta", "fasta"):  
  sampleString1 = str(record.description)
  sequencesArray.append(sampleString1)

masterArray = []
sampleString1 = ""
for record in SeqIO.parse("Sequences by Month/sequencesMaster.fasta", "fasta"):  
  sampleString1 = str(record.description)
  masterArray.append(sampleString1)


for i in range(len(sequencesArray)):
    sequencesArray[i] = sequencesArray[i].replace('[', '')
    sequencesArray[i] = sequencesArray[i].replace(']', " ")
    sequencesArray[i] = sequencesArray[i].replace(',', '')

for i in range(len(masterArray)):
    masterArray[i] = masterArray[i].replace('[', '')
    masterArray[i] = masterArray[i].replace(']', " ")
    masterArray[i] = masterArray[i].replace(',', '')
    
col_list = ["Cluster ID", "Sequence ID"]
aggMega4 = pd.read_csv("MEGA Generated Data/mega_all228_n=4.csv", usecols=col_list)
aggMega3 = pd.read_csv("MEGA Generated Data/mega_all228_n=3.csv", usecols=col_list)
aggMega2 = pd.read_csv("MEGA Generated Data/mega_all228_n=2.csv", usecols=col_list)

aggMega4Cluster = aggMega4["Cluster ID"]
aggMega4Names = aggMega4["Sequence ID"]

aggMega3Cluster = aggMega3["Cluster ID"]
aggMega3Names = aggMega3["Sequence ID"]

aggMega2Cluster = aggMega2["Cluster ID"]
aggMega2Names = aggMega2["Sequence ID"]

aggMapped4 = {}
aggMapped3 = {}
aggMapped2 = {}
for i in range(len(aggMega4Cluster)):
    aggMapped4[aggMega4Names[i]] = aggMega4Cluster[i]
    aggMapped3[aggMega3Names[i]] = aggMega3Cluster[i]
    aggMapped2[aggMega2Names[i]] = aggMega2Cluster[i]
    
orderedMega4 = []
orderedMega3 = []
orderedMega2 = []
for i in sequencesArray:
    orderedMega4.append(aggMapped4[i])
    orderedMega3.append(aggMapped3[i])
    orderedMega2.append(aggMapped2[i])


# print purity scores for 2-4 clusters (agglomerative)
for j in range (2,5):
    ac_1, ac_2 = ag.agglomerative(j)
    newLabels1 = np.asarray(con.conversion(j, ac_1.labels_))
    newLabels2 = np.asarray(con.conversion(j, ac_2.labels_))
    if (j == 2):
        print("For agglomerative L1 affinity,", j, "clusters")
        print("Accuracy score:", da.accuracy(orderedMega4, newLabels1)) # must use converted labels
        print("Purity score:", da.purity(orderedMega4, ac_1.labels_))
        print("\nFor agglomerative euclidian affinity,", j, "clusters")
        print("Accuracy score:", da.accuracy(orderedMega4, newLabels2)) # must use converted labels
        print("Purity score:", da.purity(orderedMega4, ac_2.labels_), "\n")
    
    if (j == 3):
        print("For agglomerative L1 affinity,", j, "clusters")
        print("Accuracy score:", da.accuracy(orderedMega3, newLabels1)) # must use converted labels
        print("Purity score:", da.purity(orderedMega3, ac_1.labels_))
        print("\nFor agglomerative euclidian affinity,", j, "clusters")
        print("Accuracy score:", da.accuracy(orderedMega3, newLabels2)) # must use converted labels
        print("Purity score:", da.purity(orderedMega3, ac_2.labels_), "\n")
    
    if (j == 4):
        print("For agglomerative L1 affinity,", j, "clusters")
        print("Accuracy score:", da.accuracy(orderedMega4, newLabels1)) # must use converted labels
        print("Purity score:", da.purity(orderedMega4, ac_1.labels_))
        print("\nFor agglomerative euclidian affinity,", j, "clusters")
        print("Accuracy score:", da.accuracy(orderedMega4, newLabels2)) # must use converted labels
        print("Purity score:", da.purity(orderedMega4, ac_2.labels_), "\n")
    
kMega4 = pd.read_csv("MEGA Generated Data/mega_no_partial_4.csv", usecols=col_list)
kMega3 = pd.read_csv("MEGA Generated Data/mega_no_partial_3.csv", usecols=col_list)
kMega2 = pd.read_csv("MEGA Generated Data/mega_no_partial_2.csv", usecols=col_list)

kMega4Cluster = kMega4["Cluster ID"]
kMega4Names = kMega4["Sequence ID"]

kMega3Cluster = kMega3["Cluster ID"]
kMega3Names = kMega3["Sequence ID"]

kMega2Cluster = kMega2["Cluster ID"]
kMega2Names = kMega2["Sequence ID"]

kMapped4 = {}
kMapped3 = {}
kMapped2 = {}
for i in range(len(kMega4Cluster)):
    kMapped4[kMega4Names[i]] = kMega4Cluster[i]
    kMapped3[kMega3Names[i]] = kMega3Cluster[i]
    kMapped2[kMega2Names[i]] = kMega2Cluster[i]
    
KorderedMega4 = []
KorderedMega3 = []
KorderedMega2 = []
for i in masterArray:
    KorderedMega4.append(kMapped4[i])
    KorderedMega3.append(kMapped3[i])
    KorderedMega2.append(kMapped2[i])
# print purity scores for 2-4 clusters (kmeans)
for j in range(2,5):
    kLabels = k.meansK(j)
    newLabels = np.asarray(con.conversion(j, kLabels))
    print("For kMeans,", j, "clusters")
    if (j == 2):
        print("Accuracy score:", da.accuracy(KorderedMega2, newLabels)) # must use converted labels
        print("Purity score: ", da.purity(KorderedMega2, kLabels), "\n")
    if (j == 3):
        print("Accuracy score:", da.accuracy(KorderedMega3, newLabels)) # must use converted labels
        print("Purity score: ", da.purity(KorderedMega3, kLabels), "\n")
    if (j == 4):
        print("Accuracy score:", da.accuracy(KorderedMega4, newLabels)) # must use converted labels
        print("Purity score: ", da.purity(KorderedMega4, kLabels), "\n")

'''
numClusters = [2, 3, 4]
fig1 = go.Figure(data=[go.Table(header=dict(values=['Number of Clusters', 'Agglomerative L1', 'Agglomerative Euclidian', 
                                                   'kMeans'], fill_color = 'lightgreen'),
                 cells=dict(values=[numClusters, sequencesArray, ac4_1.labels_, ac4_2.labels_]))
                     ])
    
fig1.update_layout(title_text = "Accuracy Scores")
fig1.show()

fig2 = go.Figure(data=[go.Table(header=dict(values=['Number of Clusters', 'Agglomerative L1', 'Agglomerative Euclidian', 
                                                   'kMeans'], fill_color = 'lightgreen'),
                 cells=dict(values=[numClusters, sequencesArray, ac4_1.labels_, ac4_2.labels_]))
                     ])
    
fig2.update_layout(title_text = "Purity Scores")
fig2.show()'''
