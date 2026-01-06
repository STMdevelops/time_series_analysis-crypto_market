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
close1 = data_btc.copy()
close1.rename(columns={"^DJI" : "DJI"}, inplace=True)
close1

#%%
cpi.update()
close2 = data_eth.Close.copy()
close2.rename(columns={"^DJI" : "DJI"}, inplace=True)
close2