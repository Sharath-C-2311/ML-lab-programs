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


#   or

# import pandas as pd
# import numpy as np
# from sklearn.model_selection import train_test_split
# from sklearn.neighbors import KNeighborsClassifier
# from sklearn.metrics import accuracy_score

# df = pd.read_csv("glass.csv")
# x = df.drop("Type",axis=1)
# y = df["Type"]
# print(df.info())

# x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.3)
# def euc(x,y):
#   return np.sqrt(np.sum((x-y)**2))

# def man(x,y):
#   return np.sum(np.abs(x-y))

# m = KNeighborsClassifier(n_neighbors=3,metric=man)

# m.fit(x_train,y_train)

# y_pred = m.predict(x_test)
# print("Ac :",accuracy_score(y_pred,y_test))