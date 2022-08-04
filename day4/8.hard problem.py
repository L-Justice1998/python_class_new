# Creator:justice 廖振谊
# Creat time:2022/6/3 21:01
arr=[3,3,5,5,4,6,7,7]
num=0
for i in arr:
    num^=i
temp=num&(-num)
a=0
b=0
for i in arr:
    if i&temp:
        a^=i
    else:
        b^=i
print("the two numbers appearing once in the array is %d and %d" %(a,b))