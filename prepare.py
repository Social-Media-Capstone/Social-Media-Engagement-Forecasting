# import essential libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm
import scipy.stats as stats

# import the datetime module
import datetime

# ignore warnings
import warnings
warnings.filterwarnings('ignore')


def prep_tiktok(df):
    #df.drop(columns = 'Unnamed: 0', inplace = True)
    df.rename(columns = {'commentCount':'comments', 'diggCount':'likes', 'playCount':'played', 'shareCount':'shared', 'time':'epoch'}, inplace=True)
    df['date'] = (pd.to_datetime(df['epoch'], unit='s')
                     .dt.tz_localize('utc')
                     .dt.tz_convert('US/Central'))
    df.drop(columns = 'epoch', inplace = True)
    df.date = pd.to_datetime(df.date)
    df.set_index('date', inplace=True)
    df.sort_index()
    return df


def prep_youtube_num(df):
    df.drop(columns = ['publishedTime', 'Multiplier', 'date_ref', 'title', 'duration'], inplace = True)
    df.rename(columns = {'Pub_date':'date', 'viewCount':'views'}, inplace=True)
    df.date = pd.to_datetime(df.date, utc = True)
    df.set_index('date', inplace=True)
    df.sort_index()
    df = df[df.views != 'No']
    df.views = df.views.astype('int')
    df = pd.DataFrame(df)
    return df

def change_time(string):
    '''
    This function identify the timeformat with extra :00 at the end and delete them
    '''
    if len(string)>5:
        if string.endswith(':00'):
            string = string.replace(':00', '')
    return string

def add_zero(string):
    '''
    This function add 00: to the time strings
    '''
    if len(string)<=5:
        string = '00:' + string
    return string

def prep_youtube(youtube):
    '''
    This function takes in the messy youtube dataframe and return the clean version
    '''

    # drop useless columns
    youtube.drop(columns = ['publishedTime', 'Unnamed: 2', 'date_ref'], inplace=True)
    # drop non-number viewCount rows
    indexname = youtube[youtube.viewCount.str.contains('[A-Za-z]')].index
    # drop index with letter as viewCount
    youtube.drop(indexname, inplace=True)
    # replace ',' in viewCount
    youtube.viewCount = youtube.viewCount.str.replace(',','')
    # change viewcount to int
    youtube.viewCount = youtube.viewCount.astype(int)
    # convert duration to length
    youtube.duration = youtube.duration.apply(change_time)
    # add zero to have a universal length
    youtube.duration = youtube.duration.apply(add_zero)
    youtube.duration = youtube.duration.apply(add_zero)
    # split time into hour, minute, second
    youtube['hour'] = youtube['duration'].str.slice(0,2)
    youtube['minute'] =  youtube['duration'].str.slice(3,5)
    youtube['second'] =  youtube['duration'].str.slice(6,8)
    # convert datatype
    youtube.hour = youtube.hour.astype(int)
    youtube.minute = youtube.minute.astype(int)
    youtube.second = youtube.second.astype(int)
    # calculate length
    youtube['length'] = 3600*youtube.hour + 60*youtube.minute + youtube.second\
    
    return youtube
