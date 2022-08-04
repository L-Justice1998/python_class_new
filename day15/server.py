# Creator:justice 廖振谊
# Creat time:2022/6/15 15:08
import socket
server=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
local_address=("",23457)
server.bind(local_address)
recv_data=server.recvfrom(100)
recv_data1=server.recvfrom(100)
server.sendto("This is server,and I am sending a message for you".encode('utf8'),recv_data[1])
print("This is the data receiving from %s,and the data is %s"%(recv_data[1],recv_data[0]))
print("This is the data1 receiving from %s,and the data is %s"%(recv_data1[1],recv_data1[0]))
server.close()