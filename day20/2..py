# Creator:justice 廖振谊
# Creat time:2022/6/22 0:29
import re
list1=['http://www.yahoo.com','www.kdocs.cn/l/sqwbn3edhsxH.com','https://www.sysu.edu.cn/','justice']
for name in list1:
    result=re.match('(https?://)?((www.*\.com)$|.*(edu|net)$)',name)
    if result:
        print(name,"is matched")
    else:
        print(name, "isn't matched")
