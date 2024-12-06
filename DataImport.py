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

amzn = np.array(df['Adj Close']['AMZN'])
nvda = np.array(df['Adj Close']['NVDA'])
tgt = np.array(df['Adj Close']['TGT'])
aapl = np.array(df['Adj Close']['AAPL'])
wmt = np.array(df['Adj Close']['WMT'])
goog = np.array(df['Adj Close']['GOOG'])
meta = np.array(df['Adj Close']['META'])
msft = np.array(df['Adj Close']['MSFT'])
nflx = np.array(df['Adj Close']['NFLX'])
tsla = np.array(df['Adj Close']['TSLA'])
brk = np.array(df['Adj Close']['BRK-B'])
jpm = np.array(df['Adj Close']['JPM'])
dis = np.array(df['Adj Close']['DIS'])
gs = np.array(df['Adj Close']['GS'])

print(f' tickers: {tickers}')

plt.figure(figsize = (12,6))
plt.plot(np.transpose(adj_close_price))
plt.grid()
plt.legend(tickers, loc = 'best')
plt.show()