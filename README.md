

# Social  Media Engagement Forecasting
By : **[Brad Gauvin](https://github.com/bradgauvin), [Jess Gardin](https://github.com/Jgardin875), [Meredith Wang](https://github.com/m3redithw),  [Saroj Duwal](https://github.com/Saroj6632)**

Date: 09/2022 - present

# Table of Content
- [Project Description](#project_desc)
    - [Business Goal](#business_goal)
    - [Initial Questions](#questions)
    - [Deliverables](#deliverables)
    - [Requirements](#requirements)
    - [Data Dictionary](#data)

- [Process](#process)
    - [Acquisition](#acquisition)
    - [Preparation](#preparation)
    - [Exploration](#exploration)
    - [Modeling](#modeling)
    
- [Conclusion](#conclusion)
    - [Key Findings](#key_findings)
    - [Future Development](#next_steps)


# Project Description <a name="project_desc"></a>
TikTok, a video sharing and relatively new social media platform (funded in 2016), has gained tremendous amount of popularity over the past few years. Understanding their "success metric" and knowing how to attract engagement is extremely important for business and individuals who want to develop their presence on there.

Along with other deliveralbes, a [web APP](https://m3redithw-streamlit-home-4vvfud.streamlitapp.com/) with interactive dashboard is developed as an additional component to the project for both technical and non-technical skate-holders to grasp the key findings.

## Business Goal<a name="business_goal"></a>
We used time series models to forecast engagement over time, along with natural language processing regression models to predict the key words that are likely to generate viral content. E-commerce, retail businesses, influencers, etc. can stratigically utilize ourpredictive model to push out content that would gain the most branded-effect possible with worlwide audience and generate revenue.

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

* [![python-shield](https://img.shields.io/badge/Python-dfaeff?&logo=python&logoColor=white)
    ](https://www.python.org/)
* [![numpy-shield](https://img.shields.io/badge/Numpy-dfaeff?&logo=NumPy)
    ](https://numpy.org/)
* [![pandas-shield](https://img.shields.io/badge/Pandas-dfaeff?&logo=pandas)
    ](https://pandas.pydata.org/)
* [![matplotlib-shield](https://img.shields.io/badge/Matplotlib-dfaeff.svg?)
    ](https://matplotlib.org)
* [![seaborn-shield](https://img.shields.io/badge/Seaborn-dfaeff?&logo=python-seaborn&logoColor=white)
    ](https://seaborn.pydata.org/)
* [![plotly-shield](https://img.shields.io/badge/Plotly-dfaeff?&logo=Plotly&logoColor=white)
    ]([https://seaborn.pydata.org/](https://plotly.com/python/))
* [![scipy-shield](https://img.shields.io/badge/SciPy-dfaeff?&logo=scipy&logoColor=white)
    ](https://scipy.org/)
* [![sklearn-shield](https://img.shields.io/badge/sklearn-dfaeff?logo=scikitlearn&logoColor=white)
    ](https://scikit-learn.org/stable/)
* [![Tensorflow-shield](https://img.shields.io/badge/Tensorflow-dfaeff?logo=tensorflow&logoColor=white)
    ](https://scikit-learn.org/stable/)
* [![prophet-shield](https://img.shields.io/badge/FacebookProphet-dfaeff?logoColor=white)
    ](https://scikit-learn.org/stable/)   
* [![nltk-shield](https://img.shields.io/badge/NLTK-dfaeff?&logo=&logoColor=white)
    ](https://textblob.readthedocs.io/en/dev/)
* [![xgboost-shield](https://img.shields.io/badge/XGBoost-dfaeff?&logo=XGBoost&logoColor=white)
    ](https://xgboost.readthedocs.io/en/stable/)
* [![textblob-shield](https://img.shields.io/badge/TextBlob-dfaeff?&logo=&logoColor=white)
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
%pip install tensorflow

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
## Acquisition<a name="acquisition"></a>

- Data acquisition contains 3 platforms: **TikTok**, **Youtube**, **Instagram**; 5 categories: Fahion & Beauty, Humor, Political Contents, Food, Fitness & Lifestyle

- Tiktok data is acquired through TikAPI, using search hashtag and search top influencers approach, detailed steps please reference [**acquisition**](https://github.com/Social-Media-Capstone/Social-Media-Engagement-Forecasting/tree/main/acquisition)

- Youtube data is acquired through `youtube-search-python 1.6.6` (built-in Python library), detailed steps please reference [**acquisition**](https://github.com/Social-Media-Capstone/Social-Media-Engagement-Forecasting/tree/main/acquisition)

- Instagram data is acquired and extracted through a confidential source and Instagram Graph API. If you're interested in the data source, please contact [**Meredith Wang**](wang.meredith09@gmail.com) directly

- Created `env.py` that contains API key credentials to access the data from TikTok API, and Instagram Graph API

- Created `acquire.py` file that contains functions for data acuiqisiont

## Preparation<a name="preparation"></a>
- **Automated Data Extraction**

- **Missing Values**

- **Datetime Conversion**

- **Data Encoding**

- **Text Cleaning**

## Exploration<a name="exploration"></a>


![roughviz](https://user-images.githubusercontent.com/105242871/192079926-96185ad2-505d-4181-8556-ab94c867f2b5.gif)
- Addressed initial questions to find what are the key features that drive engagement

- Explored each feature's correlation with engagement metrics

- Used statistical testing and visualizations to understand relationships between features and find driver of engagement.

- We built interactive dashboard for the audience to grasp the key findings of our exploration.

## Modeling<a name="modeling"></a>
- Last Observed Value (Baseline)
- Moving Average: The future will look, on average, like recent history.
- Holt's Linear Trend
- Previous Cycle
- Facebook Prophet
- ARIMA
- Long Short Term Memory Neural Network


# Conclusion<a name="conclusion"></a>
## Key Findings<a name="key_findings"></a>
▪️ Over **93%** of trending content on TikTok are short(0-15s) & medium(15-60s) videos.

▪️ Video duration and engagement rate is dependent on the cateogory. For example: humor content have the highest performance with extra-long (>3mins) videos, whereas political content perform the best with short (0-15s) videos.

▪️ Trending content of all categories on TikTok have **11M** views, **1.4M** likes, **10.7K** comments, and **34.5K** shares on average.

▪️ Total engagement of 2-year global trending content of each platform: TikTok is **6x** more than YouTube, and more than **1000x** more than Instagram.

▪️ TikTok total engagement has increated **980%** from 2019 to Sep 2022.

▪️ TikTok users respond to **major social/political events** significantly. Engagement peak/rise present prior, during, and after time period of the events.

▪️ Trending content creators' follower size has **decreased** since Jan 2021. TikTok's algorithm has been incentivizing **small creators** to push out content.

▪️ Content-description text frequency **DOES NOT** correlate with engagement. There are specific words that drive engagement for each niche. Our natural language processing general linear model predicts word choice 42% more accurate than baseline.

▪️ Facebook Prophet model forecast engagement with **57%** improvement compared to baseline.

▪️ Total engagement on TikTok is predicted to increase **27%** within the next year (Oct 2022 - Oct 2023). 



## Next Steps<a name="next_steps"></a>

Despite the overall effectiveness of our best-performing model, there is always room for improvement and optimization.
We're currently working on future devlopenet including:

▪️ Taking a closer look the differences between influencers and common users.

▪️ Including more niches/categories into our scope. For example: pets, sports, dance.

▪️ Doing bi-gram & tri-gram analysis on content description as long as the content of comments on videos.

▪️ Getting users' demographic data and analyzing the relatinship of location, user's age, etc. with engagement.
