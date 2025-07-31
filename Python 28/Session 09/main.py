import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

btc_data = yf.download("BTC-USD", start="2020-01-01", end="2021-01-01", interval="1d")

def sma(df:pd.DataFrame, l:int) -> pd.DataFrame:
    for i, cp in enumerate(df["Close"]['BTC-USD']):
        if i < l:
            df['sma'+str(l)]['BTC-USD'][i] = df["Close"]['BTC-USD'][i]
        else:
            # calculate moving average for specific length
            pass
        

sma(btc_data, 20)

print(btc_data.head())

plt.figure()
plt.plot(btc_data['Close']['BTC-USD'].index, btc_data['Close']['BTC-USD'], label="BTC-USD", lw=3.5, alpha=0.5)
plt.xlabel("Time")
plt.ylabel("Price")
plt.title("BTC-USD Close Price")
plt.legend()
plt.show()