import pandas as pd
import glob
import os

first_file_path = 'newdata/spot/monthly/klines/XRPUSDT/15m/XRPUSDT-15m-2018-05.csv'

# Get a list of all the files between the first and last file
file_list = glob.glob('newdata/spot/monthly/klines/XRPUSDT/15m/XRPUSDT-15m-*.csv')
file_list.sort()

# Use the first file to initialize the final dataframe
df_final = pd.read_csv(first_file_path, header=None, usecols=[1, 2, 3, 4, 5])

# Iterate over the remaining files and append their data to the final dataframe
for file_path in file_list[1:]:
    df = pd.read_csv(file_path, header=None, usecols=[1, 2, 3, 4, 5])
    df_final = pd.concat([df_final, df])

# Save the final dataframe to a new CSV file
df_final.to_csv('data/XRPUSDT_15m.csv', header=False, index=False)


