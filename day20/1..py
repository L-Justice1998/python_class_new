# Creator:justice 廖振谊
# Creat time:2022/6/21 22:08
import re
list1=['L,smith','L smith','j ustice','justice']
for name in list1:
    result=re.match('.*(,| ).*',name)
    if result:
        print(name,"is matched")
    else:
        print(name, "isn't matched")