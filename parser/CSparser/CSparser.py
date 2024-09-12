import requests as re
from bs4 import BeautifulSoup as bs
from time import sleep
import csv

header = {"User-agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:109.0) Gecko/20100101 Firefox/115.0"}

url = f'https://valvemon.ru/servers/cs/#/page/4'  # адрес

response = re.get(url, headers=header)  # получение html с сайта

print(response)

soup = bs(response.text, "lxml")

server_item = soup.find_all("div", class_="item server-preview")






def generator():




        for i in server_item:



                server_name = i.find("span", class_="h2").text.replace("\t","").replace("\n","")  # получаем список названий серваков

                server_map = i.find('div', class_='block-seven server-list-map').text

                server_ip = i.find('span', itemprop="alternateName").text

                server_value_players = i.find('div', class_='block-seven server-list-players').text

                print(server_name)

                print(server_map)

                print(server_ip)

                print(server_value_players)


                data = (server_name,server_map,server_ip,server_value_players)
                print (data)


                with open('Servers.csv', 'a') as file:
                        CSwriter = csv.writer(file, dialect='excel')

                        CSwriter.writerow(data)




generator()