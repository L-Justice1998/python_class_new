# Creator:justice 廖振谊
# Creat time:2022/6/16 18:37
import socket

tcp_client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ipaddress="192.168.1.38"
port=2000
tcp_client.connect((ipaddress,port))
tcp_client.send("我给你发信息了".encode('utf8'))
recv_data=tcp_client.recv(100)
print("the received data is")
print(recv_data.decode())
tcp_client.close()
