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
