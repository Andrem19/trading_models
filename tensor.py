# Import essential libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import tensorflow as tf

# Read the data from CSV
data = pd.read_csv('finaly/training_data.csv')

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

# Define model parameters
learning_rate = 0.001
num_epochs = 50
batch_size = 128

# Create input functions
train_input_fn = tf.compat.v1.estimator.inputs.pandas_input_fn(X_train, y_train, batch_size=batch_size,num_epochs=num_epochs, shuffle=True)
test_input_fn = tf.compat.v1.estimator.inputs.pandas_input_fn(X_test, y_test,batch_size=batch_size, num_epochs=num_epochs, shuffle=False)

# Create feature columns
feature_columns = [tf.feature_column.numeric_column(key=column) for column in X_train.columns]

# Instantiate deep learning model
optimizer = tf.keras.optimizers.legacy.Adam(learning_rate=learning_rate)
model = tf.estimator.DNNClassifier(hidden_units=[64, 64], feature_columns=feature_columns, optimizer=optimizer)

# Train the model
model.train(input_fn=train_input_fn, steps=None)

# Evaluate the model
metrics = model.evaluate(input_fn=test_input_fn)
print('Model accuracy:', metrics["accuracy"])
