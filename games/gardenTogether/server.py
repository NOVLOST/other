import socket
import time
host = ("localhost",10000)

main_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
main_socket.setsockopt(socket.IPPROTO_TCP,socket.TCP_NODELAY, 1)# отключает отправку пакетами(алгоритм нейгла) так как она замедляет передачу данных
main_socket.bind(host)
main_socket.setblocking(False) #сообщает сокету что не нужно ждать пока все игроки отправят данные
main_socket.listen(5) #кол-во людей которые могут подключиться одновременно

players_sockets = []

while True:
    #проверка на новые подключения
    try:
        new_socket,addres = main_socket.accept()
        print(f"connected:{addres}",)
        main_socket.setblocking(False)
        players_sockets.append(new_socket)
    except:
        print("no new connection")
    #чтение данных от пользователей
    for socket in players_sockets:
        try:
            data = socket.recv(1024)
            data = data.decode()
            print(f"data:{data}")
        except:
            pass
    #обработка данных от пользователей

    #отправка данных пользователям
    for socket in players_sockets:
        try:
            socket.send('new game data'.encode())
        except:
            players_sockets.remove(socket)
            socket.close()
            print("socket closed")
    time.sleep(1)