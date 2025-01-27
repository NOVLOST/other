
import random
import time

import requests as re
from bs4 import BeautifulSoup as bs
from time import sleep
import csv
import json

from unicodedata import category

header = {
'Accept' : '*/*',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:134.0) Gecko/20100101 Firefox/134.0'}
page_index = 0
for i in range(0,180):
    time.sleep(5)
    url = f"https://baza.drom.ru/ulyanovskaya-obl/wheel/disc/?page={page_index}#center=48.701177077849444%2C54.35420831869696&zoom=9.905846777792929"

    response = re.get(url, headers=header)

    print(response.status_code)#статус код


    # with open('index.html','w', encoding='utf16') as file:
    #     file.write(response.text)
    # with open('index.html',encoding='utf16') as file:
    #     source = file.read()

    soup = bs(response.text,'lxml')
    print(response.text)

    raw_name = soup.find_all('div',class_= 'descriptionCell bull-item__cell bull-item__description-cell')
    raw_img = soup.find_all('div',class_='bull-image-overlay')


    def get_img(raw):

        for i in raw:
            img = i.find('img').get('src')

            yield img

    product_info = []
    index = 0
    for i in raw_name:
        name = i.find('a',class_='bulletinLink bull-item__self-link auto-shy').text
        price = i.find('div',class_='price-block__final-price finalPrice').text
        price = price.split('₽')[0]
        city = i.find('span' ,class_='bull-delivery__city').text
        img = get_img(raw_img)
        print(name)



        product_info.append({
            'Name':name,
            'Price':price + '₽',
            'city': city,
            'img': list(img)[index]

        })
        index += 1

    with open(f"wheels.json", 'w', encoding='utf16') as file:
        json.dump(product_info, file, indent=4, ensure_ascii=False)
