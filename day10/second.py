# Creator:justice 廖振谊
# Creat time:2022/6/9 18:06
f=open("PRML","r+",encoding='utf8')
while True:
    text=f.readline()
    if not text:
        break
    print(text,end='')
f.close()
