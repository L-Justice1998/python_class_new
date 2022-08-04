# Creator:justice 廖振谊
# Creat time:2022/6/4 17:46
def test():
    global num
    num=1
    print("执行test中的num是%d" %num)
num=0
print("执行test前的num是%d" %num)
test()
print("执行test后的num是%d" %num)