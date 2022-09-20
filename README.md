# Tiktok-Youtube-Instagram-Forecasting
By Brad Gauvin, Jess Gardin, Meredith Wang, and Saroj Duwal
Date: 09/23/2022

## Readme Outline
- [Project Description](#project_desc)  
    - [Scenario](#scenario)
    - [Goals](#goals)
        - [Deliverables](#deliverables)
    - [Project Dependencies](#dependencies)

- [About the data](#data)
    - Scope
    - Acquisition
    - Preparation
    - Data Dictionary

- [Project Planning](#plan)  


# About the project <a name="project_desc"></a>
Using 

## Scenario <a name="scenario"></a>

This project serves as a proof of concept to demonstrate the viability of these types of classification problems using free-form text as an input.

<!-- > __Agile Story__  
    As a {persona}  
    I want {feature}  
    So that {goal}   -->

## Goals <a name="goals"></a>

analyze  top four different categories from popular platform TikTok.  Engineer features from the project's README.md file using TF and IDF, as well as the occurrance of certain keywords inside of a document.

### Deliverables <a name="deliverables"></a>

- Report notebook titled `Report.ipynb`
- Google/canva Slides presentation consisting content slides.
- project webpage
- project white paper

## Reproducing this project <a name="requirements"></a>

<!-- Add NLTK and the NLTK downloads -->

### Dependencies

This project makes use of several technologies that will need to be installed
* [![python-shield](https://img.shields.io/badge/Python-3-blue?&logo=python&logoColor=white)
    ](https://www.python.org/)
* [![jupyter-shield](https://img.shields.io/badge/Jupyter-notebook-orange?logo=jupyter&logoColor=white)
    ](https://jupyter.org/)
* [![numpy-shield](https://img.shields.io/badge/Numpy-grey?&logo=numpy)
    ](https://numpy.org/)
* [![pandas-shield](https://img.shields.io/badge/Pandas-grey?&logo=pandas)
    ](https://pandas.pydata.org/)
* [![matplotlib-shield](https://img.shields.io/badge/Matplotlib-grey.svg?)
    ](https://matplotlib.org)
* [![seaborn-shield](https://img.shields.io/badge/Seaborn-grey?&logoColor=white)
    ](https://seaborn.pydata.org/)
* [![scipy-shield](https://img.shields.io/badge/SciPy-grey?&logo=scipy&logoColor=white)
    ](https://scipy.org/)
* [![sklearn-shield](https://img.shields.io/badge/_-grey?logo=scikitlearn&logoColor=white&label=scikit-learn)
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
%pip install textblob
```

# About the data <a name="data"></a>

We scraped tiktok webpage using a third party API called TikAPI using top four categories with top hashtags used in each categories.

## Scope

For exploration and modeling we ignored any repositories featuring a language for which we did not scrape at least 10 samples, as well as any repositories that did not feature a language at all.

## Acquisition

- "env.py" has API key credentials to access the data from tiktok API
- Data acquisition used a combination of web-scraping and TikAPI  from the "acquire.py" module.
- Acquire module collects follow counts, like counts and play counts.
- 

## Preparation

To prepare the data for exploration and modeling we performed the following steps:
- Markdown links were removed from the corpus since the urls did not provide meaningful information
- HTML elements such as \<li>\</li> and \<strong>\</strong> were also removed for the same reason
- The text was then normalized and stripped of special characters
- Stopwords were removed
- New columns were created in the dataframe to represent the cleaned and lemmatized versions of the original
- Split the data into train, validate and test sets and stratify by the language
    - Train : 64 % of the data
    - Validate : 16 % of the data
    - Test : 20 % of the data

## Data Dictionary

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


# Project Planning <a name="plan"></a>

## Exploration

## Initial Hypotheses
- Covid-19 Pandemic resulted in spike of tiktok use
- Use of certain hashtags under particular categories
- 

## Modeling
- Created a time seriesmodel against which all models will be evaluated.
- 12 different models were compared against the baseline and model with the highest overall accuracy score was used to evaluate the test data set.


# Conclusion
### Summary

In seeking to predict programming language for GitHub repositories, we have explored our data thoroughly. \
We observed word clouds, word frequencies, and ran sentiment analyses in order to best determine any additional feature engineering that would improve our model. Although we were not able to identify any additional significant features to engineer from this exploration, we were able to identify problem areas and eliminate a host of stopwords which resulted in improved modeling.

Additionally, we have created and tested 12 different models on both uncleaned and cleaned and lemmatized data. Our 3 best performing models are:

1. Neural Network (not explicitly shown in this final notebook)
2. SVM Linear
3. XGBoost Classifier

In short, we found that our XGBoost Classifier model performed best on our uncleaned data, resulting in 58% accuracy on our test data. \
This performance beats our baseline by 115%.


### Next Steps

Despite the overall effectiveness of our best-performing model, there is always room for improvement and optimization.
If given more time to pursue better results, we could perform further investigation within exploration by:

1. Estimating each readme's school reading level. Not only would this be interesting as an anecdote, if proven useful, it could be imputed as a new feature to boost the accuracy of our model.

2. Handling ReadMes in a foreign language in a more succinct way. This could be handled more effectively by using a translator to convert all ReadMes into English for potentially better modeling accuracy. 
