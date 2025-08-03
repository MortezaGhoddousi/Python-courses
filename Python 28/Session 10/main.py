import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

ticker = "MSFT"
btc_data = yf.download(ticker, start="2020-01-01", end="2025-01-01", interval="1d")

def sma(df: pd.DataFrame, l: int) -> pd.DataFrame:
    # df[(f"sma{l}", "BTC-USD")] = np.nan  # create multi-index column
    # close = df["Close"]["BTC-USD"]       # this is a Series now
    
    # for i in range(len(close)):
    #     if i < l:
    #         df[(f"sma{l}", "BTC-USD")].iloc[i] = close.iloc[i]
    #     else:
    #         df[(f"sma{l}", "BTC-USD")].iloc[i] = np.average(close.iloc[i-l:i])
    df[(f"sma{l}", ticker)] = df["Close"][ticker].rolling(window=l, min_periods=1).mean()
    return df

btc_data = sma(btc_data, 20)
btc_data = sma(btc_data, 50)
btc_data = sma(btc_data, 200)

# print(btc_data.tail())

# for i in range(btc_data["Close"]["BTC-USD"]):
#     if btc_data["Close"]["BTC-USD"].iloc[i] > btc_data["sma200"]["BTC-USD"].iloc[i]:

# Existing assignments for clarity
sma20 = btc_data[("sma20", ticker)]
sma50 = btc_data[("sma50", ticker)]
sma200 = btc_data[("sma200", ticker)]
close = btc_data[("Close", ticker)]

# Detect crosses and condition
sma20_prev = sma20.shift(1)
sma50_prev = sma50.shift(1)
cross_up = (sma20_prev < sma50_prev) & (sma20 >= sma50)
condition_2 = sma200 < close
longSignal = cross_up & condition_2

sma20_prev = sma20.shift(1)
sma50_prev = sma50.shift(1)
cross_up = (sma20_prev > sma50_prev) & (sma20 <= sma50)
condition_2 = sma200 > close
shortSignal = cross_up & condition_2

plt.figure(figsize=(12,8))
plt.plot(btc_data.index, close, label=f"B{ticker} Close", lw=3.5, alpha=0.5)
plt.plot(btc_data.index, sma20, label="SMA 20", lw=2)
plt.plot(btc_data.index, sma50, label="SMA 50", lw=2)
plt.plot(btc_data.index, sma200, label="SMA 200", lw=2)

# Add scatter of signal points on Close price
plt.scatter(btc_data.index[longSignal], close[longSignal], color='green', s=50, label="SMA20 crosses above SMA50 & SMA200 > Close")
plt.scatter(btc_data.index[shortSignal], close[shortSignal], color='red', s=50, label="SMA20 crosses above SMA50 & SMA200 > Close")

plt.xlabel("Time")
plt.ylabel("Price")
plt.title(f"{ticker} Close Price with SMA Cross Signals")
plt.legend()

plt.tight_layout()
plt.show()