import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import GridSearchCV

# Read the data from CSV file
data = pd.read_csv('data/combined_patterns.csv')

# Preprocess the string data
for column in data.columns:
    if data.dtypes[column] == 'object':
        le = LabelEncoder()
        data[column] = le.fit_transform(data[column])

# Extract the features and target variable
X = data.iloc[:, :-1]
y = data.iloc[:, -1]

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Define the parameter grid for grid search
param_grid = {'C': [0.001, 0.01, 0.1, 1, 10]}

# Create the logistic regression model
model = LogisticRegression()

# Perform grid search
grid_search = GridSearchCV(model, param_grid, cv=5)
grid_search.fit(X_train, y_train)

# Get the best hyperparameters
best_params = grid_search.best_params_

# Create a new model with the best hyperparameters
model = LogisticRegression(**best_params)

# Train the logistic regression model
model.fit(X_train, y_train)

# Evaluate the model
accuracy = model.score(X_test, y_test)
print("Model accuracy:", accuracy)


