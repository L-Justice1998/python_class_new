# Creator:justice 廖振谊
# Creat time:2022/6/28 19:40
def line(a,b):
    def create_y(x):
        print(a*x+b)
    return create_y

line1=line(3,2)
line1(2)
line2=line(4,2)
line2(2)
