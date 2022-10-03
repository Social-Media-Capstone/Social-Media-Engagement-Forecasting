#!/usr/bin/env python
# coding: utf-8

# In[2]:


# personal imports
import prepare

# typical imports
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

# modeling methods
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.linear_model import LinearRegression, LassoLars, TweedieRegressor
from sklearn.preprocessing import PolynomialFeatures

# working with dates
from datetime import datetime
import time

# to evaluated performance using rmse
from sklearn.metrics import mean_squared_error
from math import sqrt 

# for tsa 
import statsmodels.api as sm

# holt's linear trend model. 
from statsmodels.tsa.api import Holt

#clean look
import warnings
warnings.filterwarnings("ignore")


# In[3]:


def visual(df):
    cat_col = df.columns
    plt.figure(figsize=(16, 16))
    for i, col in enumerate(cat_col):
        plot_number = i + 1
        l= len(cat_col)
        plt.subplot(9,1,plot_number)
        sns.lineplot(x = df.index, y = df[col])
        plt.suptitle('----------------------------------------')
plt.tight_layout()


# In[ ]:




