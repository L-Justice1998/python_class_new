# Creator:justice 廖振谊
# Creat time:2022/6/3 20:16
b=input("please input a integer")
a=(int)(b)
num=0
num1=64
temp=1
while num1!=0:
    if a&temp:
        num+=1
    temp*=2
    num1-=1
print("%s的二进制中1的个数为%d" %(b,num))
