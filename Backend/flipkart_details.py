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
sentimentlist = []

def extractReviews(reviewUrl):
    # HTTP Request
    webpage = requests.get(reviewUrl, headers=HEADERS)

    # Soup Object containing all data
    soup = BeautifulSoup(webpage.content, "html.parser")
    reviews = soup.findAll('div',attrs= {'class':'col _2wzgFH K0kLPL'})
#     print(reviews)
    
    for item in reviews:
#         with open('outputs/file.html', 'w', encoding='utf-8') as f:
#             f.write(str(item))
        
        title_element = item.find('p', {'class': '_2-N8zT'})
        if title_element is not None:
            title_text = title_element.text.strip()
        else:
            continue
        
        body_element = item.find('div', {'class': 't-ZTKy'})
        if body_element is not None:
            body_text = body_element.text.strip()
        else:
            continue
        review = {
            'Review Title': title_text,
            'Review Body': body_text,
        }
        reviewlist.append(review)
#     print(reviewlist)

# def totalPages(reviewUrl):
#     # HTTP Request
#     webpage = requests.get(reviewUrl, headers = HEADERS)

#     # Soup Object containing all data
#     soup = BeautifulSoup(webpage.content, "html.parser")
#     reviews = soup.find_all('div', attrs={'class':'row _2afbiS'})
#     for i in reviews:
#         review = i.text
#     reviews_cnt = review.split()[0]
#     review_lst = reviews_cnt.split(',')
#     revsum=''
#     for i in review_lst:
#         revsum += i
#     reviews_cnt = int(revsum)
# #     reviews_cnt = int(reviews.text.split()[0])
#     return reviews_cnt

def flipkart_details_function(productUrl):
    pageNumber = 3
    productUrl
    
    reviewUrl = productUrl.replace('/p/','/product-reviews/') + "&page=" + str(pageNumber)
#     print(reviewUrl)
    # totalPg = totalPages(reviewUrl)
    totalPg = 100  #considering 1000 reviews i.e.(10 pages) if reviews are greater than 1000.
    
    for i in range(1,totalPg//10):
        # print(f"Running for page {i}")
        try: 
            reviewUrl = productUrl.replace('/p/','/product-reviews/') + "&page=" + str(i)
            # print(reviewUrl)
            extractReviews(reviewUrl)
        except Exception as e: 
            print(e)
            
#     print(reviewlist)

    df = pd.DataFrame(reviewlist)

    df.to_csv('./reviews/flipkart_reviews.csv', index=False,mode ='w')

###########################################################################################
                                #Sentiment Analysis:
###########################################################################################

def get_flipkart_details(filePath):
    df = pd.read_csv(filePath)
    
    # For flipkart only
    df['Review Body'][32]
    df['Review Body'] = df['Review Body'].str.replace('READ MORE', '')
    # df['Review Body'][32]

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
    
    # print("HEllooo")
    sentimentlist = df['sentiment'].tolist()
    print(sentimentlist)
    return sentimentlist

def main():
    print("Loading...")
    
main()
