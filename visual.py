import csv
import ast
import matplotlib.pyplot as plt

data = []

with open('data/falling_patterns.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        row_data = [ast.literal_eval(value) for value in row]
        data.append(row_data)

# print(data)
# cand_data = data[1]
# print(cand_data)

for cand_data in data[1:]:
    # Extracting the candle data
    open_time = [candle[0] for candle in cand_data]
    open_price = [candle[1] for candle in cand_data]
    high_price = [candle[2] for candle in cand_data]
    low_price = [candle[3] for candle in cand_data]
    close_price = [candle[4] for candle in cand_data]
    volume = [candle[5] for candle in cand_data]

    # Plotting the candle data
    plt.figure(figsize=(10, 6))
    plt.plot(open_time, open_price, label='Open')
    plt.plot(open_time, high_price, label='High')
    plt.plot(open_time, low_price, label='Low')
    plt.plot(open_time, close_price, label='Close')
    plt.bar(open_time, volume, label='Volume')

    # Formatting the plot
    plt.xlabel('Open Time')
    plt.ylabel('Price / Volume')
    plt.title('Candlestick Chart')
    plt.legend()

    # Adjusting the y-axis limits for better visualization
    plt.ylim(min(low_price) - 0.1*(max(high_price)-min(low_price)), max(high_price) + 0.1*(max(high_price)-min(low_price)))

    # Displaying the plot
    plt.show()