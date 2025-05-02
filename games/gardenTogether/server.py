import socket


import pygame as py
import pygame.time


from classes.game_window_class import GameWin
from classes.player_class import Player

HOST = ("localhost",10000)
X_FIELD,Y_FIELD = 4000,4000
X_SERVER_WINDOW,Y_SERVER_WINDOW = 800,600
FPS = 100
START_POZ_X,START_POZ_Y = X_SERVER_WINDOW // 2,Y_SERVER_WINDOW // 2

main_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
main_socket.setsockopt(socket.IPPROTO_TCP,socket.TCP_NODELAY, 1)# отключает отправку пакетами(алгоритм нейгла) так как она замедляет передачу данных
main_socket.bind(HOST)
main_socket.setblocking(False) #сообщает сокету что не нужно ждать пока все игроки отправят данные
main_socket.listen(5) #кол-во людей которые могут подключиться одновременно

#создание окна
py.init()
game_window = GameWin(X_SERVER_WINDOW,Y_SERVER_WINDOW)
clock = pygame.time.Clock()
players = []
server_loop_bool = True

while server_loop_bool:
    clock.tick(FPS)
    #проверка на новые подключения
    try:
        new_socket,addres = main_socket.accept()
        print(f"connected:{addres}",)
        new_socket.setblocking(False)
        new_player = Player(new_socket,addres,START_POZ_X,START_POZ_Y,"image/cowboy.png")
        players.append(new_player)
    except:
        pass
    #чтение данных от пользователей
    for player in players:
        try:
            data = player.connection.recv(1024)
            data = data.decode()
            print(f"data:{data}")
        except:
            pass
    #обработка данных от пользователей

    #отправка данных пользователям
    for player in players:
        try:
            player.connection.send('new game data'.encode())
            player.connection_errors = 0
        except:
            player.connection_errors += 1
            if player.connection_errors == 500:
                player.connection.close()
                players.remove(player)
    #рисуем состояние комнаты
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            server_loop_bool = False

py.quit()
main_socket.close()
