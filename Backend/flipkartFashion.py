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
product_desc= []

def extractProductDescription(productUrl, webpage):
    soup = BeautifulSoup(webpage.text, 'lxml')
    prod_detail = soup.find_all("ul", class_ = "_1xgFaf")
    
    count=0
    for i in prod_detail:
        if(count < 5):
            detail = i.text
            product_desc.append(detail)
            count += 1
        else:
            break
    # print(product_desc)
    
    
def extractProductName(productUrl,webpage):
    
    soup = BeautifulSoup(webpage.text,"lxml")
    prod_names = soup.find_all('a',class_ = "IRpwTa") 
    
#     print(prod_names)
    count = 0
    for i in prod_names: 
        if count < 5:
            name = i.text
            product_names.append(name);    
            count += 1
        else:
            break
    # print(product_names)
    
    
def extractProductUrls(productUrl,webpage):
    soup = BeautifulSoup(webpage.content,"html.parser")
    prod_urls = soup.find_all('a',class_ = "IRpwTa")
#     print(prod_urls)
    count = 0
    for i in prod_urls:
        if count <5:    
            prod_url = i.get("href")
            product_urls.append("https://www.flipkart.com" + prod_url)
            count += 1
        else:
            break
    # print(product_urls) 
    
def extractProductPrice(productUrl,webpage):
    
    soup = BeautifulSoup(webpage.content,"html.parser")
    prod_prices = soup.find_all('div',{'class':'_30jeq3'})
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
    stars = soup.find_all('div',{'class': '_3LWZlK'})
    num_of_reviews = soup.find_all('span',{'class': '_2_R_DZ'})
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
            num = i.text.split('\xa0&\xa0')[1].split()[0]
            num = num.split(',')
            sumnum = ''
            for i in num:
                sumnum += i
            total_reviews.append(sumnum)
            count1 += 1
        else:
            break
    # print(product_reviews)
    # print(total_reviews)
    

def extractProductImage(productUrl,webpage):
    
    soup = BeautifulSoup(webpage.content,"html.parser")
    prods = soup.find_all('img',{'class':'_2r_T1I'})
    count = 0
    for i in prods:
        if count < 5:
            prod_img = i.get("src")
            product_images.append(prod_img)
            count += 1
        else:
            break
    # print(product_images)
    
def flipkart_fashion_function(search_input):
    print("Fashion!!")
    st = search_input.split()
    search_input = search_input.replace(" ", "+")
    productUrl = "https://www.flipkart.com/search?q="+ search_input 
    HEADERS = ({'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.46','Accept-Language' : 'en-US, en;q=0.5'})
    webpage = requests.get(productUrl,headers=HEADERS)
    print(productUrl)
    soup = BeautifulSoup(webpage.content,"html.parser")
    
    
    extractProductName(productUrl,webpage)
    extractProductUrls(productUrl,webpage)
    extractProductPrice(productUrl,webpage)
    # extractReviews(productUrl,webpage)
    extractProductImage(productUrl,webpage)
    # extractProductDescription(productUrl, webpage) 

    all_details = zip(product_names,product_urls,product_desc,product_prices,product_reviews,total_reviews,product_images)
    
    
    file_name = "flipkart_product.json"
    directory_name = ".\json_files" 
    
    filePath = os.path.join(directory_name, file_name)
    print(filePath)
    
    # header = ['Name', 'Link',"Description",'Price', 'Reviews', 'Number of Reviews','Images']

    data = []
    for i in range(0,len(product_names)):
        item = {
            'product_name': product_names[i],
            'product_url': product_urls[i],
            'product_price': product_prices[i],
            # 'product_review': product_reviews[i],
            # 'total_review': total_reviews[i],
            'product_image': product_images[i]
        }
        data.append(item)

    
    with open("..\\Frontend\\src\\json_files\\flipkart_fashion_product.json", 'w') as f:
        json.dump(data, f,indent=6)

    
    
def main():
    print("Starting...")


main()