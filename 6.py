import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.neighbors import KNeighborsClassifier

df = pd.read_csv("glass.csv")
x = df.drop("Type",axis=1)
y = df["Type"]

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.3)

model = KNeighborsClassifier(n_neighbors=3,metric="euclidean")
model.fit(x_train,y_train)
pre = model.predict(x_test)

ac = accuracy_score(pre,y_test)
print(ac)