import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt

def ema(data, l):
    ema = data["Close"].ewm(span=l, adjust=False).mean()
    data[f"ema{l}"] = ema
    return data

ticker = "AAPL"

try:
    data = pd.read_excel(f"data{ticker}.xlsx")
except:
    data = yf.download(ticker, start="2020-1-1", end="2024-1-1", interval="1d", multi_level_index=False)

data = ema(data, 200)
data = ema(data, 20)
data = ema(data, 50)


plt.figure()
plt.plot(data["Close"], label="price")
plt.plot(data["ema200"], label="ema200")
plt.plot(data["ema20"], label="ema20")
plt.plot(data["ema50"], label="ema50")
plt.title(f"{ticker} Price")
plt.xlabel("Date")
plt.ylabel("Price")
plt.grid()
plt.legend()
plt.show()

data.to_excel(f"data{ticker}.xlsx")

