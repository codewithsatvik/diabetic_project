# -*- coding: utf-8 -*-
"""Diebetic_project.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1d_QDGx12birBG2ZewhWzRgU4WY9TcY0K

importing importent libreay,
numpy for creating array,
pandas for extrating data,
"""

import numpy as np
import pandas as pd
from sklearn.preprocessing  import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.metrics import accuracy_score

"""Data collection and Analysis

losing of data in csv file
"""

diabetic_dataset = pd.read_csv('/content/diabetes.csv')

# print the 5 rows
diabetic_dataset.head()

# calculating Row and column
diabetic_dataset.shape

diabetic_dataset.describe()

"""diebetic_dataset['Outcome'].value_counts()"""

diabetic_dataset['Outcome'].value_counts()

diabetic_dataset.groupby('Outcome').mean()

"""create a veriable X excluding outcome and Y for only outcome data"""

X = diabetic_dataset.drop(columns = 'Outcome',axis =1)   #  for row axis = 0
Y = diabetic_dataset['Outcome']

print(X)
print(Y)

"""Data Standardization"""

scalar = StandardScaler()

scalar.fit(X)

standardize_data = scalar.transform(X)

print(standardize_data)

X =standardize_data

print(X)
print(Y)

"""Test Case spliting"""

X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size = 0.1 ,stratify = Y,random_state = 2)

print(X.shape,X_train.shape,X_test.shape)

"""training the model"""

classifier = svm.SVC(kernel = 'linear')

"""Training support vector Machine classifier """

classifier.fit(X_train, Y_train)

"""Model Evolution

Accuracy score
"""

#accuracy score on training data
X_train_prediction = classifier.predict(X_train)
training_data_accuarcy = accuracy_score(X_train_prediction,Y_train)

print('training accuracy is = ',training_data_accuarcy)

#accuracy score on test data
X_test_prediction = classifier.predict(X_test)
test_data_accuarcy = accuracy_score(X_test_prediction,Y_test)

print('test data accuracy is = ',test_data_accuarcy)

"""Making a Predictive system"""

input_data =(2,197,70,45,543,30.5,0.158,53)

# changing the input data list to numpy array
input_data_as_numpy_arr = np.asarray(input_data)

#reshape the array for one instance
input_data_reshape = input_data_as_numpy_arr.reshape(1,-1)

#standradize the input_data
std_data = scalar.transform(input_data_reshape)
print(std_data)

prediction =classifier.predict(std_data)
print(prediction)

if(prediction[0] == 0):
  print('The presion is Non-diabetic')
else:
  print('The persion is diabetic')