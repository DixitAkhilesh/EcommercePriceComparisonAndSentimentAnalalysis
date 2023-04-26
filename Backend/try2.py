from bs4 import BeautifulSoup
import requests
import pandas as pd
import csv
import os
import json
from pymongo import MongoClient


HEADERS = ({'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Safari/537.36 Edg/113.0.0.0','Accept-Language' : 'en-US, en;q=0.5'})

product_names = []
product_urls = []
product_prices = []
product_reviews = []
total_reviews = []
product_images = []
all_details = []
review_titles = []
main_review_titles = []

# Database related constants


def extractProductName(productUrl,webpage):
    
    soup = BeautifulSoup(webpage.content,"html.parser")
    prod_names = soup.find_all('span',{'class':'a-size-medium a-color-base a-text-normal'})
    count = 0
    for i in prod_names: 
        if count < 5:
            name = i.text
            product_names.append(name);    
            count += 1
        else:
            break
    # print(product_names)
    # print()
    
    
def extractProductUrls(productUrl,webpage):
    
    soup = BeautifulSoup(webpage.content,"html.parser")
    prod_urls = soup.find_all('a',{'class':'a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal'})
    count = 0
    for i in prod_urls:
        if count <5:    
            prod_url = i.get("href")
            product_urls.append("https://www.amazon.in" + prod_url)
            count += 1
        else:
            break
    # print(product_urls)
    
def extractProductPrice(productUrl,webpage):
    
    soup = BeautifulSoup(webpage.content,"html.parser")
    prod_prices = soup.find_all('span',{'class':'a-offscreen'})
    count = 0
    for i in prod_prices:
        if count <5: 
            prod_price = i.text
            product_prices.append(prod_price)
            count += 1
        else:
            break
    # print(product_prices) 

def extractReviews(productUrl,webpage):
    
    soup = BeautifulSoup(webpage.content,"html.parser")
    stars = soup.find_all('span',{'class': 'a-icon-alt'})
    num_of_reviews = soup.find_all('span',{'class': 'a-size-base s-underline-text'})
    count = 0
    for i in stars:
        if count < 5:
            prod_review = i.text
            product_reviews.append(prod_review)
            count += 1
        else:
            break
    count1 = 0
    for i in num_of_reviews:
        if count1<5:
            num = i.text
            num = num.replace(",","")
            total_reviews.append(num)
            count1 += 1
        else:
            break
    # print(product_reviews)
    # print(total_reviews)
    

def extractProductImage(productUrl,webpage):
    
    
    soup = BeautifulSoup(webpage.content,"html.parser")
    prods = soup.find_all('img',{'class':'s-image'})
    count = 0
    for i in prods:
        if count < 5:
            prod_img = i.get("src")
            product_images.append(prod_img)
            count += 1
        else:
            break
    # print(product_images)
    
def extractAllReviews():
      
        reviewUrl = product_urls[0].replace('dp','product-reviews') + "?pageNumber=" + str(i)
        # print("for url: "+ reviewUrl)
        # print(reviewUrl)
        webpage = requests.get(reviewUrl,headers=HEADERS)
        # print(webpage.content)
        if webpage.status_code == 200:
            soup = BeautifulSoup(webpage.content, "html.parser")
            total_review_title = soup.find_all('a',{'data-hook':'review-title'})
            # print(total_review_title)
            for review_title in total_review_title:        
                if review_title is not None:
                    review_title = review_title.text.strip()
                    review_titles.append(review_title)
                    main_review_titles.append(review_titles)
        else:
            print("Error occured")

def reviews_analysis():
    
    count = 1
    # for url,num in zip(product_urls,total_reviews):
    # print(product_urls[0])
    reviewUrl = product_urls[0] 
    reviewUrl = reviewUrl.replace('dp','product-reviews')
    reviewUrl = reviewUrl.split("=")
    url = reviewUrl[0] + '=cm_cr_getr_d_paging_btm_next_' + str(1) + '?ie=UTF8&reviewerType=all_reviews&pageNumber='+ str(1)
    print(reviewUrl)
    
    webpage = requests.get(url,headers=HEADERS)
    soup = BeautifulSoup(webpage.content, "html.parser")
    
    review_info = soup.find('div', {'data-hook':'cr-filter-info-review-rating-count'})
    # print (review_info)
    if review_info is not None:
        parts = review_info.text.strip()  
        print(parts)      
        parts = parts.replace(",","")
        parts = parts.split(" ")
        number = int(parts[-3])
        # print(number)

        for i in range (1,number//10):
            url = reviewUrl[0] +'=cm_cr_getr_d_paging_btm_next_' + str(i) + '?ie=UTF8&reviewerType=all_reviews&pageNumber='+ str(i)
            # print(url) 
            webpage2 = requests.get(url,headers=HEADERS)
            
            if webpage is not None:
                soup = BeautifulSoup(webpage2.content,"html.parser")
                # print(soup)
                reviews = soup.find_all('a',attrs= {'data-hook':'review'})
                # print(reviews)
                # title_element = item.find('a', {'data-hook': 'review-title'})
                    
# print(main_review_titles)
            
def fileCreation():
    file_name = "amazon_product.json"
    directory_name = ".\json_files" 
    filePath = os.path.join(directory_name, file_name)
    
    data = []
    for i in range(0,len(product_names)):
        item = {
            'product_name': product_names[i],
            'product_url': product_urls[i],
            'product_price': product_prices[i],
            'product_review': product_reviews[i],
            'total_review': total_reviews[i],
            'product_image': product_images[i],
        }
        data.append(item)
        
    print(data)
    # if data:
    #     collection.insert_many(data)
    # client = MongoClient('mongodb://localhost:27017/')
    # db = client['mydatabase']
    # collection = db['mycollection'] 
    # collection.insert_many(data)
    # client.close()
    
    # write the data to a JSON file
    with open("..\\Frontend\\src\\json_files\\amazon_product.json", 'w') as f:
        json.dump(data, f)
    f.close()

    
def main():
    search_input = input("Enter product name: ")
    st = search_input.split()
    search_input = search_input.replace(" ", "+")
    productUrl = "https://www.amazon.in/s?k="+ search_input 
    print(productUrl)
    webpage = requests.get(productUrl,headers=HEADERS)

    extractProductName(productUrl,webpage)
    extractProductUrls(productUrl,webpage)
    extractProductPrice(productUrl,webpage)
    extractReviews(productUrl,webpage)
    extractProductImage(productUrl,webpage)
    fileCreation()
    
    # reviews_analysis()
    # return file_path
    # return search_input
    

main()