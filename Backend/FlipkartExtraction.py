import requests
from bs4 import BeautifulSoup
import json


def extract_offers(url,webpage):
    
    soup = BeautifulSoup(webpage.content,"html.parser")
    # print(url)
    offer_div = soup.find('div', class_='XUp0WS')
    # print(offer_div)
    offer_spans = offer_div.find_all('span', class_='_3j4Zjq row')
    if not offer_spans:
        print("No Data ")

    else:
        offers = []
        print("Offers")

        for span in offer_spans:
            offer_title = span.find('span', class_='u8dYXW').text
            offer_description = span.find('span').find_next_sibling('span').text
            offers.append({'title': offer_title, 'description': offer_description})

        # Print scraped offers
        for offer in offers:
            print('Title:', offer['title'])
            print('Description:', offer['description'])
            print('-----')
            
    return offers

def extract_highlights(url, webpage):
    soup = BeautifulSoup(webpage.content, "html.parser")
    list_items = soup.find_all('li', class_='_21Ahn-')
    highlights = []
    if not list_items:
        print("No Data")
    else:
        highlights = [item.text for item in list_items]
    for highlight in highlights:
        print("Highlight:", highlight)
    return highlights
    

def extract_f_data(url):
    
    HEADERS = ({'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.46','Accept-Language' : 'en-US, en;q=0.5'})
    webpage = requests.get(url,headers=HEADERS)
    offers = extract_offers(url,webpage)
    highlights = extract_highlights(url,webpage)
    print(highlights)
    if not offers and not highlights:
        print("No data found.")
        return

    
    data = {
        'url': url,
        'offers': offers,
        'highlights': highlights
    }

    # Save offers as JSON
    with open('..\\Frontend\\src\\json_files\\FlipkartExtract.json', 'w') as file:
        json.dump(data, file, indent=4)