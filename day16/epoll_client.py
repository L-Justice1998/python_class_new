# Creator:justice 廖振谊
# Creat time:2022/6/16 20:02
import sys
import socket
import select

epoll_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ipaddress = "192.168.1.38"
port = 2000
epoll_client.connect((ipaddress, port))

epoll = select.epoll()
epoll.register(sys.stdin.fileno(), select.EPOLLIN)  # 用户输入的内容的缓冲区
epoll.register(epoll_client.fileno(), select.EPOLLIN)  # 进程收到另一个进程信息的缓冲区
while True:
    events = epoll.poll(-1, 2)
    for fd, _ in events:
        if fd == sys.stdin.fileno():
            data = input()
            epoll_client.send(data.encode('utf8'))
        else:
            recv_data = epoll_client.recv(100)
            if not recv_data:
                print("the connection broke")
                exit()
                continue
            print(recv_data.decode('utf8'))

epoll_client.close()