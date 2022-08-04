# Creator:justice 廖振谊
# Creat time:2022/6/17 19:48
from socket import *
import sys
import select

tcp_client=socket(AF_INET,SOCK_STREAM)
ipaddress,port=("192.168.1.38",2000)
tcp_client.connect((ipaddress,port))
tcp_client.send("我给你发信息了".encode('utf8'))
tcp_client.close()