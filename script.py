# -*- coding: utf-8 -*-
"""Иерархическая кластеризация

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1T4LRU9lp4xdWvBhmC5KMrSmzDJMnfB3W
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.datasets import make_blobs
from scipy.cluster.hierarchy import dendrogram, linkage
from sklearn.cluster import AgglomerativeClustering

sns.set()
sns.set_style('ticks')

"""**СОЗДАНИЕ ДАТАСЕТА**"""

# Главный корпус
rows = pd.DataFrame({
  'name' : 'Главный корпус',
  'countFloors' : [2],                # Количество этажей
  'countDoors' : [2]                  # Количество дверей
})
df = pd.DataFrame(rows)

# Биокорпус
rows = pd.DataFrame({
  'name' : 'Биокорпус',
  'countFloors' : [4],
  'countDoors' : [4]
})
df = df.append(rows)

# Лабораторный корпус
rows = pd.DataFrame({
  'name' : 'Лабораторный корпус',
  'countFloors' : [7],
  'countDoors' : [8]
})
df = df.append(rows)

# Анатомический корпус
rows = pd.DataFrame({
  'name' : 'Анотомический корпус',
  'countFloors' : [2],
  'countDoors' : [2]
})
df = df.append(rows)

# Хозяйственный корпус
rows = pd.DataFrame({
  'name' : 'Хозяйственный корпус',
  'countFloors' : [5],
  'countDoors' : [3]
})
df = df.append(rows)

# Корпус деканатов
rows = pd.DataFrame({
  'name' : 'Корпус деканатов',
  'countFloors' : [2],
  'countDoors' : [1]
})
df = df.append(rows)

# Латинский корпус
rows = pd.DataFrame({
  'name' : 'Латинский корпус',
  'countFloors' : [2],
  'countDoors' : [2]
})
df = df.append(rows)

df.head(7)

"""**ПОСТРОЕНИЕ ДЕНДОГРАММЫ**"""

plt.figure(figsize=(18, 8))
plt.scatter(df.countFloors, df.countDoors)
plt.show(7)

"""**ПЕРВЫЙ МЕТОД ПОСТРОЕНИЯ ДЕНДОГРАММЫ**"""

X, y, centers = make_blobs(n_samples=7, centers=2, n_features=2, center_box=[1,7], return_centers=True, random_state=0)
X = pd.DataFrame(df, columns=['countFloors', 'countDoors'])

cluster_ar = linkage(X, method='ward', metric='euclidean')

link_df = pd.DataFrame(cluster_ar, index=[f'step {i+1}' for i in range(cluster_ar.shape[0])], 
                       columns=['cluster1', 'cluster2', 'dist', 'number elements'])
link_df.head(7)

fig = plt.figure(figsize=(18, 8))
row_dendr = dendrogram(link_df)

"""**ВТОРОЙ МЕТОД ПОСТРОЕНИЯ ДЕНДОГРАММЫ**"""

data = list(zip(df.countFloors, df.countDoors))

for i in range(7,0,-1):
    hierarchical_cluster = AgglomerativeClustering(n_clusters=i, linkage='complete')
    labels = hierarchical_cluster.fit_predict(data)

    
    plt.figure(figsize=(18, 8))
    plt.scatter(df.countFloors, df.countDoors, c=labels)
    print(plt.show())

plt.figure(figsize=(18, 8))
linkage_data = linkage(data, method='complete')
dendrogram(linkage_data)
plt.show()