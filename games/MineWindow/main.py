import sys

import pygame as py


# инициализайция игры
py.init()

#иницилизация звука
py.mixer.init()

#добавление звука в игру
# py.mixer.music.load("sounds/stone3.mp3")
# py.mixer_music.load("sounds/29990.mp3")
# py.mixer.music.load("music/C418 - Sweden.mp3")
"""Нафига тогда строки выше если и так все ок?"""


stone_sound = py.mixer.Sound("sounds/stone3.mp3")
dern_sound = py.mixer.Sound("sounds/29990.mp3")
sweden = py.mixer.Sound("music/C418 - Sweden.mp3")
#создание игрового окна
game_window = py.display.set_mode((800,600))

#Координаты курсора
mouse_cor = None



#цвет фона
color = (207, 198, 174)

#цвета текста
RED = (255, 0, 0)
ORANGE = (242, 178, 5)
YELLOW = (208, 224, 22)
GREEN = (35, 224, 22)
BLUE = (190, 188, 245)
DARK_BLUE = (23, 15, 250)
PURPLE = (213, 4, 224)

color_text = (RED,ORANGE,YELLOW,GREEN,BLUE,DARK_BLUE,PURPLE)
#счетчик
count_color_text = 0
#шрифт размером 32
font = py.font.Font(None,32)

#тумблер для звука
play_choise = True

sweden.play(-1)

#флаг часов
clock=False

#
time = py.time

#
last_time = 0

#основной цикл игры
while True:

    if clock:
        count_color_text += 1

    #костыль если счетчик больше 7 то он обнуляется чтобы не словить out of range
    if count_color_text == 7:
        count_color_text = 0

    for event in py.event.get():
        #условие выхода из игры
        if event.type == py.QUIT:
            sys.exit()
        #фиксируем нажатие клавиши
        if event.type == py.MOUSEBUTTONUP:
            mouse_cor = py.mouse.get_pos()

            # воспроизведение звука
            if play_choise == True:
                stone_sound.play()
                play_choise = False

            else:
                dern_sound.play()
                play_choise = True



    #рендер текста
    text = font.render("IXTIC",False, color_text[count_color_text]  )

    #заполнение фона цветом
    game_window.fill(color)

    # #Задержка
    # py.time.delay(300)

    #написание текста
    #NOTE: важно сначала заполнить фон затем текст
    game_window.blit(text, ((game_window.get_width() -  text.get_width()   ) // 2
                        ,( game_window.get_height() - text.get_height() ) // 2) )

    #Рамка для текста
    py.draw.rect(game_window,color_text[6 - count_color_text], ((game_window.get_width() - text.get_width() ) //2 - 10 ,
                 (game_window.get_height() - text.get_height() ) //2 - 10
                ,text.get_width() +20 , text.get_height() +20 ), 3)

    #Картинка
    if mouse_cor != None:
        game_window.blit(py.image.load("image/dern.png"),(mouse_cor[0] - 16 , mouse_cor[1] - 16))



    else:
        game_window.blit(py.image.load("image/dern.png"), (game_window.get_width() // 2 - 16,
                                                           (game_window.get_height() - text.get_height()) / 2 - 64))




    #обновление экрана
    py.display.flip()

    #сброс флага
    clock = False

    #
    real_time = time.get_ticks()

    if real_time - last_time > 1000:
        last_time = real_time
        clock = True



