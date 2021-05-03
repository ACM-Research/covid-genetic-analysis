# -*- coding: utf-8 -*-
"""
Created on Sun Apr 11 21:50:24 2021

@author: mansu
"""

def conversion (numClusters, labels):
  lst = [None for x in range(len(labels))]
  
  if (numClusters == 4):
    cluster0 = 0
    cluster1 = 0
    cluster2 = 0
    cluster3 = 0
    for x in labels:
      if (x == 0):
        cluster0 = cluster0 + 1
      if (x == 1):
        cluster1 = cluster1 + 1
      if (x == 2):
        cluster2 = cluster2 + 1
      if (x == 3):
        cluster3 = cluster3 + 1
    
    #Dictionary1 = {'cluster0': cluster0, 'cluster1': cluster1, 'cluster2': cluster2, 'cluster3': cluster3}
    #print (Dictionary1)

    i = 0
    while (i <= 3):
      m = max(cluster0, cluster1, cluster2, cluster3)
      if (m == cluster0):
        for x, item in enumerate(labels):
          if (item == 0):
            lst[x] = i
        cluster0 = 0
      if (m == cluster1):
        for x, item in enumerate(labels):
          if (item == 1):
            lst[x] = i
        cluster1 = 0
      if (m == cluster2):
        for x, item in enumerate(labels):
          if (item == 2):
            lst[x] = i
        cluster2 = 0
      if (m == cluster3):
        for x, item in enumerate(labels):
          if (item == 3):
            lst[x] = i
        cluster3 = 0
      i = i + 1
 

  if (numClusters == 3):
    cluster0 = 0
    cluster1 = 0
    cluster2 = 0
    for x in labels:
      if (x == 0):
        cluster0 = cluster0 + 1
      if (x == 1):
        cluster1 = cluster1 + 1
      if (x == 2):
        cluster2 = cluster2 + 1
    
    #Dictionary1 = {'cluster0': cluster0, 'cluster1': cluster1, 'cluster2': cluster2}
    #print (Dictionary1)

    lst = [None for x in range(len(labels))]
    i = 0
    while (i <= 3):
      m = max(cluster0, cluster1, cluster2)
      if (m == cluster0):
        for x, item in enumerate(labels):
          if (item == 0):
            lst[x] = i
        cluster0 = 0
      if (m == cluster1):
        for x, item in enumerate(labels):
          if (item == 1):
            lst[x] = i
        cluster1 = 0
      if (m == cluster2):
        for x, item in enumerate(labels):
          if (item == 2):
            lst[x] = i
        cluster2 = 0
      i = i + 1
    

  if (numClusters == 2):
    cluster0 = 0
    cluster1 = 0
    cluster2 = 0
    for x in labels:
      if (x == 0):
        cluster0 = cluster0 + 1
      if (x == 1):
        cluster1 = cluster1 + 1
    
    #Dictionary1 = {'cluster0': cluster0, 'cluster1': cluster1}

    lst = [None for x in range(len(labels))]
    i = 0
    while (i <= 3):
      m = max(cluster0, cluster1, cluster2)
      if (m == cluster0):
        for x, item in enumerate(labels):
          if (item == 0):
            lst[x] = i
        cluster0 = 0
      if (m == cluster1):
        for x, item in enumerate(labels):
          if (item == 1):
            lst[x] = i
        cluster1 = 0
    

  return lst