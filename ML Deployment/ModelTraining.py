"""
Author : Rahul Bordoloi
Dated : 22nd November, 2020
Dataset Reference : https://www.kaggle.com/ritesaluja/bank-note-authentication-uci-data
"""

# Importing Libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import pickle

# Reading the Dataset
data = pd.read_csv('BankNote_Authentication.csv')

# Splitting into Independent and Dependent Features
x = data.iloc[:, :-1]
y = data.iloc[:, -1]

# Train-Test Split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.3, stratify = y, random_state = 0, shuffle = True)

# Implementing Random Forest Classifier
model = RandomForestClassifier(random_state = 0, n_jobs = -1)
model.fit(x_train, y_train)

# Prediction on the Test Set
y_pred = model.predict(x_test)

# Checking Accuracy
print(f"Model Accuracy Score: {accuracy_score(y_test, y_pred)}")

# Checking Random Results
print(f'Dummy Prediction : {model.predict([[2, 3, 4, 1]])[0]}')

# Creating a Pickle File to Serialize the Model
filename = "classifier.pkl"
pickle.dump(model, open(filename, 'wb'))


