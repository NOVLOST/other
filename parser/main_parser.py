import requests as re
from bs4 import BeautifulSoup as bs
from time import sleep

header = {"User-agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:109.0) Gecko/20100101 Firefox/115.0"}

def downloader(url):
    resp = re.get(url , stream=True)
    r  = open(r"C:\Users\SYXAЧ\Desktop\флэшка\image" + url.split("/")[-1] , "wb")
    for part in resp.iter_content(1024*1024):
        r.write(part)
    r.close()


def geter_url():

    for i in range(1,6):

        url = f"https://scrapingclub.com/exercise/list_basic/?page={i}"

        response = re.get(url,headers=header)



        soup = bs(response.text, "lxml")

        data = soup.find_all("div", class_="w-full rounded border")


        for el in data :
            #!!!ЭТА ЧАСТЬ НУЖНА ТОЛЬКО ДЛЯ ВНУТРЯНКИ!!!

            card_url = "https://scrapingclub.com" + el.find("a").get("href")


            #---------------------------
            #превью карточек с товаром
            #---------------------------

            # card = el.find("div",class_="p-4")
            #
            # clot_tag = card.find("h4").text.replace("\n","")
            #
            # clot_price = card.find("h5").text.replace("h5","")
            #
            # clot_img = "https://scrapingclub.com" + el.find("img", class_="card-img-top img-fluid").get("src")
            #
            #
            # print(f"название {clot_tag}\nцена {clot_price} \nкартинка {clot_img}\n ")





            yield card_url
def card_maker():
    for card in geter_url():
        sleep(1)
        #---------------------------
        #внутренняя карточка товара
        #---------------------------

        response = re.get(card, headers=header)

        soup = bs(response.text, "lxml")

        data = soup.find("div", class_="my-8 w-full rounded border")

        img = "https://scrapingclub.com"  + data.find("img",class_="card-img-top").get("src")

        name = data.find("h3",class_='card-title').text.replace('h3','')

        price = data.find('h4' , class_='my-4 card-price').text.replace('h4','')

        descript = data.find('p',class_='card-description').text.replace('p','')

        downloader(img)
        yield (name,price,descript,img)
