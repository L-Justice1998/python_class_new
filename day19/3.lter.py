# Creator:justice 廖振谊
# Creat time:2022/6/20 21:23
from collections.abc import Iterable,Iterator
list1=[]
tuple1=(1,)
set1=()
dict1={'1':'a'}
print(isinstance(list1,Iterator))
print(isinstance(list1,Iterable))
print(isinstance(tuple1,Iterator))
print(isinstance(tuple1,Iterable))
print(isinstance(set1,Iterator))
print(isinstance(set1,Iterable))
print(isinstance(dict1,Iterator))
print(isinstance(dict1,Iterable))
