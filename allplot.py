import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

d = np.read_csv('titanic.csv')

x=d["KM"]
y=d["Weight"]
z=d["Price"]

# 3d surface
a = plt.axes(projection="3d")
a.trisurf(x,y,z)
plt.show()