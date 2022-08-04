# Creator:justice 廖振谊
# Creat time:2022/6/22 0:50
import re
list1=['dfv321','afsd','243s','3452ert','t234']
for name in list1:
    result=re.match('^[0-9]+',name)
    if result:
        print(name,"is matched",",the match part is",result.group())
    else:
        print(name, "isn't matched")
