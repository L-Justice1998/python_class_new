# Creator:justice 廖振谊
# Creat time:2022/6/20 22:53
import re
result=[]
list=['bat','bit', 'but', 'hat', 'hit', 'hut']
for word in list:
    result=re.match('[bh][aiu]t',word)
    print(result.group())