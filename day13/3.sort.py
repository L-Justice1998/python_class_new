# Creator:justice 廖振谊
# Creat time:2022/6/13 18:48
import random
from operator import itemgetter
from operator import attrgetter
arr=[random.randint(1,100) for i in range(10)]
print(arr)
arr1=sorted(arr)
print(arr1)

tuple_list=[(1,2,4),(1,2,3),(3,-1,2),(-1,3,1)]
print(tuple_list)
tuple_list1=sorted(tuple_list,key=lambda s:s[0])
print(tuple_list1)
tuple_list2=sorted(tuple_list,key=lambda s:s[1])
print(tuple_list2)
tuple_list3=sorted(tuple_list,key=itemgetter(2))
print(tuple_list3)
# 若没有涉及的排序 则稳定处理
tuple_list4=sorted(tuple_list,key=itemgetter(0,1))
print(tuple_list4)

mydict = { 'Li' : ['M',7],
 'Zhang': ['E',2],
 'Wang' : ['P',3],
 'Du' : ['C',2],
 'Ma' : ['C',9],
 'Zhe' : ['H',7]}
# items()的作用是为了让mydict变成元组后进行迭代
mydict1=sorted(mydict.items(),key=lambda x:x[0])
print(mydict1)
mydict2=sorted(mydict.items(),key=lambda x:x[1][1])
print(mydict2)

gameresult = [
{ "name":"Bob", "wins":10, "losses":3, "rating":75.00 },
{ "name":"David", "wins":3, "losses":5, "rating":57.00 },
{ "name":"Carol", "wins":4, "losses":5, "rating":57.00 },
{ "name":"Patty", "wins":9, "losses":3, "rating": 71.48 }]
gameresult1=sorted(gameresult,key=itemgetter("wins","rating"))
print(gameresult1)