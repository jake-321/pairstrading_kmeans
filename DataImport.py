import pandas as pd
import numpy as np
import yfinance as yf
import matplotlib.pyplot as plt


tickers = ('AMZN', 'NVDA', 'TGT', 'AAPL', 
           'WMT', 'GOOG', 'META', 'MSFT', 
           'NFLX', 'TSLA', 'BRK-B', 'JPM', 
           'DIS', 'GS')

start_date = '2023-01-01'
end_date = '2024-11-30'
interval = '1d'

df = yf.download(tickers, start = start_date, end = end_date, interval = interval)

adj_close_price = np.transpose(np.array(df['Adj Close']))

AMZN = np.array(df['Adj Close']['AMZN'])
NVDA = np.array(df['Adj Close']['NVDA'])
TGT = np.array(df['Adj Close']['TGT'])
AAPL = np.array(df['Adj Close']['AAPL'])
WMT = np.array(df['Adj Close']['WMT'])
GOOG = np.array(df['Adj Close']['GOOG'])
META = np.array(df['Adj Close']['META'])
MSFT = np.array(df['Adj Close']['MSFT'])
NFLX = np.array(df['Adj Close']['NFLX'])
TSLA = np.array(df['Adj Close']['TSLA'])
BRK-B = np.array(df['Adj Close']['BRK-B'])
JPM = np.array(df['Adj Close']['JPM'])
DIS = np.array(df['Adj Close']['DIS'])
GS = np.array(df['Adj Close']['GS'])

print(f' tickers: {tickers}')

plt.figure(figsize = (12,6))
plt.plot(np.transpose(adj_close_price))
plt.grid()
plt.legend(tickers, loc = 'best')
plt.show()