import pandas as pd
import numpy as np
import os
import csv
from sklearn.linear_model import LinearRegression

path = 'data/'
files = ['ADAUSDT_15m.csv', 'BNBUSDT_15m.csv', 'BTCUSDT_15m.csv', 'ETHUSDT_15m.csv', 'XRPUSDT_15m.csv', 'DOTUSDT_15m.csv']
target_path = 'cases'

pattern_length = 10
change_length = 6
change_threshold = 0.03

def get_patterns(data):
    patterns = []
    for i in range(len(data) - pattern_length - change_length + 1):
        pattern = data[i:i+pattern_length]
        target = data[i+pattern_length+change_length-1]
        if target >= (1 + change_threshold) * pattern[-1]:
            patterns.append((pattern, 1))
        elif target <= (1 - change_threshold) * pattern[-1]:
            patterns.append((pattern, 0))
    return patterns

def save_patterns(patterns):
    all_patterns = []
    for pattern, label in patterns:
       all_patterns.append([*pattern, label])
    return all_patterns

def save_patterns_to_csv(patterns, coin_name):
    output_filepath = os.path.join(target_path, f'{coin_name}_patterns.csv')
    with open(output_filepath, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(patterns)

for file in files:
    coin_name = file.split('_')[0]
    file_path = os.path.join(path, file)

    df = pd.read_csv(file_path, header=None)
    data = df.values[:, 1]  # assuming the price is in the second column

    patterns = get_patterns(data)
    patterns_list = save_patterns(patterns)
    save_patterns_to_csv(patterns_list, coin_name)

print('Patterns saved successfully.')

