#!/usr/bin/env python
# coding: utf-8

# In[1]:


# personal imports
import prepare
import explore

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
from sklearn.ensemble import RandomForestRegressor

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

import re
import unicodedata
import pandas as pd
import nltk
import numpy as np

from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer

import matplotlib.pyplot as plt
import seaborn as sns

from wordcloud import WordCloud


# In[2]:


tik = pd.read_csv('tiktok_final_data.csv')


# In[3]:


tik.drop(columns = ['Unnamed: 0', 'total_likes', 'total_videos', 'duration'], inplace = True)


# In[4]:


tik['engagement'] = (tik.comments+tik.likes+tik.views+tik.shares)/tik.total_followers


# In[5]:


tik.drop(columns = ['comments', 'likes', 'views', 'shares', 'hashtag', 'date'], inplace = True)


# In[6]:


#separate data based on category, into their own dataframe
tik_fas = tik[tik.category == 'fashion']
tik_fit = tik[tik.category == 'fitness & lifestyle']
tik_foo = tik[tik.category == 'food']
tik_pol = tik[tik.category == 'political']
tik_hum = tik[tik.category == 'humor']


# In[7]:


#drop category as a column
tik_fas.drop(columns = ['category'], inplace = True)
tik_fit.drop(columns = ['category'], inplace = True)
tik_foo.drop(columns = ['category'], inplace = True)
tik_pol.drop(columns = ['category'], inplace = True)
tik_hum.drop(columns = ['category'], inplace = True)


# In[8]:


def basic_clean(t):
    article = t.lower()
    article1 = unicodedata.normalize('NFKD', article).encode('ascii', 'ignore').decode('utf-8', 'ignore')
    article2 = re.sub(r"[^a-z\s']", '', article1)
    return article2


# In[9]:


#set description as a string to prep for basic clean
tik_fas.description = tik_fas.description.astype('str')
tik_fit.description = tik_fit.description.astype('str')
tik_foo.description = tik_foo.description.astype('str')
tik_pol.description = tik_pol.description.astype('str')
tik_hum.description = tik_hum.description.astype('str')


# In[10]:


#apply basic clean
tik_fas.description = tik_fas.description.apply(basic_clean)
tik_fit.description = tik_fit.description.apply(basic_clean)
tik_foo.description = tik_foo.description.apply(basic_clean)
tik_pol.description = tik_pol.description.apply(basic_clean)
tik_hum.description = tik_hum.description.apply(basic_clean)


# In[11]:


#TfidVectorizer for X and y
def tfidvect(df):
    tfidf = TfidfVectorizer()
    x = tfidf.fit_transform(df.description)
    y = df.engagement
    return x, y, tfidf


# In[12]:


def data_split_for_modeling(x_data, y_data): #data split
    ''' splitting for x & y train,validate,test'''
    x_train_validate, x_test, y_train_validate, y_test = train_test_split(x_data, y_data, 
                                                                          #stratify = y_data, 
                                                                          test_size=.25, random_state=123) #spicify random state so we get the same split everytime
    
    x_train, x_validate, y_train, y_validate = train_test_split(x_train_validate, y_train_validate, 
                                                                #stratify = y_train_validate, 
                                                                test_size=.3, 
                                                                random_state=123) #spicify random state so we get the same split everytime
    
    return x_train, y_train, x_validate, y_validate, x_test, y_test


# In[13]:


def rmse_median(df):
    df['med'] = df.engagement.median()
    rmse_baseline = mean_squared_error(df.engagement, df.med)**(1/2)
    return rmse_baseline


# In[14]:


# x_train = x_train.toarray()
# x_val = x_val.toarray()
# x_test = x_test.toarray()


# In[15]:


def lasolars(x_train, y_train, x_val, y_val):    
    # create the model object
    lars = LassoLars(alpha=0.5)

    # fit the model ONLY to our training data.  

    lars.fit(x_train, y_train)

    # predict train
    y_train_lars = lars.predict(x_train)

    # evaluate: rmse
    rmse_train = mean_squared_error(y_train, y_train_lars)**(1/2)

    # predict validate
    y_val_lars = lars.predict(x_val)

    # evaluate: rmse
    rmse_validate = mean_squared_error(y_val, y_val_lars)**(1/2)

    print("RMSE for OLS using Lars\nTraining/In-Sample: ", rmse_train, 
          "\nValidation/Out-of-Sample: ", rmse_validate)
    return rmse_train, rmse_validate


