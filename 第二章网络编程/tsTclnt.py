from socket import *

HOST = 'localhost'
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

tcpCliSock = socket(AF_INET, SOCK_STREAM)
tcpCliSock.connect(ADDR)

while True:
    data = input('> ')
    print(data)
    if not data:
        break
    print(data.encode('utf-8'))
    tcpCliSock.send(data.encode())
    data = tcpCliSock.recv(BUFSIZ).decode()
    if not data:
        break
    print(data)
tcpCliSock.close()
