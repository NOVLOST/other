import random

import requests as re
from bs4 import BeautifulSoup as bs
from time import sleep
import csv
import json

from unicodedata import category

header = {
'Accept' : '*/*',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:134.0) Gecko/20100101 Firefox/134.0'}
#
# url = "https://health-diet.ru/table_calorie/?utm_source=leftMenu&utm_medium=table_calorie"
#
# response = re.get(url, headers=header)
#
# print(response)#статус код


# with open('index.html','w', encoding='utf16') as file:
#     file.write(response.text)
#
# with open('BSindex.html','w' ,encoding='utf16') as file:
#     file.write(soup.text)


# with open('index.html',encoding='utf16') as file:
#     source = file.read()
#
#
#
#
# soup = bs(source, "lxml")
#
#
#
#
# name_of_products = soup.find_all('a',class_='mzr-tc-group-item-href')
#
# print(name_of_products)
#
# categories_product = {}
# for staff in name_of_products:
#
#     staff_text = staff.text
#     staff_link ='https://health-diet.ru' + staff.get('href')
#     print(f'{staff_text},{staff_link}')
#
#     categories_product[staff_text] = staff_link
#
# with open('categories_product.json','w',encoding='utf16') as file:
#     json.dump(categories_product, file , indent=4, ensure_ascii=False)

with open('categories_product.json',encoding='utf16') as file:
    categories_product = json.load(file)

print(categories_product)
value_of_pages = int(len(categories_product)) - 1
all_pages = int(len(categories_product)) - 1
count = 0
procent = '*......... 1%'
print(f'номер страницы {count}')
for name,link in categories_product.items():

    if count != -1:
        symbols = [',',' ','-',"'"]
        for char in symbols:
            if char in name:
                name = name.replace(char,'_')


        response = re.get(url = link,headers=header)
        res_text = response.text

        with open(f"data/{count}_{name}.html",'w',encoding='utf16') as file:
            file.write(res_text)

        with open(f"data/{count}_{name}.html",encoding='utf16') as file:
            site = file.read()

        soup = bs(site,'lxml')

        #проверка на ошибку
        alert_block = soup.find(class_ = 'uk-alert uk-alert-danger uk-h1 uk-text-center mzr-block mzr-grid-3-column-margin-top')
        if alert_block is not None:
            continue
        #заголовки таблицы
        table_head = soup.find(class_="uk-overflow-container").find('tr').find_all('th')
        product_head = table_head[0].text
        calories_head = table_head[1].text
        protein_head = table_head[2].text
        fat_head = table_head[3].text
        carbo_head = table_head[4].text

        with open(f"data/{count}_{name}.csv",'w',encoding='utf16') as file:
            writer = csv.writer(file)
            writer.writerow(
            (
                product_head,
                calories_head,
                protein_head,
                fat_head,
                carbo_head

            )
            )
        # собираем данные продуктов
        product_data = soup.find(class_='uk-overflow-container').find('tbody').find_all('tr')

        product_info = []
        for staff in product_data:
            product_chara = staff.find_all('td')

            title = product_chara[0].find('a').text
            calories = product_chara[1].text
            protein = product_chara[2].text
            fats = product_chara[3].text
            carbon = product_chara[4].text

            product_info.append(
                {
                    'Titles':title,
                    "Calories":calories,
                    "Protein": protein,
                    'Fats': fats,
                    "carbon":carbon

                }
            )

            with open(f"data/{count}_{name}.csv", 'a', encoding='utf16') as file:
                writer = csv.writer(file)
                writer.writerow(
                    (
                        title,
                        calories,
                        protein,
                        fats,
                        carbon

                    )
                )

        with open(f"data/{count}_{name}.json",'a',encoding='utf16') as file:
            json.dump(product_info, file ,indent = 4,ensure_ascii=False )
        count += 1




        value_of_pages -= 1
        if value_of_pages == 0:
            print('All Done 100%!!!')
            break
        else:
            print(f' осталось {value_of_pages} из {all_pages}')
            sleep(random.randrange(2, 3))

