import getdata
import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np

data = getdata.get_csv_data()

def find_rising_patterns(data):
    rising_patterns = []
    for i in range(len(data)-11):
        prices = [candle[4] for candle in data[i:i+10]]  # Get the closing prices of each candle in the pattern
        target_price = data[i+10][4]  
        reg = LinearRegression().fit(np.arange(10).reshape(-1, 1), prices)  # Fit linear regression model
        slope = reg.coef_[0]  # Get the slope of the regression line
        if slope > 0 and (target_price - prices[-1]) / prices[-1] >= 0.035:  # If the slope is positive and the next day's price increased by at least 3%, it's a rising pattern
            rising_patterns.append(data[i:i+10])
    return rising_patterns

def find_falling_patterns(data):
    falling_patterns = []
    for i in range(len(data)-11):
        prices = [candle[4] for candle in data[i:i+10]]  # Get the closing prices of each candle in the pattern
        target_price = data[i+10][4]  
        reg = LinearRegression().fit(np.arange(10).reshape(-1, 1), prices)  # Fit linear regression model
        slope = reg.coef_[0]  # Get the slope of the regression line
        if slope < 0 and (target_price - prices[-1]) / prices[-1] <= -0.035:  # If the slope is negative and the next day's price decreased by at least 3%, it's a falling pattern
            falling_patterns.append(data[i:i+10])
    return falling_patterns

# Find rising patterns
rising_patterns = find_rising_patterns(data)

# Save rising patterns in a file
rising_df = pd.DataFrame(rising_patterns)
rising_df.to_csv('data/rising_patterns.csv', index=False)

# Find falling patterns
falling_patterns = find_falling_patterns(data)

# Save falling patterns in a file
falling_df = pd.DataFrame(falling_patterns)
falling_df.to_csv('data/falling_patterns.csv', index=False)
