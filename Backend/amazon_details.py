from bs4 import BeautifulSoup
import requests
import pandas as pd
import numpy as np
import random
import re
import string
from collections import Counter

import nltk
import matplotlib.pyplot as plt
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

from nltk.sentiment import SentimentAnalyzer
from nltk.sentiment.util import *
from nltk.sentiment.vader import SentimentIntensityAnalyzer

from wordcloud import WordCloud
import seaborn as sns
import matplotlib. pyplot as plt
import cufflinks as cf
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer  #must read doc 
from textblob import TextBlob
# %matplotlib inlines
import warnings


# add your user agent 
HEADERS = ({'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.46', 'Accept-Language': 'en-US, en;q=0.5'})

reviewlist = []

def extractReviews(reviewUrl):
    # HTTP Request
    webpage = requests.get(reviewUrl, headers=HEADERS)

    # Soup Object containing all data
    soup = BeautifulSoup(webpage.content, "html.parser")
    reviews = soup.findAll('div',attrs= {'data-hook':'review'})
#     print(reviews)
    
    for item in reviews:
#         with open('outputs/file.html', 'w', encoding='utf-8') as f:
#             f.write(str(item))
        
        title_element = item.find('a', {'data-hook': 'review-title'})
        if title_element is not None:
            title_text = title_element.text.strip()
        else:
            continue
        
        body_element = item.find('span', {'data-hook': 'review-body'})
        if body_element is not None:
            body_text = body_element.text.strip()
        else:
            continue
        review = {
            'Review Title': title_text,
            'Review Body': body_text,
        }
        reviewlist.append(review)
        
def totalPages(reviewUrl):
    # HTTP Request
    webpage = requests.get(reviewUrl, headers = HEADERS)

    # Soup Object containing all data
    soup = BeautifulSoup(webpage.content, "html.parser")
    reviews = soup.find('div', attrs={'data-hook':'cr-filter-info-review-rating-count'})
    # print(reviews)
    # reviews_cnt = int(reviews.text.strip().split(',')[1].split()[0])
    return 100

def amazon_details_function(productUrl):
    
    print("Working Successfully!")
    pageNumber = 3
    reviewUrl = productUrl.replace('dp','product-reviews') + "?pageNumber=" + str(pageNumber)
    # print(reviewUrl)
    totalPg = totalPages(reviewUrl)
    
    for i in range(1,totalPg//10):
        print(f"Running for page {i}")
        try: 
            reviewUrl = productUrl.replace("dp","product-reviews") + "&pageNumber=" + str(i)
            # print(reviewUrl)
            extractReviews(reviewUrl)
        except Exception as e: 
            print(e)
        
    # print(reviewlist)

    df = pd.DataFrame(reviewlist)
#     preprocess_data(df)
    df.to_csv('./reviews/amazon_reviews.csv', index=False, mode='w')
    # get_amazon_details()
    
###########################################################################################
                                #Sentiment Analysis:
###########################################################################################

def get_amazon_details(filePath):
    df = pd.read_csv(filePath)

    df['reviewText']= df[df.columns[0:]].apply(
        lambda x: ' '.join(x.dropna().astype(str)),
        axis=1
    )

    #Removing the earlier two columns
    del df['Review Title']
    del df['Review Body']

    rt = lambda x: re.sub("[^a-zA-Z]",' ',str(x))
    df['reviewText'] = df['reviewText'].map(rt)
    df['reviewText'] = df['reviewText'].map(rt).str.lower()
    # df['reviewText'][32]
    
    df[['polarity','subjectivity']] = df['reviewText'].apply(lambda Text:pd.Series(TextBlob(Text).sentiment))

    for index, row in df['reviewText'].items():
        score = SentimentIntensityAnalyzer().polarity_scores(row)
        neg = score['neg']
        neu = score['neu']
        pos = score['pos']
        if (neg>pos):
            df.loc[index, 'sentiment'] = 'Negative'
        elif pos>neg:
            df.loc[index, 'sentiment'] = 'Positive'
        else:
            df.loc[index, 'sentiment'] = 'Neutral'
    
    # print(df)
    sentimentlist = df['sentiment'].tolist()
    print("HELLOOO...")
    print("Amazon Details: ")
    print(sentimentlist)
    return sentimentlist

def main():
    print("Loading...")
    
main()

# 'https://www.amazon.in/Samsung-Storage-6000mAh-Purchased-Separately/dp/B09TWH8YHM/ref=sr_1_1_sspa?crid=1O14H4QEVBZX0&keywords=samsung+galaxy+f62&qid=1682692033&sprefix=samsung+galaxy+f62%2Caps%2C216&sr=8-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1'