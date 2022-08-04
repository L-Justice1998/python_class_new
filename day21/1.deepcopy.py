# Creator:justice 廖振谊
# Creat time:2022/6/22 20:25
import copy

a=[1,2,3,4]
b=a
print(a is b)
a[0]=5
print(a is b)
print('*'*50)
a=[1,2,3,4]
b=copy.copy(a)
print(a is b)
a[0]=5
print(a is b)
print('*'*50)
a=[1,2]
b=[3,4]
c=[a,b]
d=copy.copy(c)
print(c is d)
d[0][0]=5
print(a)
print('*'*50)
a=[1,2]
b=[3,4]
c=[a,b]
d=copy.deepcopy(c)
print(c is d)
d[0][0]=5
print(a)