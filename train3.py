import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix, roc_curve, roc_auc_score
import matplotlib.pyplot as plt
import pickle

# Read the data from CSV file
data = pd.read_csv('finaly/training_data2.csv')

# Preprocess the data (handle missing values, outliers, scaling)
# Add your preprocessing code here
for column in data.columns:
    if data.dtypes[column] == 'object':
        le = LabelEncoder()
        data[column] = le.fit_transform(data[column])

# Extract the features and target variable
X = data.iloc[:, :-1]
y = data.iloc[:, -1]

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Define the parameter grid for grid search
param_grid = {'n_estimators': [100, 200, 300], 'max_depth': [3, 5, 7]}

# Create the random forest model
model = RandomForestClassifier()

# Perform grid search for hyperparameter tuning
grid_search = GridSearchCV(model, param_grid, cv=5)
grid_search.fit(X_train, y_train)

# Get the best hyperparameters
best_params = grid_search.best_params_

# Create a new model with the best hyperparameters
model = RandomForestClassifier(**best_params)

# Train the random forest model
model.fit(X_train, y_train)

# Save the model to a file
filename = 'models/trained_model5.pkl'
with open(filename, 'wb') as file:
    pickle.dump(model, file)

# Evaluate the model
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)
confusion = confusion_matrix(y_test, y_pred)
roc_auc = roc_auc_score(y_test, y_pred)

print("Model accuracy:", accuracy)
print("Model precision:", precision)
print("Model recall:", recall)
print("Model F1-score:", f1)
print("Confusion matrix:\n", confusion)
print("ROC AUC score:", roc_auc)

# Plot ROC curve
y_pred_proba = model.predict_proba(X_test)[:, 1]
fpr, tpr, thresholds = roc_curve(y_test, y_pred_proba)
plt.plot(fpr, tpr)
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Receiver Operating Characteristic')
plt.show()


