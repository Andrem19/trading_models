import pandas as pd

# Load the falling_patterns.csv file
falling_data = pd.read_csv('data/falling_patterns.csv')

# Remove the quotes from the column values
falling_data = falling_data.apply(lambda x: x.str.strip('[]"'))

# Save the modified dataframe with the same name
falling_data.to_csv('data/falling_patterns.csv', index=False)

# Load the rising_patterns.csv file
rising_data = pd.read_csv('data/rising_patterns.csv')

# Remove the quotes from the column values
rising_data = rising_data.apply(lambda x: x.str.strip('[]"'))

# Save the modified dataframe with the same name
rising_data.to_csv('data/rising_patterns.csv', index=False)

