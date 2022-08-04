# Creator:justice 廖振谊
# Creat time:2022/6/9 18:10
f=open("Readme","r+",encoding='utf8')
text=f.read()
f1=open("Readme1","w+",encoding='utf8')
f1.write(text)
text1=f1.read()
print(text1)