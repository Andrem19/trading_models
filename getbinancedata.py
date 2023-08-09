import time
from binance.client import Client
import os
from dotenv import load_dotenv
import helpers.rel as rel
import helpers.predict as pr
import pandas as pd
import train4 as tr
import predict as p

# Load variables from the .env file
load_dotenv()
coins = ['ETHUSDT', 'DOTUSDT', 'BNBUSDT', 'ADAUSDT', 'BTCUSDT', 'XRPUSDT']
# Enter your Binance API credentials here
api_key = os.getenv("API_KEY")
api_secret = os.getenv("API_SECRET")

# Initialize the Binance API client
client = Client(api_key, api_secret)

# Function to fetch the last 11 candles for a given symbol and interval
def get_last_12_candles(symbol, interval):
    candles = client.get_klines(symbol=symbol, interval=interval, limit=12)
    
    # Cut every candle before returning
    cut_candles = []
    for candle in candles:
        open = candle[1]
        high = candle[2]
        low = candle[3]
        close = candle[4]
        volume = candle[5]
        cut_candles.append([float(open), float(high), float(low), float(close), float(volume)])
    
    return rel.convert_to_relative2(cut_candles[1:], cut_candles[0], 3)

# Main loop to fetch candles every 15 minutes
while True:
    for c in coins:
        candles = get_last_12_candles(c, Client.KLINE_INTERVAL_5MINUTE)
        print(candles)
        # pr.pred(candles)
        tr.train(candles[:-5], c)
        # p.pred2(candles[:-5])
    # Sleep for 15 minutes (900 seconds)
    time.sleep(300)