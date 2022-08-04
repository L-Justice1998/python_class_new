# Creator:justice 廖振谊
# Creat time:2022/6/22 1:22
import re
list1=['dfv321','afsd','243s','3452ert','t234','那种是z,','   f   ']
for name in list1:
    result=re.match('.*?([0-9a-zA-Z]).*?',name)
    if result:
        print(name,"is matched",",the match part is",result.group(1))
    else:
        print(name, "isn't matched")