import pandas as pd
import pickle
from sklearn.preprocessing import LabelEncoder
import warnings
from sklearn.preprocessing import LabelEncoder

def pred():
    data_to_predict = pd.read_csv('data_to_predict3.csv')

    for column in data_to_predict.columns: 
        if data_to_predict.dtypes[column] == 'object': 
            le = LabelEncoder() 
            data_to_predict[column] = le.fit_transform(data_to_predict[column])

    filename = 'models/trained_model6.pkl' 
    with open(filename, 'rb') as file: 
        model = pickle.load(file)

    predictions = model.predict(data_to_predict)
    probabilities = model.predict_proba(data_to_predict)
    print("Predictions:", predictions)
    print("Predicted Probabilities:", probabilities)

def pred2(data):
    # Convert the array into a DataFrame
    data_to_predict = pd.DataFrame([data])

    # Load the LabelEncoder from file if it exists
    try:
        with open('models/label_encoder.pkl', 'rb') as le_file:
            le = pickle.load(le_file)
    except FileNotFoundError:
        le = LabelEncoder()

    # Load the trained model from file
    try:
        with open('models/trained_model6.pkl', 'rb') as model_file:
            model = pickle.load(model_file)
    except FileNotFoundError:
        print("Trained model file not found")

    # Apply label encoding on the columns
    for column in data_to_predict.columns:
        if data_to_predict.dtypes[column] == 'object':
            data_to_predict[column] = le.transform(data_to_predict[column])

    # Transform the data using the loaded LabelEncoder
    for column in data_to_predict.columns:
        if data_to_predict.dtypes[column] == 'object':
            data_to_predict[column] = le.transform(data_to_predict[column])

    predictions = model.predict(data_to_predict)
    probabilities = model.predict_proba(data_to_predict)

    print("Predictions:", predictions)
    print("Predicted Probabilities:", probabilities)

