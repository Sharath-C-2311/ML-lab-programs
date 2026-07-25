from sklearn.datasets import load_iris
import numpy as np
from scipy.cluster.hierarchy import dendrogram,linkage
import matplotlib.pyplot as plt

data = load_iris()
data = data.data[:6]

def proximity(data):
    n = data.shape[0]
    prox_matrix = np.zeros((n,n))

    for i in range(n):
        for j in range(i+1,n):
            prox_matrix[i,j] = np.linalg.norm(data[i]-data[j])
            prox_matrix[j,i] = prox_matrix[i,j]
    return prox_matrix

def ploting(data,method):
    lin = linkage(data,method=method)
    dendrogram(lin)
    plt.show()

pr = proximity(data)
print(pr)
ploting(data,"single")