# In[16]:


def glm_p1(x_train, y_train, x_val, y_val):    
    # create the model object
    glm = TweedieRegressor(power=1, alpha=0.05)

    # fit the model ONLY to our training data.  

    glm.fit(x_train, y_train)

    # predict train
    y_train_glm = glm.predict(x_train)

    # evaluate: rmse
    rmse_train = mean_squared_error(y_train, y_train_glm)**(1/2)

    # predict validate
    y_val_glm = glm.predict(x_val)

    # evaluate: rmse
    rmse_validate = mean_squared_error(y_val, y_val_glm)**(1/2)

    print("RMSE for OLS using GLM\nTraining/In-Sample: ", rmse_train, 
          "\nValidation/Out-of-Sample: ", rmse_validate)
    return rmse_train, rmse_validate


# In[17]:


def glm_p2(x_train, y_train, x_val, y_val):    
    # create the model object
    glm = TweedieRegressor(power=1, alpha=0.05)

    # fit the model ONLY to our training data.  

    glm.fit(x_train, y_train)

    # predict train
    y_train_glm = glm.predict(x_train)

    # evaluate: rmse
    rmse_train = mean_squared_error(y_train, y_train_glm)**(1/2)

    # predict validate
    y_val_glm = glm.predict(x_val)

    # evaluate: rmse
    rmse_validate = mean_squared_error(y_val, y_val_glm)**(1/2)

    print("RMSE for OLS using GLM\nTraining/In-Sample: ", rmse_train, 
          "\nValidation/Out-of-Sample: ", rmse_validate)
    return rmse_train, rmse_validate, glm


# In[18]:


def linreg(x_train, y_train, x_val, y_val): 
    # create the model object
    lm = LinearRegression(normalize=True, positive=True)

    # fit the model ONLY to our training data.  

    lm.fit(x_train, y_train)

    # predict train
    y_train_lr = lm.predict(x_train)

    # evaluate: rmse
    rmse_train = mean_squared_error(y_train, y_train_lr)**(1/2)

    # predict validate
    y_val_lr = lm.predict(x_val)

    # evaluate: rmse
    rmse_validate = mean_squared_error(y_val, y_val_lr)**(1/2)

    print("RMSE for OLS using LinearRegression\nTraining/In-Sample: ", rmse_train, 
          "\nValidation/Out-of-Sample: ", rmse_validate)
    return rmse_train, rmse_validate


# In[19]:


def rand_for_reg(x_train, y_train, x_val, y_val): 
    # create the model object
    rgr = RandomForestRegressor(max_depth=11, random_state=123)

    # fit the model ONLY to our training data.  

    rgr.fit(x_train, y_train)

    # predict train
    y_train_rgr = rgr.predict(x_train)

    # evaluate: rmse
    rmse_train = mean_squared_error(y_train, y_train_rgr)**(1/2)

    # predict validate
    y_val_rgr = rgr.predict(x_val)

    # evaluate: rmse
    rmse_validate = mean_squared_error(y_val, y_val_rgr)**(1/2)

    print("RMSE for OLS using RandomForestRegression\nTraining/In-Sample: ", rmse_train, 
          "\nValidation/Out-of-Sample: ", rmse_validate)
    return rmse_train, rmse_validate


# In[20]:


def glm_eng_word_prep(glm, tfidf):
    eng_coef = glm.coef_
    eng_coef = pd.DataFrame(eng_coef)
    eng_coef.rename(columns = {0:'score'}, inplace=True)
    eng_words = tfidf.get_feature_names_out()
    eng_words = pd.DataFrame(eng_words)
    eng_words.rename(columns = {0:'words'}, inplace=True)
    word_eng = pd.concat([eng_words, eng_coef], axis =1)
    word_dic = dict(zip(word_eng.words, word_eng.score))
    return word_dic


# In[ ]:





# In[21]:


# def comb(df):
#     rmse_sum = pd.DataFrame()
#     rmse_train, rmse_val = lasolars(df)
#     rmse_sum = pd.concat([rmse_sum, df])
    
#     rmse_train, rmse_val = glm_p1(df)
#     rmse_sum = pd.concat([rmse_sum, df])
    
#     rmse_train, rmse_val = linreg(df)
#     rmse_sum = pd.concat([rmse_sum, df])
    
#     rmse_train, rmse_val = linreg(df)
#     rmse_sum = pd.concat([rmse_sum, df])
    
    
    
    


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




