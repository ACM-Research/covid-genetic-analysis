# -*- coding: utf-8 -*-
"""
Created on Sun Apr 11 21:54:29 2021

@author: mansu
"""

import agglomerative as ag
import kMeans as k
import conversion as con
import dataAnalysis as da
import os

import numpy as np
from Bio import SeqIO
import plotly.graph_objects as go

from sklearn.metrics import accuracy_score
from sklearn import metrics
import numpy as np

import pandas as pd

#os.chdir("Sequences by Month")

sequencesArray = []
sampleString1 = ""

for record in SeqIO.parse("all200Sequences.fasta", "fasta"):  
  sampleString1 = str(record.description)
  sequencesArray.append(sampleString1)

"""fig = go.Figure(data=[go.Table(header=dict(values=['Sequence ID', 'Clustering Label (n=4)', 
                                                   'Clustering Label (n=4) V2'], fill_color = 'lightgreen'),
                 cells=dict(values=[sequencesArray, ac4_1.labels_, ac4_2.labels_]))
                     ])
print(ac4_1.labels_)
newLabels = np.asarray(con.conversion(4, ac4_1.labels_))"""

col_list = ["Cluster ID", "Sequence ID"]
mega = pd.read_csv("MEGA_Cluster_ID's_Updated.csv", usecols=col_list)
megaCluster = mega["Cluster ID"]
megaNames = mega["Sequence ID"]

for i in range(len(sequencesArray)):
    sequencesArray[i] = sequencesArray[i].replace('[', '')
    sequencesArray[i] = sequencesArray[i].replace(']', " ")
    sequencesArray[i] = sequencesArray[i].replace(',', '')

mapped = {}
for i in range(len(megaCluster)):
    mapped[megaNames[i]] = megaCluster[i]
    
orderedMega = []
for i in sequencesArray:
    orderedMega.append(mapped[i])

# print purity scores for 2-4 clusters (agglomerative)
for j in range (2,5):
    ac_1, ac_2 = ag.agglomerative(j)
    #newLabels1 = np.asarray(con.conversion(j, ac_1.labels_))
    #print(da.accuracy(orderedMega, newLabels1)) # must use converted labels
    print("Purity score: ", da.purity(orderedMega, ac_1.labels_))
    
    #newLabels2 = np.asarray(con.conversion(j, ac_2.labels_))
    #print(da.accuracy(orderedMega, newLabels2)) # must use converted labels
    print("Purity score: ", da.purity(orderedMega, ac_2.labels_))

"""for i in range(2,5):
    kLabels = k.meansK(i)
    #newLabels = np.asarray(con.conversion(j, kLabels))
    #print(da.accuracy(orderedMega, newLabels)) # must use converted labels
    print("Purity score: ", da.purity(orderedMega, kLabels))"""
    

#fig.update_layout(title_text = "Data Table of Sample Similarity Ratios + Clustering Labels")
#fig.show()
