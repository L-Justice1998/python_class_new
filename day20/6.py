# Creator:justice 廖振谊
# Creat time:2022/6/22 1:55
import re
contexts=["2022年06月22日01时55分是什么意思","你说30222年07月22日08时61分会发生什么"]
for context in contexts:
    result=re.search('\d+年(0[1-9]|1[0-2])月(0[1-9]|[1-2]\d)日([0-1]\d|2[0-3])时[0-5]\d分'
                    ,context)
    if result:
        print(context,"is matched",",and the match part is",result.group())