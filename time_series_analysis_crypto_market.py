#%%
import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import cpi
from statsmodels.tsa.stattools import adfuller, acf, pacf
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from statsmodels.tsa.statespace.sarimax import SARIMAX
import pmdarima as pm
from sklearn.metrics import mean_squared_error
from math import sqrt

#%%
# --------------------------- Select Data via API ---------------------------
btc = yf.Ticker("BTC-GBP")
eth = yf.Ticker("ETH-GBP")

btc.info

#%%
eth.info

#%%
data_btc = yf.download(["BTC-GBP", "^DJI"], start="2012-01-01", end="2026-01-01")
data_eth = yf.download(["ETH-GBP", "^DJI"], start="2016-01-01", end="2026-01-01")

# %%
data_btc

#%%
data_eth

#%% 
# --------------------------- Preview Data Graphically ---------------------------
data_btc.Close["BTC-GBP"].plot(title="BTC/GBP");

#%%
data_eth.Close["ETH-GBP"].plot(title="ETH/GBP");

#%%
# --------------------------- Adjust Data for Inflation ---------------------------
cpi.update()
close_btc = data_btc.copy()
close_btc.rename(columns={"^DJI" : "DJI"}, inplace=True)
close_btc

#%%
cpi.update()
close_eth = data_eth.Close.copy()
close_eth.rename(columns={"^DJI" : "DJI"}, inplace=True)
close_eth

#%%
date_range_btc = pd.date_range(close_btc.index[0] - pd.DateOffset(days=3),
                               close_btc.index[-1], freq="MS")
date_range_btc

#%%
date_range_eth = pd.date_range(close_eth.index[0], pd.DateOffset(days=3),
                               close_eth.index[-1], freq="MS")
date_range_eth

#%%
cpi_mon_btc = pd.DataFrame(index=date_range_btc)  # check if this is needed
cpi_mon_eth = pd.DataFrame(index=date_range_eth) # check if this is needed

