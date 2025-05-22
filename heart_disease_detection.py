# heart_disease_detection.py

# Step 1: Import required libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

import pickle

# Step 2: Load the dataset
file_path = r'C:\Users\Nitesh k. sahoo\Downloads\Projects-20240722T093004Z-001\Projects\heart_disease\Heart Disease\dataset.csv'
data = pd.read_csv(file_path)

# Display basic information
print("First 5 rows of the dataset:")
print(data.head())

print("\nDataset Info:")
print(data.info())

# Step 3: Check for missing values
print("\nMissing values in each column:")
print(data.isnull().sum())

# Step 4: Prepare features (X) and target (y)
X = data.drop('target', axis=1)  # Features
y = data['target']              # Target
         

# Step 5: Feature Scaling
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Step 6: Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y, test_size=0.2, random_state=42
)

# Step 7: Train the Logistic Regression model
model = LogisticRegression()
model.fit(X_train, y_train)

# Step 8: Make predictions and evaluate
y_pred = model.predict(X_test)

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))

print("\nClassification Report:")
print(classification_report(y_test, y_pred))

print("Accuracy Score:", accuracy_score(y_test, y_pred))

# Step 9: Save the model and scaler
with open('heart_disease_model.pkl', 'wb') as model_file:
    pickle.dump(model, model_file)

with open('scaler.pkl', 'wb') as scaler_file:
    pickle.dump(scaler, scaler_file)

print("\n✅ Model and Scaler saved successfully!")
