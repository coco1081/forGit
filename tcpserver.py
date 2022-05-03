from socket import *
from time import ctime

HOST = '' #表示可以使用任何可用的地址。
PORT = 21516 #选择一个端口号
BUFSIZ = 1024 #将缓冲区大小设置为1KB
ADDR = (HOST, PORT)

tcpSerSock=socket(AF_INET,SOCK_STREAM) #分配TCP服务器的套接字
tcpSerSock.bind(ADDR) #将套接字绑定到服务器地址
tcpSerSock.listen(5) #开启TCP监听器的调用

try:
    while True:
        #进入服务器的无限循环中，被动等待客户端的连接
        print('Waiting for connection……')
        tcpCliSock, adrr = tcpSerSock.accept() #收到请求才向下走
        print('...Connected from:', ADDR)
        while True:
            data = tcpCliSock.recv(BUFSIZ)
            if not data: #若服务器退出调用，跳出循环，回到等待请求
                break
            tcpCliSock.send(bytes('[%s] %s' % (ctime(),data.decode("utf-8")),"utf-8"))
        tcpCliSock.close()
except KeyboardInterrupt:
    print("Connection closed.")
    tcpSerSock.close()
except Exception as e:
    print(e)
    tcpSerSock.close()