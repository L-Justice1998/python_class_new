# Creator:justice 廖振谊
# Creat time:2022/6/17 20:18
from socket import *
import struct

tcp_client=socket(AF_INET,SOCK_STREAM)
ipaddress,port=("192.168.1.38",2000)
tcp_client.connect((ipaddress,port))

len_of_file_name=tcp_client.recv(4)

file_name=tcp_client.recv(struct.unpack("I",len_of_file_name)[0]).decode('utf-8')
print(file_name)
file=open(file_name,'wb')
len_of_file=tcp_client.recv(4)
file.write(tcp_client.recv(struct.unpack("I",len_of_file)[0]))
file.close()
tcp_client.close()

# tcp_client_socket = socket(AF_INET, SOCK_STREAM)
#
# # 本地IP地址和端口
# address = ('192.168.1.38', 2000)
#
# # 连接服务器
# tcp_client_socket.connect(address)
#
# # 先接文件名
# file_name_len = tcp_client_socket.recv(4)
# file_name = tcp_client_socket.recv(struct.unpack('I', file_name_len)[0])  # 接到文件名
#
# file = open(file_name.decode('utf8'), 'wb')
# # 接文件内容长度
# file_content_len = tcp_client_socket.recv(4)
# # 接文件内容
# file_content = tcp_client_socket.recv(struct.unpack('I', file_content_len)[0])
# # 写进去
# file.write(file_content)
# file.close()
# tcp_client_socket.close()


