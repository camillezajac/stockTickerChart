import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt

tickers_list = ['^GSPC', '^DJI', '^IXIC', '^RUT', '^FTSE', '^N225', 'BTC-USD']
data = yf.download(tickers_list,'2020-1-1')['Adj Close']
print(data.head())

currency_list = ['BTC-USD', '^CMC200', 'EURUSD=X', 'GBPUSD=X', 'JPY=X', 'SI=F', 'GC=F']
data = yf.download(currency_list,'2020-1-1')['Adj Close']
print(data.head())

benchmark_list = ['^VIX', '^TNX', 'CL=F']
data = yf.download(benchmark_list,'2020-1-1')['Adj Close']
print(data.head())

indicator_list = ['^VIX', '^GSPC', 'BTC-USD']
data = yf.download(indicator_list,'2020-1-1')['Adj Close']
print(data.head())

chart = yf.download(tickers_list,'2000-01-01','2021-01-05')
chart['Adj Close'].plot()
chart = yf.download(currency_list,'2000-01-01','2021-01-05')
chart['Adj Close'].plot()
chart = yf.download(benchmark_list,'2000-01-01','2021-01-05')
chart['Adj Close'].plot()
chart = yf.download(indicator_list,'2000-01-01','2021-01-05')
chart['Adj Close'].plot()
plt.show()