import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import GridSearchCV
import pickle


# Read the data from CSV file
data = pd.read_csv('finaly/training_data.csv')
#Example data in csv file: Header = 0,1,2,3,4,5,6,7,8,9,type Data = "[-0.0, 0.04, 0.01, 0.01, 2.08]","[0.01, -0.01, 0.01, 0.01, -0.17]","[0.01, -0.01, -0.01, -0.0, 0.27]","[-0.0, 0, -0.02, -0.04, 0.12]","[-0.03, -0.03, -0.03, -0.02, 0.47]","[-0.02, -0.02, 0.0, -0.02, -0.41]","[-0.02, -0.01, -0.02, -0.01, -0.26]","[-0.01, 0.01, 0.01, 0.02, -0.19]","[0.02, -0.0, 0.02, 0.01, 0.08]","[0.01, 0.01, 0.01, 0.01, -0.13]",0
# Preprocess the string data
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

# Perform grid search
grid_search = GridSearchCV(model, param_grid, cv=5)
grid_search.fit(X_train, y_train)

# Get the best hyperparameters
best_params = grid_search.best_params_

# Create a new model with the best hyperparameters
model = RandomForestClassifier(**best_params)

# Train the random forest model
model.fit(X_train, y_train)

# Save the model to a file in the "models" folder
filename = 'models/trained_model.pkl'
with open(filename, 'wb') as file:
    pickle.dump(model, file)

# Evaluate the model
accuracy = model.score(X_test, y_test)
print("Model accuracy:", accuracy)
