# -*- coding: utf-8 -*-
"""
Created on Sun Apr 11 21:45:18 2021

@author: mansu
"""
import numpy as np
import matplotlib.pyplot as plt
import scipy.cluster.hierarchy as shc 
from Bio import SeqIO
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from scipy.cluster.hierarchy import dendrogram
import os
  

#os.chdir("Sequences by Month")

def meansK(numClusters):
  sequencesArray = []
  sampleString1 = ""

  for record in SeqIO.parse("sequencesMaster.fasta", "fasta"):  
    sampleString1 = str(record.seq)
    sequencesArray.append(sampleString1)  # sequences array is really a list!

  # this turns the list into an array where every letter is replaced with its ascii value; 
  # the array is composed of a bunch of lists(arrays?) of the ascii values
  arr = np.asarray([np.fromstring(s, dtype=np.uint8) for s in sequencesArray])

  #Load Data
  #data = load_digits().data
  pca = PCA(2)
  
  #Transform the data
  df = pca.fit_transform(arr)

  #Initialize the class object
  kmeans = KMeans(n_clusters=numClusters, random_state=0)
  
  #predict the labels of clusters.
  label = kmeans.fit_predict(df)
  print (label)

  #Getting unique labels
  u_labels = np.unique(label)

  #Getting the Centroids
  centroids = kmeans.cluster_centers_

  #plotting the results:
  for i in u_labels:
      plt.scatter(df[label == i , 0] , df[label == i , 1] , label = i)
  #plt.scatter(centroids[:,0] , centroids[:,1] , s = 80, color = 'k')    # shows the centroids
  plt.legend()
  plt.show()
  plt.figure(figsize =(10, 10)) 
  plt.title('Visualising the data') 
  Dendrogram = shc.dendrogram((shc.linkage(df, method ='ward'))) 

  return label