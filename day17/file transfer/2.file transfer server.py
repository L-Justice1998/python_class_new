# Creator:justice 廖振谊
# Creat time:2022/6/17 20:17
from socket import *
import struct
import time


tcp_server=socket(AF_INET,SOCK_STREAM)
tcp_server.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
ipaddress,port=("192.168.1.38",2000)
tcp_server.bind((ipaddress,port))
tcp_server.listen(100)
client_socket,client_addr=tcp_server.accept()
print(client_addr)

file_name='readme'
b_file_name=file_name.encode('utf8')
print(b_file_name)
len_of_file_name=struct.pack("I",len(b_file_name))
client_socket.send(len_of_file_name)
client_socket.send(b_file_name)

file=open(file_name,'rb')
b_text=file.read()
len_of_file=struct.pack("I",len(b_text))
client_socket.send(len_of_file)

client_socket.send(b_text)
print("finished")
file.close()
client_socket.close()
tcp_server.close()



# tcp_server_socket = socket(AF_INET, SOCK_STREAM)
#
# # 重用对应地址和端口
# tcp_server_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
#
# # 本地IP地址和端口
# address = ('192.168.1.38', 2000)
#
# tcp_server_socket.bind(address)
# # 端口激活
# tcp_server_socket.listen(100)
#
# client_socket, clientAddr = tcp_server_socket.accept()
# #连上了
# print(clientAddr)
#
# #发文件名
# file_name = "readme"
# #先发报文头--文件名的长度
# b_file_name =file_name.encode('utf-8')
# client_socket.send(struct.pack("I", len(b_file_name))) #发送文件名的长度
# client_socket.send(b_file_name) #发文件名
#
# #发文件内容
# file = open(file_name,"rb")
# text_bytes = file.read()
# client_socket.send(struct.pack("I", len(text_bytes))) #文件内容长度
# client_socket.send(text_bytes)  #文件内容
# file.close()
# time.sleep(5)
# client_socket.close()
# tcp_server_socket.close()