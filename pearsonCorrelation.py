import yfinance as yf
import scipy.stats as stats
import datetime

start = datetime.datetime(2000,1,1)
end = datetime.datetime(2020,1,1)

VIX = yf.download("^VIX", start, end, output_format='pandas')
SPY = yf.download("^GSPC", start, end, output_format='pandas')

c, p = stats.pearsonr(VIX['Adj Close'], SPY['Adj Close'])
print(f"VIX vs SPY Pearson Correlation: {c}\n")
