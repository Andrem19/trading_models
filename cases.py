import pandas as pd
import numpy as np
import os

path = 'data/'
files = ['ADAUSDT_15m.csv', 'BNBUSDT_15m.csv', 'BTCUSDT_15m.csv', 'ETHUSDT_15m.csv', 'XRPUSDT_15m.csv', 'DOTUSDT_15m.csv']
target_path = 'cases'

pattern_length = 10
target_lenth = 6
positive_threshold = 0.035
negative_threshold = -0.035

for file in files:
    # Read the csv file
    data = pd.read_csv(os.path.join(path, file), header=None)
    
    # Calculate the percentage change for each candle
    data['percentage_change'] = (data[3] - data[0]) / data[0]
    
    # Find positive patterns
    positive_patterns = []
    for i in range(len(data)-pattern_length-target_lenth):
        pattern = data[i:i+pattern_length+target_lenth]
        if pattern['percentage_change'].iloc[-1] > positive_threshold:
            pattern_values = list(pattern['percentage_change'].values.astype(str))
            pattern_values.append('1')
            positive_patterns.append(pattern_values)
    
    # Find negative patterns
    negative_patterns = []
    for i in range(len(data)-pattern_length-target_lenth):
        pattern = data[i:i+pattern_length+target_lenth]
        if pattern['percentage_change'].iloc[-1] < negative_threshold:
            pattern_values = list(pattern['percentage_change'].values.astype(str))
            pattern_values.append('0')
            negative_patterns.append(pattern_values)
    
    # Create a folder for the patterns if it doesn't exist
    coin_name = file.split('_')[0]
    coin_folder = os.path.join(target_path, coin_name)
    os.makedirs(coin_folder, exist_ok=True)
    
    # Save the patterns in a single file for each coin
    with open(os.path.join(coin_folder, f'{coin_name}_patterns.csv'), 'w') as file:
        for pattern in positive_patterns:
            file.write(','.join(pattern))
            file.write('\n')
        
        for pattern in negative_patterns:
            file.write(','.join(pattern))
            file.write('\n')


