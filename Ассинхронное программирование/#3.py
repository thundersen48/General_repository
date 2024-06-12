import socket
# domain:5000

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)# ipv4
"""Определяем опции, 1 Опция относится к уровню сокета"""
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
server_socket.bind(('localhost', 5001))
server_socket.listen()

while True:
    print('Мы находимся перед accept()')
    client_socket, addr = server_socket.accept()#Принимает входящие подключения, accept - это блокирующая операция
    print('Connection from', addr)

    while True:
        print('Мы находимся перед методом .recv()')
        request = client_socket.recv(4096)

        if not request:
            break
        else:
            response = 'Hello World\n'.encode()
            client_socket.sent(response)


