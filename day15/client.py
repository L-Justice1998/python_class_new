# Creator:justice 廖振谊
# Creat time:2022/6/15 15:41
import socket
client=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
destination_address=("192.168.1.38",23457)
client.sendto("This is client,and I am sending a message1 for you".encode('utf8'),destination_address)
client.sendto("This is client,and I am sending a message2 for you".encode('utf8'),destination_address)
recv_data=client.recvfrom(100)
print("This is the data receiving from %s,and the data is %s"%(recv_data[1],recv_data[0]))
client.close()