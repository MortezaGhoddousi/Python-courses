import numpy as np
from Maths import Mathematical

print(np.pi)
print(np.cos(np.pi))

m = Mathematical(4, 7)
print(m.pi)

print(m.area())
print(m.primeter())

class extended_mathematical(Mathematical):
    def volume(self, h):
        return self.x*self.y*h

m1 = extended_mathematical(4, 7)
print(m1.pi)

print(m1.area())
print(m1.primeter())
print(m1.volume(3))

import pandas as pd

# df = pd.read_excel("data.xlsx")
# print(df)
# print(df['firstName'][0])

# df['isMale'] = [True, True, True, True]

# df.to_excel('data.xlsx')

# print(df)

import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

ticker = 'MSFT'  

try:
    data = pd.read_excel(f'{ticker}.xlsx')
except FileNotFoundError:
    data = yf.download(ticker, start="2023-01-01", end="2025-01-01", interval="1d", multi_level_index=False)
    data.to_excel(f'{ticker}.xlsx')

data = data.reset_index()

def sma_indicator(df, l):
    close = df['Close']
    sma = []
    for i, v in enumerate(close):
        if i < l:
            if i == 0:
                sma.append(v)
            else:
                sma.append(np.average(close[:i]))
        else:
            sma.append(np.average(close[i-l+1:i+1]))
    df[f'sma{l}'] = sma
    return df

data = sma_indicator(data, 20)
data = sma_indicator(data, 50)
data = sma_indicator(data, 200)

sma20Shifted = data['sma20'].shift(-1)
sma50Shifted = data['sma50'].shift(-1)

buy_signal = []
sell_signal = []

for i, v in enumerate(data['Close']):
    if v >= data['sma200'].iloc[i]:
        if sma20Shifted.iloc[i] >= sma50Shifted.iloc[i] and data['sma20'].iloc[i] < data['sma50'].iloc[i]:
            buy_signal.append(1)
        else:
            buy_signal.append(np.nan)
    else:
        buy_signal.append(np.nan)

for i, v in enumerate(data['Close']):
    if v < data['sma200'].iloc[i]:
        if sma20Shifted.iloc[i] <= sma50Shifted.iloc[i] and data['sma20'].iloc[i] > data['sma50'].iloc[i]:
            sell_signal.append(1)
        else:
            sell_signal.append(np.nan)
    else:
        sell_signal.append(np.nan)

       

data['buy_signal'] = buy_signal
data['sell_signal'] = sell_signal

print(data.head())

# Plotting
plt.figure(figsize=(12, 7))
plt.plot(data['Date'], data['Close'], label='Close Price')
plt.plot(data['Date'], data['sma20'], label='SMA 20')
plt.plot(data['Date'], data['sma50'], label='SMA 50')
plt.plot(data['Date'], data['sma200'], label='SMA 200')

# Plot buy signals
buy_signals = data[data['buy_signal'] == 1]
plt.scatter(buy_signals['Date'], buy_signals['Close'], marker='^', color='green', s=100, label='Buy Signal')

sell_signals = data[data['sell_signal'] == 1]
plt.scatter(sell_signals['Date'], sell_signals['Close'], marker='^', color='red', s=100, label='Sell Signal')

plt.xlabel('Time')
plt.ylabel('Price')
plt.title(f'{ticker} Price with Buy Signals')
plt.grid(True)
plt.legend()
plt.show()








        