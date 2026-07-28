import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

x = load_iris().data
k=3

def k_mens(x,k):
    centroid = x[:k]

    for _ in range(100):

        x_expand = x[:,np.newaxis]
        euclid = np.linalg.norm(x_expand-centroid,axis=2)
        labels = np.argmin(euclid,axis=1)

        new = np.array([x[k==labels].mean(axis=0) for k in range(k)])
        if np.all(centroid == new):
            break

        centroid = new
    return labels,centroid

l,c = k_mens(x,k)
print(l,"\ncentroids : ",c)


plt.scatter(x[:,0],x[:,1],c=l)
plt.scatter(c[:,0],c[:,1],marker="x",color="red",s=200)
plt.show()







def kmeans(x,k):
    centroid = x[:k]

    for _ in range(100):

        other = x[:,np.newaxis]
        euclid = np.linalg.norm(other-centroid,axis=2)
        min_ = np.argmin(euclid,axis=1)

        new = np.array([x[k==min_].mean() for _ in range(k)])

        if np.all(new == centroid):
            break

        centroid = new
    return centroid,min_


l,c = kmeans(x,k)
print(l,"\ncentroids : ",c)