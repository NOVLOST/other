import time

import requests as re
from bs4 import BeautifulSoup as bs
from time import sleep

import openpyxl
from openpyxl import load_workbook

page = 0
book_name = 'products.xlsx' # название книги
sheet_name = f'Лист{page}'
url_list = [f'https://techtiger.ru/catalog/podveska/',
            f'https://techtiger.ru/catalog/kuzovnye_detali/',
            f'https://techtiger.ru/catalog/optika/',
            f'https://techtiger.ru/catalog/avtostekla/',
            f'https://techtiger.ru/catalog/bachok_adsorbera/',
            f'https://techtiger.ru/catalog/vykhlopnaya_sistema/',
            f'https://techtiger.ru/catalog/zaglushka_bampera/',
            f'https://techtiger.ru/catalog/zaglushka_podkrylka/',
            f'https://techtiger.ru/catalog/zaglushka_ruchki_dveri/',
            f'https://techtiger.ru/catalog/zalivnaya_gorlovina/',
            f'https://techtiger.ru/catalog/zashchita_arki/',
            f'https://techtiger.ru/catalog/zashchita_radiatora/',
            f'https://techtiger.ru/catalog/katalizator/',
            f'https://techtiger.ru/catalog/koltso_uplotnitelnoe/',
            f'https://techtiger.ru/catalog/kontakt_startera/',
            f'https://techtiger.ru/catalog/masla_i_zhidkosti/',
            f'https://techtiger.ru/catalog/oprava_fary/',
            f'https://techtiger.ru/catalog/patrubok_korpusa_vozdushnogo_filtra/',
            f'https://techtiger.ru/catalog/petlya_kryshki_bagazhnika/',
            f'https://techtiger.ru/catalog/planka/',
            f'https://techtiger.ru/catalog/povorot_v_dver/',
            f'https://techtiger.ru/catalog/povorot_v_krylo/',
            f'https://techtiger.ru/catalog/prokladki/',
            f'https://techtiger.ru/catalog/pylezashchitnyy_komplekt/'
            f'https://techtiger.ru/catalog/rezonator_vozdushnogo_filtra_vlagootdelitel/',
            f'https://techtiger.ru/catalog/remkomplekt_podveski/',
            f'https://techtiger.ru/catalog/rulevoe_upravlenie/',
            f'https://techtiger.ru/catalog/saylentblok_komplekt/',
            f'https://techtiger.ru/catalog/uplotnitel_dveri/',
            f'https://techtiger.ru/catalog/uplotnitel_kapota/',
            f'https://techtiger.ru/catalog/filtry/',
            f'https://techtiger.ru/catalog/flanets_sistemy_okhlazhdeniya/',
            f'https://techtiger.ru/catalog/tsep_balansirovochnogo_vala/',
            f'https://techtiger.ru/catalog/tsep_maslonasosa/',
            f'https://techtiger.ru/catalog/elektronika/',
            f'https://techtiger.ru/catalog/transmissiya/',
            f'https://techtiger.ru/catalog/tormoza/',
            f'https://techtiger.ru/catalog/datchiki/',
            f'https://techtiger.ru/catalog/dvigatel/',
            f'https://techtiger.ru/catalog/zerkalo/',
            f'https://techtiger.ru/catalog/raznoe/',
            f'https://techtiger.ru/catalog/aksessuary/'
            ]

header = {
'Accept' : '*/*',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:134.0) Gecko/20100101 Firefox/134.0'}

for url in url_list:
    page += 1
    sheet_name = f'Лист{page}'

    print(url)
    response = re.get(url, headers=header)
    print(f'ответ сервера {response.status_code}')

    soup = bs(response.text, 'lxml')

    max_page_list = soup.find_all('a', class_='dark_link') # находим мак кол0во страниц
    max_page = max_page_list[-1].text
    print(f'максисмум страниц {max_page}')


    for i in range(1,int(max_page)):

            #сайт динамический но можно в гет запросах найти подобную строку и сделав подобную ссылку мы можем рабоать
            # с динамическим сайтом как с статикой
            url_new = url + f'filter/clear/apply/?PAGEN_1={i}&ajax_get=Y&AJAX_REQUEST=Y&bitrix_include_areas=N'

            print(url_new)
            response = re.get(url_new,headers=header)
            print(f'ответ сервера {response.status_code}')

            soup = bs(response.text, 'lxml')

            list_of_card = soup.find_all('div', class_='inner_wrap TYPE_1')


            for card in list_of_card:
                card_name = card.find('a', class_='dark_link js-notice-block__title option-font-bold font_sm').find(
                    'span')
                print(card_name.text)

                quantity_available = card.find('span', class_='value font_sxs').text
                print(quantity_available)

                price = card.find('span', class_='price_value').text + ' ₽' + '/шт'
                print(price)

                img = 'https://techtiger.ru' + card.find('img', class_="lazy img-responsive").get('src')
                print(img)

                wb = load_workbook(book_name)
                ws = wb[sheet_name]

                ws.append([
                    f"{card_name.text}",
                    f'{quantity_available}',
                    f'{price}',
                    f'{img}'
                ])
                wb.save(book_name)
                wb.close()
            time.sleep(5)



