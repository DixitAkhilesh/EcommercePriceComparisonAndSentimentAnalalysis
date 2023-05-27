import requests
from bs4 import BeautifulSoup
import json


def extract_offers(url,webpage):
    
    print("Extracting Offers!")
    soup = BeautifulSoup(webpage.content,"html.parser")
    offers = []
    
    carousel_cards = soup.find_all('li', class_='a-carousel-card')
    for card in carousel_cards:
        offer_title = card.find('h6', class_='a-size-base').text.strip()
        offer_description = card.find('span', class_='a-truncate-full').text.strip()
        offers.append({'title': offer_title, 'description': offer_description})

    print(offers)
            
    return offers

def extract_highlights(url, webpage):
    soup = BeautifulSoup(webpage.content, "html.parser")
    data = []
    rows = soup.find_all('tr', class_='a-spacing-small')

    for row in rows:
        label = row.find('td', class_='a-span3').text.strip()
        value = row.find('td', class_='a-span9').text.strip()
        data.append({'label': label, 'value': value})

    print(data)
    return data
    

def extract_a_data(url):
    
    print("Yess")
    HEADERS = ({'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.46','Accept-Language' : 'en-US, en;q=0.5'})
    webpage = requests.get(url,headers=HEADERS)
    offers = extract_offers(url,webpage)
    highlights = extract_highlights(url,webpage)
    # print(highlights)
    # if not offers and not highlights:
    #     print("No data found.")
    #     return

    
    data = {
        'url': url,
        'offers': offers,
        # 'highlights': highlights
    }

    # Save offers as JSON
    with open('..\\Frontend\\src\\json_files\\AmazonExtract.json', 'w') as file:
        json.dump(data, file, indent=4)