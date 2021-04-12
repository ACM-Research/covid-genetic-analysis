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

print(da.accuracy(ac4_2.labels_,ac4_1.labels_)) # must use converted labels
print("Purity score: ", da.purity(ac4_2.labels_, ac4_1.labels_))

fig.update_layout(title_text = "Data Table of Sample Similarity Ratios + Clustering Labels")
fig.show()