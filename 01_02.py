import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def symbol_to_path(symbol, base_dir="data"):
    return os.path.join(base_dir, "{}.csv".format(str(symbol)))

def get_data(symbols, dates):
    df = pd.DataFrame(index=dates)
    if 'SPY' not in symbols:
        symbols.insert(0, 'SPY')
    for symbol in symbols:
        df_temp = pd.read_csv(symbol_to_path(symbol), index_col='Date', parse_dates=True, usecols=['Date', 'Adj Close'], na_values=['nan'])
        df_temp = df_temp.rename(columns={'Adj Close': symbol})
        df = df.join(df_temp)
        if symbol == 'SPY':
                df = df.dropna(subset=['SPY'])

    return df


def run_test():
    symbols = ['GOOG', 'IBM', 'GLD']
    date_start = '2010-01-01'
    end_date = '2010-12-31'
    dates = pd.date_range(date_start, end_date)
    df = get_data(symbols, dates)
    print df
    


if __name__ == '__main__':
    run_test()
