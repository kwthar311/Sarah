import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
import pickle
from  sklearn import svm
from sklearn.model_selection import train_test_split
#import matplotlib.pyplot as plt
df = pd.read_csv('a6.csv')


X = df.iloc[:, :-1].values
y = df.iloc[:, 9].values

X_TV, X_test, y_TV, y_test = train_test_split(X,y, test_size=0.25,random_state=42)

error = []

knn = KNeighborsClassifier(n_neighbors=17)
print(X_TV[0])
knn.fit(X_TV, y_TV)
pred_i = knn.predict(X_test)
error.append(np.mean(pred_i != y_test))
filename_one = 'knn_model.sav'
pickle.dump(knn, open(filename_one, 'wb'))
accuracy=np.mean(pred_i == y_test)*100
print ("The achieved accuracy using knn is " + str(accuracy))
