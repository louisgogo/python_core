from socket import *
from time import ctime

HOST = ''
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

tcpSerSock = socket(AF_INET, SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)  # 在连接被转接和拒绝前，传入连接请求的最大数

while True:
    print('waiting fro connection...')
    tcpCliSock, addr = tcpSerSock.accept()
    print('...connected from:', addr)

    while True:
        data = tcpCliSock.recv(BUFSIZ).decode()
        print(data)
        if not data:
            break
        print(('[%s] %s' % (ctime(), data)).encode())
        tcpCliSock.send(('[%s] %s' % (ctime(), data)).encode())

    tcpCliSock.close()
tcpSerSock.close()
