from socket import *
HOST = 'localhost' #服务器所在主机名
PORT = 21516 #与服务端相同的端口号
BUFIZ = 1024 #将缓冲区大小设置为1KB
ADDR = (HOST,PORT)

tcpCliSock=socket(AF_INET,SOCK_STREAM) #分配TCP客户端套接字
tcpCliSock.connect(ADDR)

while True:
    data = input('> ')
    if not data: #用户无输入，结束循环
        break
    tcpCliSock.send(bytes(data,"utf-8"))
    data = tcpCliSock.recv(BUFIZ)
    if not data: #服务器调用失败（无返回信息），结束循环
        break
    print(data.decode('utf-8'))
tcpCliSock.close()