# Creator:justice 廖振谊
# Creat time:2022/6/16 19:36
import sys
import socket
import select

epoll_server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ipaddress="192.168.119.129"
port=2000
epoll_server.bind((ipaddress,port))
epoll_server.listen(10)

epoll=select.epoll()
epoll.register(sys.stdin.fileno(),select.EPOLLIN)#用户输入的内容的缓冲区
epoll.register(epoll_server.fileno(),select.EPOLLIN)#进程收到另一个进程信息的缓冲区
client_socket=None
while True:
    events=epoll.poll(-1,2)
    for fd,_ in events:
        if fd==epoll_server.fileno():
            client_socket,_=epoll_server.accept()
            epoll.register(client_socket.fileno(),select.EPOLLIN)
        elif fd==sys.stdin.fileno():
            data=input()
            if not client_socket:
                print("No one connects the server")
                continue
            client_socket.send(data.encode('utf8'))
        else:
            recv_data=client_socket.recv(100)
            if not recv_data:
                print("the connection broke")
                epoll.unregister(client_socket.fileno())
                exit()
                continue
            print(recv_data.decode('utf8'))

epoll_server.close()


