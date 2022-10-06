

# Social  Media Engagement Forecasting
By : **[Brad Gauvin](https://github.com/bradgauvin), [Jess Gardin](https://github.com/Jgardin875), [Meredith Wang](https://github.com/m3redithw),  [Saroj Duwal](https://github.com/Saroj6632)**

Date: 09/2022 - present

# Table of Content
- [Project Description](#project_desc)
    - [Business Goal](#business_goal)
    - [Initial Questions](#questions)
    - [Deliverables](#deliverables)
    - [Dependencies](#dependencies)
    - [Data Dictionary](#data)

- [Process](#data)
    - Planning
    - Acquisition
    - Preparation
    - Exploration
    - Modeling
    
- [Conclusion](#conclusion)
    - Key Findings
    - Recommendation
    - Future Development


# Project Description <a name="project_desc"></a>
TikTok, a video sharing social media platform, funded in 2016 has gained tremedous amount of popularity over the past few years.
(EDITING...)

## Business Goal<a name="business_goal"></a>

## Initial Questions<a name="questions"></a>
▪️ What does trending video's duration distribution look like? Is most vidoes on TikTok short (<15?)

▪️ Is the avg. video duration of a category more than the other? If so, which video length drives the highest engagement for each category?

▪️ What's the avg engagement metrics of trending vidoe's in the past two years?

▪️ Where does TikTok stand compared to YouTube and Instagram?

▪️ Is a certian category's engagement significant more than the other?

▪️ Does creator's follower size correlate with engagement?

▪️ Are there certain key words/hashtags that drive engagement?

## Deliverables <a name="deliverables"></a>

- Report Notebook `final_report.ipynb`
- Web app with interactive dashboard
- Slide presentation for technical and non-technical skateholders
- Project white paper for non-technical audience

## Requirements <a name="requirements"></a>

Before you run this notebook, please ensure you have the below packages installed.

* [![python-shield](https://img.shields.io/badge/Python-3-blue?&logo=python&logoColor=white)
    ](https://www.python.org/)
* [![numpy-shield](https://img.shields.io/badge/Numpy-grey?&logo=numpy)
    ](https://numpy.org/)
* [![pandas-shield](https://img.shields.io/badge/Pandas-grey?&logo=pandas)
    ](https://pandas.pydata.org/)
* [![matplotlib-shield](https://img.shields.io/badge/Matplotlib-grey.svg?)
    ](https://matplotlib.org)
* [![seaborn-shield](https://img.shields.io/badge/Seaborn-grey?&logoColor=white)
    ](https://seaborn.pydata.org/)
* [![plotly-shield](https://img.shields.io/badge/Plotly-grey?&logoColor=white)
    ]([https://seaborn.pydata.org/](https://plotly.com/python/))
* [![scipy-shield](https://img.shields.io/badge/SciPy-grey?&logo=scipy&logoColor=white)
    ](https://scipy.org/)
* [![sklearn-shield](https://img.shields.io/badge/_-grey?logo=scikitlearn&logoColor=white&label=scikit-learn)
    ](https://scikit-learn.org/stable/)
* [![prophet-shield](https://img.shields.io/badge/_-grey?logo=Facebookprophet&logoColor=white&label=prophet)
    ](https://scikit-learn.org/stable/)   
* [![nltk-shield](https://img.shields.io/badge/NLTK-grey?&logo=&logoColor=white)
    ](https://textblob.readthedocs.io/en/dev/)
* [![xgboost-shield](https://img.shields.io/badge/XGBoost-grey?&logo=&logoColor=white)
    ](https://xgboost.readthedocs.io/en/stable/)
* [![textblob-shield](https://img.shields.io/badge/TextBlob-grey?&logo=&logoColor=white)
    ](https://textblob.readthedocs.io/en/dev/)


Dependencies can be installed quickly with just a few lines of code.

```
%pip install notebook
%pip install numpy
%pip install pandas
%pip install matplotlib
%pip install seaborn
%pip install scipy
%pip install sklearn
%pip install nltk
%pip install xgboost
%pip install youtube-search-python
```


## Data Dictionary<a name="data"></a>
**Variable** |    **Value**    | **Meaning**
---|---|---
<span style="background-color: #ffe0bd">*commentCount*</span> | int | The number of comments on a video
<span style="background-color: #ffe0bd">*diggCount*</span> | int | The number of likes on a video
<span style="background-color: #ffe0bd">*playCount*</span> | int | The number of views on a video
<span style="background-color: #ffe0bd">*shareCount*</span> | int | The number of shares on a video
<span style="background-color: #ffe0bd">*followerCount*</span> | int | The number of followers a creator has
<span style="background-color: #ffe0bd">*heartCount*</span> | int | The total number of likes a creator has gotten for that account
<span style="background-color: #ffe0bd">*videoCount*</span> | int | The number of videos a creator has posted as public
<span style="background-color: #ffe0bd">*description*</span>| string object | The description of videos
<span style="background-color: #ffe0bd">*time*</span> | datetime object | The time a video is posted, formatted in epoch time
<span style="background-color: #ffe0bd">*hashtag*</span> | string object | The hashtag the caption of the video contains
<span style="background-color: #ffe0bd">*category*</span> | string obejct | The category the video belongs to







# Process <a name="process"></a>
## Acquisition

- "env.py" has API key credentials to access the data from tiktok API, youtube API and Instagram API
- Data acquisition contains 3 platforms: Tiktok, Youtube, Instagram; 5 categories: Fahion & Beauty, Humor, Political Contents, Food, Fitness & Lifestyle
- Tiktok data is acquired through TikAPI, using search hashtag and search top influencers approach, detailed steps please reference acquire editing
- Youtube data is acquired through functions inside youtube-search-python 1.6.6 (built-in Python library), detailed steps please reference acquire editing
- Instagram data is acquired and extracted through an existing dataset. We used automated data extraction to go through 1.5 million json files and condensed useful information into a dataframe.

## Preparation

## Exploration


![roughviz](https://user-images.githubusercontent.com/105242871/192079926-96185ad2-505d-4181-8556-ab94c867f2b5.gif)



## Modeling
- Last Observed Value (Baseline)
- Moving Average: The future will look, on average, like recent history.
- Holt's Linear Trend
- Previous Cycle
- Facebook Prophet
- ARIMA
- Long Short Term Memory Neural Network


# Conclusion
## Key Findings




## Next Steps

Despite the overall effectiveness of our best-performing model, there is always room for improvement and optimization.
If given more time to pursue better results, we could perform further investigation within exploration by:

1. Estimating each readme's school reading level. Not only would this be interesting as an anecdote, if proven useful, it could be imputed as a new feature to boost the accuracy of our model.

2. Handling ReadMes in a foreign language in a more succinct way. This could be handled more effectively by using a translator to convert all ReadMes into English for potentially better modeling accuracy. 

