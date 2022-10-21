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
import numpy as np


#define the ticker symbol
tickerSymbol = 'AAPL'
# tickerSymbol = input("Enter a ticker: ")
# tickerSymbol = tickerSymbol.upper()

#startDate = input("Enter a start date (YYYY-MM-DD): ")
startDate = '2019-01-01'
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


#### Calculate the metrics RMSE and MAPE ####
def calculate_rmse(y_true, y_pred):
    """
    Calculate the Root Mean Squared Error (RMSE)  
    """
    rmse = np.sqrt(np.mean((y_true-y_pred)**2))                   
    return rmse

def calculate_mape(y_true, y_pred): 
    """
    Calculate the Mean Absolute Percentage Error (MAPE) %
    """
    y_pred, y_true = np.array(y_pred), np.array(y_true)    
    mape = np.mean(np.abs((y_true-y_pred) / y_true))*100    
    return mape

rmse = calculate_rmse(tickerDf.Open, tickerDf.Close)
mape = calculate_mape(tickerDf.Open, tickerDf.Close)



# rmse = calculate_rmse(priceData, final_list)
# mape = calculate_mape(tickerDf.Open, tickerDf.Close)



## Simple Moving Average

# create 20 days simple moving average column
tickerDf['20_SMA'] = tickerDf['Open'].rolling(window = 20, min_periods = 1).mean()
# create 50 days simple moving average column
tickerDf['50_SMA'] = tickerDf['Open'].rolling(window = 50, min_periods = 1).mean()


tickerDf['Signal'] = 0.0
tickerDf['Signal'] = np.where(tickerDf['20_SMA'] > tickerDf['50_SMA'], 1.0, 0.0)
tickerDf['Position'] = tickerDf['Signal'].diff()


plt.figure(figsize = (20,10))
# plot close price, short-term and long-term moving averages 
tickerDf['Open'].plot(color = 'k', label= 'Open Price') 
tickerDf['20_SMA'].plot(color = 'b',label = '20-day SMA') 
tickerDf['50_SMA'].plot(color = 'g', label = '50-day SMA')
# plot ‘buy’ signals
plt.plot(tickerDf[tickerDf['Position'] == 1].index, 
         tickerDf['20_SMA'][tickerDf['Position'] == 1], 
         '^', markersize = 15, color = 'g', label = 'buy')
# plot ‘sell’ signals
plt.plot(tickerDf[tickerDf['Position'] == -1].index, 
         tickerDf['20_SMA'][tickerDf['Position'] == -1], 
         'v', markersize = 15, color = 'r', label = 'sell')
plt.ylabel('Price in USD', fontsize = 15 )
plt.xlabel('Date', fontsize = 15 )
plt.title('AAPL', fontsize = 20)
plt.legend()
plt.grid()
plt.show()

sma_rmse = calculate_rmse(tickerDf['Open'], tickerDf['50_SMA'])
print(sma_rmse)
sma_mape = calculate_mape(tickerDf['Open'], tickerDf['20_SMA'])
print(sma_mape)



## Exponential Moving Average

# Create 20 days exponential moving average column
tickerDf['20_EMA'] = tickerDf['Open'].ewm(span = 20, adjust = False).mean()
# Create 50 days exponential moving average column
tickerDf['50_EMA'] = tickerDf['Open'].ewm(span = 50, adjust = False).mean()
# create a new column 'Signal' such that if 20-day EMA is greater   # than 50-day EMA then set Signal as 1 else 0
  
tickerDf['Signal_EMA'] = 0.0  
tickerDf['Signal_EMA'] = np.where(tickerDf['20_EMA'] > tickerDf['50_EMA'], 1.0, 0.0)
# create a new column 'Position' which is a day-to-day difference of # the 'Signal' column
tickerDf['Position_EMA'] = tickerDf['Signal_EMA'].diff()
plt.figure(figsize = (20,10))
# plot close price, short-term and long-term moving averages 
tickerDf['Open'].plot(color = 'k', lw = 1, label = 'Open Price')  
tickerDf['20_EMA'].plot(color = 'b', lw = 1, label = '20-day EMA') 
tickerDf['50_EMA'].plot(color = 'g', lw = 1, label = '50-day EMA')
# plot ‘buy’ and 'sell' signals
plt.plot(tickerDf[tickerDf['Position_EMA'] == 1].index, 
         tickerDf['20_EMA'][tickerDf['Position'] == 1], 
         '^', markersize = 15, color = 'g', label = 'buy')
plt.plot(tickerDf[tickerDf['Position'] == -1].index, 
         tickerDf['20_EMA'][tickerDf['Position'] == -1], 
         'v', markersize = 15, color = 'r', label = 'sell')
plt.ylabel('Price in USD', fontsize = 15 )
plt.xlabel('Date', fontsize = 15 )
plt.title('AAPL - EMA Crossover', fontsize = 20)
plt.legend()
plt.grid()
plt.show()

sma_rmse = calculate_rmse(tickerDf['Open'], tickerDf['50_EMA'])
print(sma_rmse)
sma_mape = calculate_mape(tickerDf['Open'], tickerDf['20_EMA'])
print(sma_mape)











