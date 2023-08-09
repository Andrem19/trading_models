import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.linear_model import LogisticRegression
import pickle
import numpy as np
import telegram as tg
def train_model():
    # # Load the training data from 'finaly/training_data2.csv'
    data = pd.read_csv('finaly/training_data5.csv')

    # # Separate the features (X) and the target variable (y)
    X = data.iloc[:, :-1].values
    y = data.iloc[:, -1].values

    # # Split the data into training and test sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # # Standardize the features
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    # # Create and fit the LabelEncoder
    # label_encoder = LabelEncoder()
    # y_train_encoded = label_encoder.fit_transform(y_train)
    # y_test_encoded = label_encoder.transform(y_test)

    # # Train a logistic regression model
    model = LogisticRegression(max_iter=1000)
    model.fit(X_train, y_train)

    # # Evaluate the model
    accuracy = model.score(X_test, y_test)
    print("Accuracy:", accuracy)
    return model

def train(model, res_data, coin):
    # # Load the training data from 'finaly/training_data2.csv'
    data = pd.read_csv('finaly/training_data5.csv')

    # # Separate the features (X) and the target variable (y)
    X = data.iloc[:, :-1].values
    y = data.iloc[:, -1].values

    # # Split the data into training and test sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # # Standardize the features
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)
    # Save the model to a file
    model_filename = 'models/trained_model7.pkl'
    with open(model_filename, 'wb') as file:
        pickle.dump(model, file)

    # # Save the LabelEncoder to a file
    # label_encoder_filename = 'models/label_encoder.pkl'
    # with open(label_encoder_filename, 'wb') as le_file:
    #     pickle.dump(label_encoder, le_file)
    
    data_to_predict = [-3.03,-1.98,-0.01,0.93,-58.31,0.98,0.23,0.72,-0.3,-60.42,-0.35,-0.33,-0.22,-0.34,-37.68,-0.33,-0.15,-0.47,0.46,134.26,0.46,0.0,0.19,-0.37,-30.88,-0.39,-0.46,-2.09,-2.1,193.84,-2.02,-2.01,-3.15,-3.67,73.8,-3.73,-1.12,-0.01,2.33,-29.75,2.37,1.44,2.33,1.34,-36.71,1.36,-0.21,0.58,0.08,-34.08]
    # Convert the data_to_predict into a numpy array
    data_to_predict = res_data
    data_to_predict = np.array(data_to_predict).reshape(1, -1)

    # Standardize the data_to_predict
    scaled_data_to_predict = scaler.transform(data_to_predict)

    # Make prediction
    prediction = model.predict(scaled_data_to_predict)
    probabilities = model.predict_proba(scaled_data_to_predict)
    print(coin)
    print("Predictions:", prediction)
    print("Predicted Probabilities:", probabilities)
    if probabilities[0][0] > 0.90 or probabilities[0][1] > 0.90:
        message = f'"{coin} - Predictions:", {prediction}\nPredicted Probabilities: {probabilities}'
        tg.send_inform_message(message)