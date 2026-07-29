# PCA
import numpy as np
from sklearn.datasets import load_iris
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

x = load_iris().data
y = load_iris().target

model = PCA(2)
x_t = model.fit_transform(x,y)

print("1:",x.shape)
print("2:",x_t.shape)

p1 = x_t[:,0]
p2 = x_t[:,1]
plt.scatter(p1,p2,c=y,cmap="jet")
plt.show()


# LDA
import numpy as np
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as LDA
from sklearn.datasets import load_iris
import matplotlib.pyplot as plt

x = load_iris().data
y = load_iris().target

model = LDA(n_components=2)
x_t = model.fit_transform(x,y)
print("1: ",x.shape)
print("2: ",x_t.shape)

l1 = x_t[:,0]
l2 = x_t[:,1]

plt.scatter(l1,l2,c=y,cmap="jet")
plt.show()