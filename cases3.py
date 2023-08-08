import pandas as pd
import numpy as np
import os
from sklearn.linear_model import LinearRegression

# Variables
pattern_length = 10
target_length = 6
positive_threshold = 0.035
negative_threshold = -0.035

path = 'data/'
files = ['ADAUSDT_15m.csv', 'BNBUSDT_15m.csv', 'BTCUSDT_15m.csv', 'ETHUSDT_15m.csv', 'XRPUSDT_15m.csv', 'DOTUSDT_15m.csv']
target_path = 'cases'

def find_rising_patterns(data):
    rising_patterns = []
    for i in range(len(data)-(pattern_length+target_length+1)):
        prices = [candle[4] for candle in data[i:i+pattern_length]]  # Get the closing prices of each candle in the pattern
        target_price = data[i+pattern_length+target_length][4]  
        reg = LinearRegression().fit(np.arange(pattern_length).reshape(-1, 1), prices)  # Fit linear regression model
        slope = reg.coef_[0]  # Get the slope of the regression line
        if slope > 0 and (target_price - prices[-1]) / prices[-1] >= positive_threshold:  # If the slope is positive and the next day's price increased by at least 3%, it's a rising pattern
            rising_patterns.append(data[i:i+pattern_length])
    return rising_patterns

def find_falling_patterns(data):
    falling_patterns = []
    for i in range(len(data)-(pattern_length+target_length+1)):
        prices = [candle[4] for candle in data[i:i+pattern_length]]  # Get the closing prices of each candle in the pattern
        target_price = data[i+pattern_length+target_length][4]  
        reg = LinearRegression().fit(np.arange(pattern_length).reshape(-1, 1), prices)  # Fit linear regression model
        slope = reg.coef_[0]  # Get the slope of the regression line
        if slope < 0 and (target_price - prices[-1]) / prices[-1] <= negative_threshold:  # If the slope is negative and the next day's price decreased by at least 3%, it's a falling pattern
            falling_patterns.append(data[i:i+pattern_length])
    return falling_patterns

for file in files:
    # Read the csv file
    data = pd.read_csv(os.path.join(path, file), header=None).values
    
    # Find patterns
    rising_patterns = find_rising_patterns(data)
    falling_patterns = find_falling_patterns(data)
    
    # Create a folder for the patterns if it doesn't exist
    coin_name = file.split('_')[0]
    coin_folder = os.path.join(target_path, coin_name)
    os.makedirs(coin_folder, exist_ok=True)
    
    # Save the patterns in separate files for each type of pattern
    with open(os.path.join(coin_folder, f'{coin_name}_rising_patterns.csv'), 'w') as file:
        for pattern in rising_patterns:
            file.write(','.join([str(value) for value in pattern.flatten()]))
            file.write('\n')
    
    with open(os.path.join(coin_folder, f'{coin_name}_falling_patterns.csv'), 'w') as file:
        for pattern in falling_patterns:
            file.write(','.join([str(value) for value in pattern.flatten()]))
            file.write('\n')
