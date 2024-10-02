import time

import requests as re
from bs4 import BeautifulSoup as bs
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import csv
from selenium.webdriver.common.by import By


#инициализация драйвера
driver = webdriver.Firefox()

#ссылка на сайт
driver.get("https://valvemon.ru/servers/cs/#/page/4")
scroll_vаlue = 3000 #кол-во пикселей сколько надо вниз
scroll_by = f'window.scrollTo(0, {scroll_vаlue});' #команда скрола страницы вниз

#сначала скролим страницу затем отсылаем BS
for i in range(1,6):
    scroll_by = f'window.scrollTo(0, {scroll_vаlue});'
    driver.execute_script(scroll_by)
    scroll_vаlue += 3000 # все ниже и ниже
    time.sleep(5) # ждем пока загрузиться сайт



header = {"User-agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:109.0) Gecko/20100101 Firefox/115.0"}

url = driver.page_source  # адрес из марионетки браузера

# response = re.get(url, headers=header)  #  если бы сайт был статичным работало бы это ПОЛНОЕ получение html с сайта
#                                            но request дает лишь часть контента
# print(response)

soup = bs(url,"lxml") #получаем код для BS

server_item = soup.find_all("div", class_="item server-preview") # ищем все карточки серверов






def generator(): # поиск названий ,айпи,карты,кол-ва игроков




        for i in server_item:



                server_name = i.find("span", class_="h2").text.replace("\t","").replace("\n","")  # получаем список названий серваков

                server_map = i.find('div', class_='block-seven server-list-map').text # получаем список названий карт

                server_ip = i.find('span', itemprop="alternateName").text # получаем список айпи

                server_value_players = i.find('div', class_='block-seven server-list-players').text # получаем список кол-ва игроков

#--------------------ОТЛАДОЧНАЯ ПЕЧАТЬ--------------------------

                print(server_name)

                print(server_map)

                print(server_ip)

                print(server_value_players)


                data = (server_name,server_map,server_ip,server_value_players)
                print (data)

# --------------------ОТЛАДОЧНАЯ ПЕЧАТЬ--------------------------

                with open('Servers.csv', 'a') as file:# формируем csv файл
                        CSwriter = csv.writer(file, dialect='excel')

                        CSwriter.writerow(data)




generator()
