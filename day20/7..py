# Creator:justice 廖振谊
# Creat time:2022/6/22 1:26
import re
context="把邮件发到gdmmxiaolaohu@163.com上"
context1=re.sub('[0-9a-zA-Z_]{4,20}@.*\.com','378925221@qq.com',context)
print(context)
print(context1)
