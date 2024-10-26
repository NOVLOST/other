import time

import requests as re
from bs4 import BeautifulSoup as bs
from time import sleep
from lxml import *

#сделать Парсинг описания машины в отдельный мб файли (\*_|_*/)

header = {"User-agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:109.0) Gecko/20100101 Firefox/115.0"}

def parser():
    print("HELLO")
    for num in range(1,5):
        sleep(10)
        url = f"https://auto.drom.ru/lada/2121_4x4_niva/page{num}/"

        response = re.get(url, headers=header)

        print(response)

        soup = bs(response.text, "lxml")

        data = soup.find_all("div", class_="css-1f68fiz ea1vuk60")

        for i in data:
            complect_part_3 = ""

            try:
                name = i.find("h3", class_="css-16kqa8y efwtv890").text

                price = i.find("span", class_="css-46itwz e162wx9x0").text.replace('\xa0', '')

                link = i.find("a",class_="g6gv8w4 g6gv8w8 _1ioeqy90").get("href")

                complect_part_1 = i.find_all("span",class_='css-1l9tp44 e162wx9x0')

                town = i.find("span",class_="css-1488ad e162wx9x0").text
                for y in complect_part_1:
                    complect_part_2 = y.text
                    complect_part_3 += complect_part_2



                # print(f"{name},цена:{price},комплектация:{complect_part_3 },город:{town},ссылка:{link}")

                yield (name,f"цена:{price}",f'комплектация:{complect_part_3 }',f'город:{town}',f'ссылка:{link}')
            except:
                continue







