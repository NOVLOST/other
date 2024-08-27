import sys

import pygame as py

from player_class import Player
from plant_class import Plant
from game_window_class import GameWin


#NOTE:переделать размеры картинок и сделать чтобы они росли по часам мб передлать на другие спрайты.
#очки за сбор растений ,переписать объектно границу карты.Сделать инвентарь :D и магаз сделать хочется:P

#флаг часов
clock=False
once = True
#время
time = py.time

#разница вовремени
last_time = 0
last_time_use = 0

# инициализайция игры
py.init()

#иницилизация звука
py.mixer.init()

#создание игрового окна
game_window = GameWin(800,600,"image/background__clear.gif",255,255,0)



# background = py.image.load("image/background__clear.gif").convert_alpha()

#стартовая позиция игрока
poz_x = 100
poz_y = 100


#объект игрока
joe = Player(poz_x,poz_y,'image/cowboy.png')

#инициализация растения


#флаг клавиши использования
use_key = False

#список растений которые посадил игрок
plats_list = []

check_plants = 0

while True :


    for event in py.event.get():
        #условие выхода из игры
        if event.type == py.QUIT:
            sys.exit()
    key = py.key.get_pressed()
    if clock == True:
        if key[py.K_w]:
            joe.last_coor_y = joe.coordinate_Y
            joe.coordinate_Y -= 4

        if key[py.K_s]:
            joe.last_coor_y = joe.coordinate_Y
            joe.coordinate_Y += 4


        if key[py.K_d]:
            joe.last_coor_x = joe.coordinate_X
            joe.coordinate_X += 4

        if key[py.K_a]:
            joe.last_coor_x = joe.coordinate_X
            joe.coordinate_X -= 4

        if key[py.K_e]:
            use_key = True



            coordinate_X = (joe.coordinate_X + 100) - (joe.coordinate_X % 100)
            coordinate_Y = (joe.coordinate_Y + 100) - (joe.coordinate_Y % 100)

            if once == True:
                poted_grass = Plant(coordinate_X, coordinate_Y, 0, 1)
                once = False
                plats_list.append(poted_grass)
            for el in plats_list:
                if coordinate_Y == el.coordinate_Y and coordinate_X == el.coordinate_X:

                    check_plants += 1
                    if check_plants != 0:
                        break
            if check_plants == 0:
                poted_grass = Plant(coordinate_X, coordinate_Y, 0, 1)
                plats_list.append(poted_grass)
                check_plants = 0
            else:
                check_plants = 0




                #фон отрисовка
    game_window.display_set_mode.blit(game_window.background, (0, 0))

    # рисуем коллизию игрока
    joe_rect = joe.avatar.get_rect(topleft = (joe.coordinate_X  ,joe.coordinate_Y))
    scope = py.draw.rect(game_window.display_set_mode, (255, 255, 0), ((joe.coordinate_X + 100) - (joe.coordinate_X % 100), (joe.coordinate_Y + 100) - (joe.coordinate_Y % 100), 20, 20),3)


    #==================================================
    #                                                ||
    #               отрисовка растений               ||
    #                                                ||
    #==================================================
    if use_key == True:
        for el in plats_list:
            #ограничение на два первых столба
            if el.coordinate_X >= 300:

                game_window.display_set_mode.blit(el.skin,(el.coordinate_X, el.coordinate_Y))

                # if el.show.colliderect(el.show):
                #     plats_list.remove(el)

                if el.show.colliderect(scope):

                    if key[py.K_q]:
                        if el.skin_index == 12:
                            joe.score += 100
                        plats_list.remove(el)

            else:
                continue

    game_window.border_right = py.draw.line(game_window.display_set_mode, (255, 255, 0), (800, 0), (800, 600), 3)
    game_window.border_left = py.draw.line(game_window.display_set_mode, (255, 255, 0), (0, 0), (0, 600), 3)
    game_window.border_up = py.draw.line(game_window.display_set_mode, (255, 255, 0), (0, 0), (800, 0), 3)
    game_window.border_down = py.draw.line(game_window.display_set_mode, (255, 255, 0), (0 , 600), (800, 600), 3)




    if joe_rect.colliderect(game_window.border_right):
        joe.coordinate_X = joe.last_coor_x
        joe.coordinate_Y = joe.last_coor_y
    if joe_rect.colliderect(game_window.border_left):
        joe.coordinate_X = joe.last_coor_x
        joe.coordinate_Y = joe.last_coor_y
    if joe_rect.colliderect(game_window.border_up):
        joe.coordinate_X = joe.last_coor_x
        joe.coordinate_Y = joe.last_coor_y
    if joe_rect.colliderect(game_window.border_down):
        joe.coordinate_X = joe.last_coor_x
        joe.coordinate_Y = joe.last_coor_y
    # персонаж отрисовка

    game_window.display_set_mode.blit(joe.avatar, (joe.coordinate_X, joe.coordinate_Y))
    #прицел
    scope = py.draw.rect(game_window.display_set_mode, (255, 255, 0), ((joe.coordinate_X + 100) - (joe.coordinate_X % 100), (joe.coordinate_Y + 100) - (joe.coordinate_Y % 100), 20, 20),3)

    #счетчик очков игрока
    game_window.display_set_mode.blit(joe.font.render(f"Score:{joe.score}",False, 'white'  ),(50,50))
    # обновление экрана
    py.display.update()

    # сброс флага
    clock = False

    #настоящее время с часов
    real_time = time.get_ticks()

    #сравниваем разницу во времени
    if real_time - last_time > 10:
        last_time = real_time
        clock = True



    for el in plats_list:
        if el.skin_index != 12:

            if  el.grow_time == 100:
                el.grow_time = 0
                el.skin_index += 1

            if el.skin_index == 12:
                el.skin_index = 12
        el.grow_time += 1
        new_el = Plant(el.coordinate_X,el.coordinate_Y,el.grow_time,el.skin_index)
        plats_list.remove(el)
        plats_list.append(new_el)

