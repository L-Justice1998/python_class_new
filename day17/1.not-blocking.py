# Creator:justice 廖振谊
# Creat time:2022/6/17 19:35
import sys
import select
from socket import *

tcp_server=socket(AF_INET,SOCK_STREAM)
ipaddress,port=("192.168.1.38",2000)
tcp_server.bind((ipaddress,port))
tcp_server.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
tcp_server.setblocking(False)
tcp_server.listen(100)
client_socket=None
flag=True
while True:
    try:
        client_socket,_=tcp_server.accept()
    except:
        pass
    if client_socket:
        if flag:
            print("the connection established")
            flag=False
            client_socket.setblocking(False)
        try:
            data=client_socket.recv(100)
            if not data:
                print("the connection broke")
                exit()
            print(data.decode('utf8'))
            client_socket.close()
        except:
            if not flag:
                print("the connection broke")
                exit()
            pass
tcp_server.close()



