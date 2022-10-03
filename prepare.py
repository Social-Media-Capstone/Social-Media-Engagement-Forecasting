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
    '''
    This funciton takes in messy tiktok data and return the cleaned version
    '''
    #df.drop(columns = 'Unnamed: 0', inplace = True)
    df.rename(columns = {'commentCount':'comments', 'diggCount':'likes',
                     'playCount':'views', 'shareCount':'shares', 'time':'epoch',
                    'followerCount': 'total_followers',
                    'heartCount':'total_likes',
                    'videoCount': 'total_videos'}, inplace=True)
    df['date'] = (pd.to_datetime(df['epoch'], unit='s')
                     .dt.tz_localize('utc')
                     .dt.tz_convert('US/Central'))
    df['date'] = df['date'].astype(str).str.slice(0,10)
    # convert date
    df.date = pd.to_datetime(df.date)
    
    df.drop(columns = 'epoch', inplace = True)
    # locate duration = 0 columns
    indexname = df[df.duration ==0].index
    # drop rows with duration = 0
    df.drop(indexname, inplace=True)
    
    # df.set_index('date', inplace=True)
    # df.sort_index()
    df['category'].replace({
        'fashion': 'Fashion',
        'fitness & lifestyle': 'Fitness & Lifestyle',
        'food': 'Food',
        'humor': 'Humor',
        'political': 'Political'}, inplace=True)
    # create conditions
    conditions = [(df['duration']<=15),
              (df['duration']>15)&(df['duration']<=60),
              (df['duration']>60)&(df['duration']<=180), 
              (df['duration']>180)]
    values = ['Short: 0-15s', 'Medium: 15-60s', 'Long: 1-3mins', 'Extra-long: >3mins']
    # create length column using conditions
    df['length'] = np.select(conditions, values)

    return df

def prep_tiktok2(df):
    '''
    This funciton takes in messy tiktok data and return the cleaned version
    '''
    df.drop(columns = 'Unnamed: 0', inplace = True)
#     df.rename(columns = {'commentCount':'comments', 'diggCount':'likes',
#                      'playCount':'views', 'shareCount':'shares', 'time':'epoch',
#                     'followerCount': 'total_followers',
#                     'heartCount':'total_likes',
#                     'videoCount': 'total_videos'}, inplace=True)
#     df['date'] = (pd.to_datetime(df['epoch'], unit='s')
#                      .dt.tz_localize('utc')
#                      .dt.tz_convert('US/Central'))
    df['date'] = df['date'].astype(str)
    df['date'] = df['date'].str.slice(0,10)
    df.date = pd.to_datetime(df.date)
    #df.drop(columns = 'epoch', inplace = True)
    # locate duration = 0 columns
    indexname = df[df.duration ==0].index
    # drop rows with duration = 0
    df.drop(indexname, inplace=True)
    # convert date
    df.date = pd.to_datetime(df.date)
    # df.set_index('date', inplace=True)
    # df.sort_index()
    df['category'].replace({
        'fashion': 'Fashion',
        'fitness & lifestyle': 'Fitness & Lifestyle',
        'food': 'Food',
        'humor': 'Humor',
        'political': 'Political'}, inplace=True)
    # create conditions
    conditions = [(df['duration']<=15),
              (df['duration']>15)&(df['duration']<=60),
              (df['duration']>60)&(df['duration']<=180), 
              (df['duration']>180)]
    values = ['Short', 'Medium', 'Long', 'Extra-long']
    # create length column using conditions
    df['length'] = np.select(conditions, values)

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
    # convert datetime
    youtube['pub_date']=pd.to_datetime(youtube['pub_date'], errors='coerce')
    # drop nulls after date conversion
    youtube.dropna(inplace = True)
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
    youtube['length(second)'] = 3600*youtube.hour + 60*youtube.minute + youtube.second
    
    return youtube
    
def prep_ytshort(youtube):
    youtube.drop(columns = ['publishedTime', 'Unnamed: 2', 'date_ref'], inplace=True)
    # drop non-number viewCount rows
    indexname = youtube[youtube.viewCount.str.contains('[A-Za-z]')].index
    # drop index with letter as viewCount
    youtube.drop(indexname, inplace=True)
    # replace ',' in viewCount
    youtube.viewCount = youtube.viewCount.str.replace(',','')
    # change viewcount to int
    youtube.viewCount = youtube.viewCount.astype(int)
    # convert datetime
    youtube['pub_date']=pd.to_datetime(youtube['pub_date'], errors='coerce')
    # drop nulls after date conversion
    youtube.dropna(inplace = True)
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
    youtube['length(second)'] = 3600*youtube.hour + 60*youtube.minute + youtube.second
    youtube = youtube[youtube['length(second)']<=200]
    conditions = [(youtube['length(second)']<=15),
              (youtube['length(second)']>15)&(youtube['length(second)']<=60),
              (youtube['length(second)']>60)&(youtube['length(second)']<=180), 
              (youtube['length(second)']>180)]
    values = ['Short: 0-15s', 'Medium: 15-60s', 'Long: 1-3mins', 'Extra-long: >3mins']
    # create length column using conditions
    youtube['length'] = np.select(conditions, values)
    
    return youtube
