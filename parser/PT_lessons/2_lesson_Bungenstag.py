import time

import requests as re
from bs4 import BeautifulSoup as bs
import json

""""Это первая часть в ней мы берем ссылки на страницы депутатов для последующей обработки"""
# persons_url_list = []
# for i in range(0,780,12):
#
#     url = f'https://www.bundestag.de/ajax/filterlist/de/abgeordnete/862712-862712?limit=12&noFilterSet=true&offset={i}'
#     print(url)
#
#     response = re.get(url)
#     result = response.content
#
#     soup = bs(result,'lxml')
#
#     persons = soup.find_all('a')
#
#
#     for person in persons:
#         person_page_url = person.get('href')
#         persons_url_list.append(person_page_url)
#         print(person_page_url)
#
# with open('persons_url_list.txt','a') as file:
#     for link in persons_url_list:
#         file.write(f'{link}\n')
"""Вторая часть в ней мы работаем непосредственно с ссылками"""
def gen_links(soup):
    links = []
    raw_links = soup.find_all('a',class_='bt-link-extern')
    for i in raw_links:

        links.append(i.get('href'))
    return links

with open('persons_url_list.txt') as file:

    lines = [line.strip() for line in file.readlines()]
    flag = False
    data_person = []
    count = 0
    for link in lines:
        print(f"№{count} {link} in progress...")
        response = re.get(link)
        result = response.content

        soup = bs(result,'lxml')

        name = soup.find('div',class_='col-xs-8 col-md-9 bt-biografie-name').find('h2').text
        job_name = soup.find('div',class_='bt-biografie-beruf').find('p').text
        other_links = gen_links(soup.find('ul', class_='bt-linkliste'  ))

        name_and_party = name.split(',')
        name_and_party[1] = name_and_party[1].strip()


        data = {
            'name': name_and_party[0][1:],
            'job_name': name_and_party[1],
            'other_links': other_links

        }
        data_person.append(data)
        count += 1
        with open("bundenstag.json", 'w',encoding='utf16') as file:
            json.dump(data_person, file, indent=4, ensure_ascii=False )

