# Creator:justice 廖振谊
# Creat time:2022/6/16 17:20
import socket
tcp_server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ipaddress="192.168.1.38"
port=2000
tcp_server.bind((ipaddress,port))
tcp_server.listen(10)
client_socket,_=tcp_server.accept()
recv_data=client_socket.recv(100)
print("the received data is")
print(recv_data.decode())
client_socket.send("我收到你的消息了".encode('utf8'))
client_socket.close()
tcp_server.close()
