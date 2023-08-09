import pandas as pd
import pickle
import numpy as np
from sklearn.preprocessing import StandardScaler
import telegram as tg

def pred(data_to_predict):
    data_to_predict = np.array(data_to_predict).reshape(1, -1)

    scaler = StandardScaler()

    filename = 'models/trained_model6.pkl' 
    with open(filename, 'rb') as file: 
        model = pickle.load(file)

    scaler.fit(data_to_predict) # Fit the scaler on the data_to_predict

    # Standardize the data_to_predict
    scaled_data_to_predict = scaler.transform(data_to_predict)

    # Make prediction
    prediction = model.predict(scaled_data_to_predict)
    probabilities = model.predict_proba(scaled_data_to_predict)

    print("Predictions:", prediction)
    print("Predicted Probabilities:", probabilities)
    message = f'"Predictions:", {prediction}\nPredicted Probabilities: {probabilities}'
    tg.send_inform_message(message)
