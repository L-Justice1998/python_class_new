# Creator:justice 廖振谊
# Creat time:2022/6/20 21:50
from collections.abc import Iterable,Iterator
class MyIterator():
    def __init__(self,mylist):
        self.mylist=mylist
        self.current_index=0
    def __next__(self):
        if self.current_index<len(self.mylist.list):
            temp=self.mylist.list[self.current_index]
            self.current_index+=1
            return temp
        else:
            raise StopIteration
    def __iter__(self):
        return self

class Mylist():
    def __init__(self):
        self.list=[]
    def add(self,item):
        self.list.append(item)
    def __iter__(self):
        thisiter=MyIterator(self.list)
        return thisiter

newlist=Mylist()
newlist.add(1)
newlist.add(2)
newlist.add(3)
newiter=MyIterator(newlist)
print(next(newiter))
print(next(newiter))
print(next(newiter))
newiter1=MyIterator(newlist)
for item in newiter1:
    print(item)
