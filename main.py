# -*- coding: utf-8 -*-
"""
Created on Sun Apr 11 21:54:29 2021

@author: mansu
"""

import agglomerative as ag
import kMeans
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

for record in SeqIO.parse("Sequences by Month/all200Sequences.fasta", "fasta"):  
  sampleString1 = str(record.description)
  sequencesArray.append(sampleString1)

ac4_1, ac4_2 = ag.agglomerative()

fig = go.Figure(data=[go.Table(header=dict(values=['Sequence ID', 'Clustering Label (n=4)', 
                                                   'Clustering Label (n=4) V2'], fill_color = 'lightgreen'),
                 cells=dict(values=[sequencesArray, ac4_1.labels_, ac4_2.labels_]))
                     ])
print(ac4_1.labels_)
newLabels = np.asarray(con.conversion(4, ac4_1.labels_))

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


print(da.accuracy(orderedMega,ac4_1.labels_)) # must use converted labels
print("Purity score: ", da.purity(orderedMega, ac4_1.labels_))

fig.update_layout(title_text = "Data Table of Sample Similarity Ratios + Clustering Labels")
fig.show()
