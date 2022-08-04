# Creator:justice 廖振谊
# Creat time:2022/6/9 17:53
import os
f=open("first","r+")
f.write("life is short,I need python")
f.seek(0,os.SEEK_SET)
text=f.read()
print(text)
f.close()