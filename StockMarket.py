#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 22:00:34 2022

@author: joelsommerfeld
"""

import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime#, timedelta
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf


#define the ticker symbol
tickerSymbol = 'AAPL'
# tickerSymbol = input("Enter a ticker: ")
# tickerSymbol = tickerSymbol.upper()

#startDate = input("Enter a start date (YYYY-MM-DD): ")
startDate = '2010-01-01'
#endDate = input("Enter an end date (YYYY-MM-DD): ")
endDate = '2019-10-30'
#interval = input("Select an interval (day/month/year): ")

#get data on this ticker
tickerData = yf.Ticker(tickerSymbol)

#get the historical prices for this ticker
tickerDf = tickerData.history(interval = '1d', start = startDate, end = endDate)

priceData = tickerDf.Open

priceData = priceData.asfreq(pd.infer_freq(priceData.index))

# plt.figure(figsize=(10,4))
fig, ax = plt.subplots(3,1,figsize=(12,7))
fig.suptitle("Stock Price on Open: %s"%tickerSymbol, fontsize=20)
fig.tight_layout(pad=2)

# plt.plot(priceData, ax = ax[0])
ax[0].plot(priceData)
# for year in range(priceData.index[0].year, priceData.index[-1].year+1):
#    plt.axvline(datetime(year,1,1), color='k', linestyle='--', alpha=0.2)
#plt.title("%s Price Data"%tickerSymbol, fontsize=20)

# Subplot of the autocorrelations
plot_acf(tickerDf.Open, lags = 50, ax = ax[1])
plot_pacf(tickerDf.Open, lags = 50, method = "ywm", ax = ax[2])

plt.show()


# Looking at volume
volume = tickerDf.Volume 

# Subplot of the autocorrelations
fig, ax = plt.subplots(3,1,figsize=(12,7))
fig.suptitle("Stock Volume: %s"%tickerSymbol, fontsize=20)
fig.tight_layout(pad=2)


ax[0].plot(tickerDf.Volume)
plot_acf(tickerDf.Volume, lags = 50, ax = ax[1])
plot_pacf(tickerDf.Volume, lags = 50, method = "ywm", ax = ax[2])
plt.show()
