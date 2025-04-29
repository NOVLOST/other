import socket

host = ("localhost",10000)
client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client_socket.setsockopt(socket.IPPROTO_TCP,socket.TCP_NODELAY, 1)# отключает отправку пакетами(алгоритм нейгла) так как она замедляет передачу данных
client_socket.connect(host)

while True:
    #чтение команды

    #отправка команды на сервер
    client_socket.send("hello! I am client".encode())

    #получение данных от сервера
    data = client_socket.recv(1024)
    data = data.decode()

    #отрисовка новых данных
    print(f"data_client:{data}")

