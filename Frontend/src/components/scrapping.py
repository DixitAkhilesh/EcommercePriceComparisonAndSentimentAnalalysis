import requests
import pandas as pd
from bs4 import BeautifulSoup
import random

product_images = []
product_names = []
product_urls = []
product_prices = []
reviews = []
total_reviews = 0

def getRandomProxy():
    # Using Proxy
    proxy = {
        "http":f"http://Kh072ICB0vRFuRg9:wifi;;@proxy.soax.com:{9000 + random.randint(0,9)}",
        "https":f"http://Kh072ICB0vRFuRg9:wifi;;@proxy.soax.com:{9000 + random.randint(0,9)}"
    }
    return proxy

# def extractProductImage(productUrl):
#     resp = requests.get(productUrl)
#     soup = BeautifulSoup(resp.content, "html.parser")
#     prods = soup.find_all('img',{'class':'s-image'})
#     for i in prods:
#         prod_img = i.get("src")
#         product_images.append(prod_img)
#     print(product_images)
    
def extractProductName(productUrl):
    product_names = []
    resp = requests.get(productUrl)
    soup = BeautifulSoup(resp.text, "lxml")
    print(resp.text)
    prods = soup.find_all("span", class_ = "a-size-medium a-color-base a-text-normal")
    count = 0
    for i in prods:
        if count<5:
            prod_name = i.text
            product_names.append(prod_name)
            count += 1
        else:
            break
    print(product_names)

def extractProductUrls(productUrl):
    resp = requests.get(productUrl)
    soup = BeautifulSoup(resp.content, "html.parser")
    prods = soup.find_all('a',{'class':'a-link-normal s-underline-text s-underline-link-text s-link-style a-normal'})
    for i in prods:
        prod_url = i.get("href")
        product_urls.append("https://www.amazon.in" + prod_url)
    print(product_urls) 

def extractProductPrice(productUrl):
    resp = requests.get(productUrl)
    soup = BeautifulSoup(resp.content, "html.parser")
    prods = soup.find_all('span',{'class':'a-offscreen'})
    for i in prods:
        prod_price = i.text
        product_prices.append(prod_price)
    print(product_prices) 

def extractReviews(productUrl):
    resp = requests.get(productUrl)
    soup = BeautifulSoup(resp.text, "lxml")
    stars = soup.find_all('span',{'class': 'a-icon-alt'})
    num_of_reviews = soup.find_all('span',{'class': 'a-size-base s-underline-text'})
    count = 0
    for i in stars:
        for j in num_of_reviews:
            if count<5:
                review = i.text
                total_reviews += j.text
                reviews.append(review)
                count += 1
            else:
                break
    print(reviews)
    
# def extractProductdetails(productUrl):
#     product_details = []
#     resp = requests.get(productUrl)
#     soup = BeautifulSoup(resp.text, "lxml")
#     prods = soup.find_all("ul", class_ = "a-unordered-list a-vertical a-spacing-mini")
#     for i in prods:
#         detail = i.text
#         product_details.append(detail)
#     print(product_details)

def extractInfo(productUrl):
    # extractProductImage(productUrl)
    extractProductName(productUrl)
    extractProductUrls(productUrl)
    extractProductPrice(productUrl)
    extractReviews(productUrl)



def main():
    s= input("Enter product name: ")
    st = s.split()
    s = s.replace(" ", "+")
    productUrl = "https://www.amazon.in/s?k="+ s 
    print(productUrl)

    extractInfo(productUrl)
    # extractProductdetails(productUrl)
    # print(product_names, product_urls,product_images,reviews,total_reviews)

main() 
