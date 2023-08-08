import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np
import getdata
import os

path = 'data/'
files = ['ADAUSDT_15m.csv', 'BNBUSDT_15m.csv', 'BTCUSDT_15m.csv', 'ETHUSDT_15m.csv', 'XRPUSDT_15m.csv', 'DOTUSDT_15m.csv']
target_path = 'cases'

pattern_length = 10
change_length = 6
change_threshold = 0.03

def convert_to_relative(data, first, type):
    newdata = []
    for i in range(len(data)):
        
        if i == 0:
            previous_candle = first
        else:
            previous_candle = data[i - 1]
        current_candle = data[i]

        if previous_candle[0] != 0 and previous_candle[0] != current_candle[0]:
            if previous_candle[0] < current_candle[0]:
                relative_open = round((current_candle[0] - previous_candle[0]) / previous_candle[0], 2)
            else:
                relative_open = -round((previous_candle[0] - current_candle[0]) / previous_candle[0], 2)
        else:
            relative_open = 0
        
        if previous_candle[1] != 0 and previous_candle[1] != current_candle[1]:
            if previous_candle[1] < current_candle[1]:
                relative_high = round((current_candle[1] - previous_candle[1]) / previous_candle[1], 2)
            else:
                relative_high = -round((previous_candle[1] - current_candle[1]) / previous_candle[1], 2)
        else:
            relative_high = 0
        
        if previous_candle[2] != 0 and previous_candle[2] != current_candle[2]:
            if previous_candle[2] < current_candle[2]:
                relative_low = round((current_candle[2] - previous_candle[2]) / previous_candle[2], 2)
            else:
                relative_low = -round((previous_candle[2] - current_candle[2]) / previous_candle[2], 2)
        else:
            relative_low = 0
        
        if previous_candle[3] != 0 and previous_candle[3] != current_candle[3]:
            if previous_candle[3] < current_candle[3]:
                relative_close = round((current_candle[3] - previous_candle[3]) / previous_candle[3], 2)
            else:
                relative_close = -round((previous_candle[3] - current_candle[3]) / previous_candle[3], 2)
        else:
            relative_close = 0
        
        if previous_candle[4] != 0 and previous_candle[4] != current_candle[4]:
            if previous_candle[4] < current_candle[4]:
                relative_volume = round((current_candle[4] - previous_candle[4]) / previous_candle[4], 2)
            else:
                relative_volume = -round((previous_candle[4] - current_candle[4]) / previous_candle[4], 2)
        else:
            relative_volume = 0

        # data[i] = [relative_open, relative_high, relative_low, relative_close, relative_volume]
        newdata.append([relative_open, relative_high, relative_low, relative_close, relative_volume])
    newdata.append(type)
    return newdata

def find_rising_patterns(data):
    rising_patterns = []
    for i in range(len(data)-(pattern_length+1)):
        prices = [candle[3] for candle in data[i:i+pattern_length]]
        target_price = data[i+change_length][3]
        reg = LinearRegression().fit(np.arange(pattern_length).reshape(-1, 1), prices)
        slope = reg.coef_[0]
        if slope > 0 and (target_price - prices[-1]) / prices[-1] >= change_threshold:
            rising_patterns.append(convert_to_relative(data[i:i+pattern_length], data[i-1], 1))
    return rising_patterns

def find_falling_patterns(data):
    falling_patterns = []
    for i in range(len(data)-(pattern_length+1)):
        prices = [candle[3] for candle in data[i:i+pattern_length]]
        target_price = data[i+change_length][3]
        reg = LinearRegression().fit(np.arange(pattern_length).reshape(-1, 1), prices)
        slope = reg.coef_[0]
        if slope < 0 and (target_price - prices[-1]) / prices[-1] <= -change_threshold:
            falling_patterns.append(convert_to_relative(data[i:i+pattern_length], data[i-1], 0))
    return falling_patterns


for file in files:
    coin_name = file.split('_')[0]
    file_path = os.path.join(path, file)
    data = getdata.get_csv_data(file_path)
    rising_patterns = find_rising_patterns(data)
    
    rising_df = pd.DataFrame(rising_patterns)
    rising_df.to_csv(f'{target_path}/{coin_name}_rising_patterns.csv', index=False)

    falling_patterns = find_falling_patterns(data)

    falling_df = pd.DataFrame(falling_patterns)
    falling_df.to_csv(f'{target_path}/{coin_name}_falling_patterns.csv', index=False)
