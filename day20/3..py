# Creator:justice 廖振谊
# Creat time:2022/6/22 0:47
import re
list1=['dfv321','afsd','243s']
for name in list1:
    result=re.match('^[a-zA-Z]+',name)
    if result:
        print(name,"is matched")
    else:
        print(name, "isn't matched")
