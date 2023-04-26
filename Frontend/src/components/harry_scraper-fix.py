import requests
import pandas as pd
from bs4 import BeautifulSoup
import random

review_title = []

def getRandomProxy():
    # Using Proxy
    proxy = {
        "http":f"http://Kh072ICB0vRFuRg9:wifi;;@proxy.soax.com:{9000 + random.randint(0,9)}",
        "https":f"http://Kh072ICB0vRFuRg9:wifi;;@proxy.soax.com:{9000 + random.randint(0,9)}"
    }
    return proxy

# def extractReviews(reviewUrl, pageNumber):

def extractProductImage(productUrl):
    product_images = []
    resp = requests.get(productUrl)
    soup = BeautifulSoup(resp.content, "html.parser")
    prods = soup.find_all("img", class_="s-image")
    for i in prods:
        prod_img = i.get("src")
        product_images.append(prod_img)
    print(product_images)


# def extractReviews(reviewUrl):
#     resp = requests.get(reviewUrl)
#     soup = BeautifulSoup(resp.text, "html.parser")
#     # reviews = soup.find_all("div", {"data-hook":"review"})
#     # print(reviews) 
#     reviews =  soup.findAll("div", {"data-hook":"review"})
#     print(reviews)
#     for i in reviews:
#         name = i.text
#         review_title.append(name)
#     # print(review_title)



    # # Now extract reviews from the raw html obtained
    # for item in reviews:
    #     #  lets analyze the code by writing it to file
    #     with open('backend/web scrapper/outputs/file.html','w',encoding="utf-8") as f:
    #         if item:
    #             f.write(str(item))
                
    #     title_element = item.find('a', {'data-hook': 'review-title'})
    #     if title_element is not None:
    #         title_text = title_element.text.strip()
    #     else:
    #         title_text = None
    #     rating_element = item.find('i', {'data-hook': 'review-star-rating'})
    #     if rating_element is not None:
    #         rating_text = rating_element.text.strip()
    #     else:
    #         rating_text = None
    #     body_element = item.find('span', {'data-hook': 'review-body'})
    #     if body_element is not None:
    #         body_text = body_element.text.strip()
    #     else:
    #         body_text = None

    #     review= {
    #         'productTitle': soup.title.text.replace("Amazon.in:Customer reviews: ", "").strip(),
    #         'Review Title': item.find('a', {'data-hook': 'review-title'}).text.strip(),
    #         'Rating': item.find('i', {'data-hook': 'review-star-rating'}).text.strip(),
    #         'Review Body': item.find('span', {'data-hook': 'review-body'}).text.strip(),
    #     }
    #     # print(review)
    #     review_title.append(review)
    #     break


# def totalPages(reviewUrl):
#     resp = requests.get(reviewUrl)
#     soup = BeautifulSoup(resp.text, "html.parser")
#     reviews = soup.find("div", {"data-hook":"cr-filter-info-review-rating-count"})
#     reviews_cnt_txt = reviews.text.strip().split(',')[1].split(" ")[0]
#     reviews_cnt = int(reviews_cnt_txt.replace(',',''))
#     return reviews_cnt



# def getreviews(product_links):
#     for link in product_links:
#         product_url = link
#         reviewUrl = product_url.replace("dp","product-reviews") + "?pageNumber=" + str(1)
#         # print(reviewUrl)
#         total_pg = totalPages(reviewUrl) 

#         for i in range(1,total_pg//10):
#             print(f"Running for page {i}")
#             try:
#                 reviewUrl = product_url.replace("dp","product-reviews") + "?pageNumber=" + str(i)
#                 print(reviewUrl)
#                 extractReviews(reviewUrl)
#             except Exception as e:
#                 print(e)
#             break
#         print(review_title)
#         # df = pd.DataFrame(reviewlist)
#         # df.to_excel('output.xlsx', index=False)
        
#         break  # sirf first product of the list ke reviews lega ye


def extractProductUrls(productUrl):
    product_links = []
    resp = requests.get(productUrl)
    soup = BeautifulSoup(resp.content, "html.parser")
    prods = soup.find_all("a", class_="a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal")
    for i in prods:
        prod_url = i.get("href")
        product_links.append("https://www.amazon.in" + prod_url)
    print(product_links) 

    # getreviews(product_links) # function to fetch reviews of every product url

    # for link in product_links:
    #     # print(link)
    #     extractProductdetails(link)

def extractProductMainPageReviews(productUrl):
    reviews = []
    total_reviews = 0
    resp = requests.get(productUrl)
    soup = BeautifulSoup(resp.text, "lxml")
    stars = soup.find_all("span", class_ = "a-icon-alt")
    num_of_reviews = soup.find_all("span", class_ = "a-size-base s-underline-text")
    count = 0
    for i in stars:
        for j in num_of_reviews:
            if count<5:
                review = i.text
                total_reviews = j.text
                reviews.append(review + " " + total_reviews)
                count += 1
            else:
                break
    print(reviews)


def extractProductName(productUrl):
    product_names = []
    resp = requests.get(productUrl)
    soup = BeautifulSoup(resp.text, "lxml")
    prods = soup.find_all("span", class_ = "a-size-medium a-color-base a-text-normal")
    print(resp.text)
    count = 0
    for i in prods:
        if count<5:
            prod_name = i.text
            product_names.append(prod_name)
            count += 1
        else:
            break
    print(product_names)
    # extractProductMainPageReviews(productUrl)
    


        # separating the specifications from names
        # fin_product_name=[]
        # renewed  = "Renewed"
        # for i in product_names:
        #     if renewed in i:
        #         name = i[1:].split("(")
        #         fin_product_name.append(name[0])
        #     else:
        #         name = i.split("(")
        #         fin_product_name.append(name[0])
    # print(product_names)

def extractProductdetails(productUrl):
    product_details = []
    resp = requests.get(productUrl)
    soup = BeautifulSoup(resp.text, "lxml")
    prods = soup.find_all("ul", class_ = "a-unordered-list a-vertical a-spacing-mini")
    for i in prods:
        detail = i.text
        product_details.append(detail)
    print(product_details)

#realme narzo 50a

def main():
    s= input("Enter product name: ")
    st = s.split()
    s = s.replace(" ", "+")
    # print(st[0])
    # https://www.amazon.in/s?k=acer+nitro+5
    pageNumber =3 
    productUrl = "https://www.amazon.in/s?k="+ s 
    print(productUrl)
    # url = "https://www.amazon.in/"+ st[0] +"-Storage-Definition-Display-Included/dp/B0BG1PYJR4/ref=sr_1_1"
    # reviewUrl = url.replace("dp", "product_reviews") + "?pageNumber=2" + str(pageNumber)
    # print(reviewUrl)


    # extractProductImage(productUrl)
    extractProductName(productUrl)
    # extractProductUrls(productUrl)
    # extractProductdetails(productUrl)
    # extractReviews(reviewUrl, pageNumber)


main() 
