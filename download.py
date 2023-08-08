from binance_historical_data import BinanceDataDumper
import multiprocessing

def main():
    # Define the symbols and intervals for the historical data
    symbols = ['ETHUSDT', 'DOTUSDT', 'BNBUSDT', 'ADAUSDT', 'BTCUSDT', 'XRPUSDT']

    # Download the historical data for each symbol and save it to the specified folder
    for symbol in symbols:
        data_dumper = BinanceDataDumper(
            path_dir_where_to_dump="newdata",
            asset_class="spot",  # spot, um, cm
            data_type="klines",  # aggTrades, klines, trades
            data_frequency="15m",
        )
        data_dumper.dump_data(
            tickers=symbol,
            date_start=None,
            date_end=None,
            is_to_update_existing=False,
            tickers_to_exclude=["UST"],
        )

if __name__ == '__main__':
    multiprocessing.freeze_support()
    main()
