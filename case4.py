import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np
import helpers.getdata as gd
import os
import helpers.rel as rel

path = 'data/'
files = ['ADAUSDT_5m.csv', 'BNBUSDT_5m.csv', 'BTCUSDT_5m.csv', 'ETHUSDT_5m.csv', 'XRPUSDT_5m.csv', 'DOTUSDT_5m.csv']
target_path = 'cases5'

pattern_length = 10
change_length = 6
change_threshold = 0.01

# def find_rising_patterns(data):
#     rising_patterns = []
#     for i in range(len(data)-(pattern_length+1)):
#         prices = [candle[3] for candle in data[i:i+pattern_length]]
#         target_price = data[i+change_length][3]
#         reg = LinearRegression().fit(np.arange(pattern_length).reshape(-1, 1), prices)
#         slope = reg.coef_[0]
#         if slope > 0 and (target_price - prices[-1]) / prices[-1] >= change_threshold:
#             rising_patterns.append(rel.convert_to_relative2(data[i:i+pattern_length], data[i-1], 1))
#     return rising_patterns

# def find_falling_patterns(data):
#     falling_patterns = []
#     for i in range(len(data)-(pattern_length+1)):
#         prices = [candle[3] for candle in data[i:i+pattern_length]]
#         target_price = data[i+change_length][3]
#         reg = LinearRegression().fit(np.arange(pattern_length).reshape(-1, 1), prices)
#         slope = reg.coef_[0]
#         if slope < 0 and (target_price - prices[-1]) / prices[-1] <= -change_threshold:
#             falling_patterns.append(rel.convert_to_relative2(data[i:i+pattern_length], data[i-1], 0))
#     return falling_patterns
def find_rising_patterns(data):
    rising_patterns = []
    for i in range(len(data)-(pattern_length+1)):
        prices = [candle[3] for candle in data[i:i+pattern_length]]
        target_prices = [candle[1] for candle in data[i+1:i+change_length]]
        reg = LinearRegression().fit(np.arange(pattern_length).reshape(-1, 1), prices)
        slope = reg.coef_[0]
        if slope > 0 and (max(target_prices) - prices[-1]) / prices[-1] >= change_threshold:
            rising_patterns.append(rel.convert_to_relative2(data[i:i+pattern_length], data[i-1], 1))
    return rising_patterns


def find_falling_patterns(data):
    falling_patterns = []
    for i in range(len(data)-(pattern_length+1)):
        prices = [candle[3] for candle in data[i:i+pattern_length]]
        target_prices = [candle[2] for candle in data[i+1:i+change_length]]
        reg = LinearRegression().fit(np.arange(pattern_length).reshape(-1, 1), prices)
        slope = reg.coef_[0]
        if slope < 0 and (min(target_prices) - prices[-1]) / prices[-1] <= -change_threshold:
            falling_patterns.append(rel.convert_to_relative2(data[i:i+pattern_length], data[i-1], 0))
    return falling_patterns


for file in files:
    coin_name = file.split('_')[0]
    file_path = os.path.join(path, file)
    data = gd.get_csv_data(file_path)
    rising_patterns = find_rising_patterns(data)
    
    rising_df = pd.DataFrame(rising_patterns)
    rising_df.to_csv(f'{target_path}/{coin_name}_rising_patterns.csv', index=False)

    falling_patterns = find_falling_patterns(data)

    falling_df = pd.DataFrame(falling_patterns)
    falling_df.to_csv(f'{target_path}/{coin_name}_falling_patterns.csv', index=False)
