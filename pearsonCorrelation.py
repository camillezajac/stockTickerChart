import yfinance as yf
import matplotlib.pyplot as plt
import scipy.stats as stats
import datetime

start = datetime.datetime(2000,1,1)
end = datetime.datetime(2020,1,1)

VIX = yf.download("^VIX", start, end, output_format='pandas')
SPY = yf.download("^GSPC", start, end, output_format='pandas')
plt.figure(figsize=(10, 4))
plt.plot(SPY.index, SPY['Adj Close'])
plt.plot(VIX.index, VIX['Adj Close'])
plt.legend(['SPY','VIX'],loc=2)
plt.title('Times Series');
plt.show()

c, p = stats.pearsonr(VIX['Adj Close'], SPY['Adj Close'])
print(f"VIX vs SPY Pearson Correlation: {c}\n")
