from bs4 import BeautifulSoup
import requests
import pandas as pd
import csv
import os
import json

product_names = []
product_urls = []
product_prices = []
product_reviews = []
total_reviews = []
product_images = []
all_details = []
search_input = ''

def extractProductName(productUrl,webpage):
    print("Name")
    soup = BeautifulSoup(webpage.content,"html.parser")
    prod_names = soup.find_all('span',{'class':'a-size-medium a-color-base a-text-normal'})
    print("prodnmes: ", end = " ")
    print(prod_names) 
    count = 0
    for i in prod_names: 
        count+=1
        if count <= 7 and count >2:
            name = i.text
            product_names.append(name);    
        else:
            continue
    print("product names: ", end=" ")
    print(product_names)
    
    
def extractProductUrls(productUrl,webpage):
    
    soup = BeautifulSoup(webpage.content,"html.parser")
    prod_urls = soup.find_all('a',{'class':'a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal'})
    count = 0
    for i in prod_urls: 
        count+=1
        if count <= 7 and count >2:
            prod_url = i.get("href")  
            product_urls.append("https://www.amazon.in" + prod_url)
        else:
            continue
#     print(product_urls) 
    
def extractProductPrice(productUrl,webpage):
    
    soup = BeautifulSoup(webpage.content,"html.parser")
    prod_prices = soup.find_all('span',{'class':'a-offscreen'})
    count = 0
    for i in prod_prices: 
        count+=1
        if count <= 7 and count >2:
            prod_price = i.text
            product_prices.append(prod_price)
        else:
            continue
    # print(product_prices) 

def extractReviews(productUrl,webpage):
    
    soup = BeautifulSoup(webpage.content,"html.parser")
    stars = soup.find_all('span',{'class': 'a-icon-alt'})
    num_of_reviews = soup.find_all('span',{'class': 'a-size-base s-underline-text'})
    count = 0
    for i in stars: 
        count+=1
        if count <= 7 and count >2:
            prod_review = i.text.split()[0]
            product_reviews.append(prod_review)
        else:
            continue
    count1 = 0
    for i in num_of_reviews: 
        count1+=1
        if count1 <= 7 and count1 >2:
            num = i.text
            if not num:
                total_reviews.append("0")
            total_reviews.append(num)
        else:
            continue
    # print(product_reviews)
    print(total_reviews)
    

def extractProductImage(productUrl,webpage):
    
    soup = BeautifulSoup(webpage.content,"html.parser")
    prods = soup.find_all('img',{'class':'s-image'})
    count = 0
    for i in prods: 
        count+=1
        if count <= 7 and count >2:
            prod_img = i.get("src")
            product_images.append(prod_img)
        else:
            continue
    # print(product_images)
    
    
def amazon_function(search_input):
    st = search_input.split()
    search_input = search_input.replace(" ", "+")
    productUrl = "https://www.amazon.in/s?k="+ search_input 
    HEADERS = ({'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.46','Accept-Language' : 'en-US, en;q=0.5'})
    webpage = requests.get(productUrl,headers=HEADERS)
    print(productUrl)

    extractProductName(productUrl,webpage)
    extractProductUrls(productUrl,webpage)
    extractProductPrice(productUrl,webpage)
    extractReviews(productUrl,webpage)
    extractProductImage(productUrl,webpage)

    all_details = zip(product_names,product_urls,product_prices,product_reviews,total_reviews,product_images)
    
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
    
    
    file_name = "amazon_product.json"
    directory_name = ".\json_files" 
    filePath = os.path.join(directory_name, file_name)

    print("YESSSS")
    with open("..\\Frontend\\src\\json_files\\amazon_product.json", 'w') as f:
        json.dump(data, f,indent=6)
    
    
def main():
    print("Starting...")

main()