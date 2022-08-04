# Creator:justice 廖振谊
# Creat time:2022/6/28 19:49
x=300

def change():
    x=200
    def change1():
        nonlocal x
        print("x is",x)
    return change1
ob=change()
ob()
