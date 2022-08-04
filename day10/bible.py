# Creator:justice 廖振谊
# Creat time:2022/6/9 19:56
import os
def handle_line(text):
    text1=''
    for current in text:
        if not (65 <= ord(current) <= 90 or 48 <= ord(current) <= 57 or 97 <= ord(current) <= 122):
            text1+=' '
        elif 65 <= ord(current) <= 90:
            text1+=chr(ord(current)+32)
        else:
            text1+=current
    return text1

f=open("D:\python班\python项目\day10\The_Holy_Bible.txt","r+")
f1=open("The_Holy_Bible_new.txt","w+")
while True:
    text = f.readline()
    if not text:
        break
    f1.write(handle_line(text))





