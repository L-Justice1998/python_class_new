# Creator:justice 廖振谊
# Creat time:2022/6/28 20:13
def deco1(func):
    print("this is deco1")
    def deco10():
        print("this is deco10")
        func()
    return deco10

def deco2(func):
    print("this is deco2")
    def deco20():
        print("this is deco20")
        func()
    return deco20
@deco1
@deco2
def func():
    print("this is func")

func()