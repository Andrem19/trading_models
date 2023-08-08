# Import the necessary libraries
import pandas as pd
import torch
import torch.nn as nn
import torch.nn.functional as F
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split

# Read the data from CSV file
data = pd.read_csv('finaly/training_data.csv')

# Preprocess the string data
for column in data.columns:
    if data.dtypes[column] == 'object':
        le = LabelEncoder()
        data[column] = le.fit_transform(data[column])

# Extract the features and target variable
X = data.iloc[:, :-1].values
y = data.iloc[:, -1].values

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Convert the training and testing sets to PyTorch tensors
X_train_tensor = torch.from_numpy(X_train).type(torch.float)
X_test_tensor = torch.from_numpy(X_test).type(torch.float)
y_train_tensor = torch.from_numpy(y_train).type(torch.long)
y_test_tensor = torch.from_numpy(y_test).type(torch.long)

# Create the model
class LogisticRegressionModel(nn.Module):
    def __init__(self, feature_dim):
        super(LogisticRegressionModel, self).__init__()
        self.fc1 = nn.Linear(feature_dim, 2)
    def forward(self, x):
        x = self.fc1(x)
        x = F.softmax(x, dim=1)
        return x

# Create the model, optimizer, and criterion
model = LogisticRegressionModel(feature_dim=X_train.shape[1])
optimizer = torch.optim.Adam(params=model.parameters(), lr=0.01)
criterion = nn.CrossEntropyLoss()

# Train the model
model.train()
for e in range(100):
    optimizer.zero_grad()
    output = model(X_train_tensor)
    loss = criterion(output, y_train_tensor)
    loss.backward()
    optimizer.step()

# Evaluate the model
model.eval()
with torch.no_grad():
    output = model(X_test_tensor)
    loss = F.cross_entropy(output, y_test_tensor).item()
    accuracy = (output.argmax(dim=1) == y_test_tensor).sum().item() / len(y_test_tensor)
    print("Model accuracy:", accuracy)