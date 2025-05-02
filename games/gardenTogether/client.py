import socket


import pygame as py
from classes.game_window_class import GameWin
from classes.player_class import Player

#подключение к серверу
SCREEN_X, SCREEEN_Y = 800,600
HOST = ("localhost",10000)
client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client_socket.setsockopt(socket.IPPROTO_TCP,socket.TCP_NODELAY, 1)# отключает отправку пакетами(алгоритм нейгла) так как она замедляет передачу данных
client_socket.connect(HOST)

#создание окна игры
py.init()
game_window = GameWin(SCREEN_X,SCREEEN_Y)
py.display.set_caption("GardenTogether")
#объект игрока
#стартовая позиция игрока
start_poz_x,start_poz_y = SCREEN_X // 2,SCREEEN_Y // 2
joe = Player(new_socket,addres,START_POZ_X,START_POZ_Y,"image/cowboy.png")

loop_bool = True
while loop_bool:
    #обработка событий
    for event in py.event.get():
        if event.type == py.QUIT:
            loop_bool = False

    key = joe.key
   # if clock == True:
    joe.vector = [0, 0]


    if key[py.K_w]:

            joe.last_coor_y = joe.coordinate_Y
            joe.coordinate_Y -= 4
            joe.vector[1] -= 4

    if key[py.K_s]:
            joe.last_coor_y = joe.coordinate_Y
            joe.coordinate_Y += 40
            joe.vector[1] += 4

    if key[py.K_d]:
            joe.last_coor_x = joe.coordinate_X
            joe.coordinate_X += 40
            joe.vector[0] += 4

    if key[py.K_a]:
            joe.last_coor_x = joe.coordinate_X
            joe.coordinate_X -= 40
            joe.vector[0] -= 4

    if key[py.K_e]:
            use_key = True

    #отправка команды на сервер
    #FIXME: как не отправлять одни и теже данные на сервак?
    if joe.vector[0] != 0 and joe.vector[1] != 0:
        data_to_server = f'<{joe.vector[0]},{joe.vector[1]}>'
        client_socket.send(data_to_server.encode())


    #получение данных от сервера
    data = client_socket.recv(1024)
    data = data.decode()

    #отрисовка новых данных
    print(f"data_client:{data}")

    game_window.display_set_mode.fill("green")

    game_window.display_set_mode.blit(joe.avatar, (joe.coordinate_X, joe.coordinate_Y))
    py.display.update()
py.quit()

