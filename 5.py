import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import confusion_matrix,accuracy_score

df = pd.read_csv("titanic.csv")
df = df[['Survived', 'Pclass', 'Age', 'SibSp', 'Parch', 'Fare', 'Embarked']]

imputer = SimpleImputer(strategy="median")
df[["Age","Fare"]] = imputer.fit_transform(df[["Age","Fare"]])

df["Embarked"].fillna(df["Embarked"].mode()[0],inplace=True)
df["Embarked"] = LabelEncoder().fit_transform(df["Embarked"])

x = df.drop("Survived",axis=1)
y = df["Survived"]

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=42)

model = GaussianNB()
model.fit(x_train,y_train)

y_pred = model.predict(x_test)

cm = confusion_matrix(y_pred,y_test)
ac = accuracy_score(y_pred,y_test)

print(cm,"\nscore = ",ac)




































import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix,accuracy_score
from sklearn.naive_bayes import GaussianNB


df = pd.read_csv("titanic.csv")
df = df[['Survived', 'Pclass', 'Age', 'SibSp', 'Parch', 'Fare', 'Embarked']]

imputer = SimpleImputer(strategy="median")
df[["Age","Fare"]] = imputer.fit_transform(df[["Age","Fare"]])

df["Embarked"].fillna(df["Embarked"].mode()[0],inplace=True)
df["Embarked"] = LabelEncoder().fit_transform(df["Embarked"])


x = df.drop("Survived",axis=1)
y = df["Survived"]

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,randon_state=42)

model = GaussianNB()
model.fit(x_train,y_train)

y_pred = model.predict(x_test)

acc = accuracy_score(y_pred,y_test)
cm = confusion_matrix(y_pred,y_test)

print(acc,"\n",cm)

