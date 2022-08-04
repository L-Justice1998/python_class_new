# Creator:justice 廖振谊
# Creat time:2022/6/7 19:10
def is_symmetric(num):
    n=len(num)
    for i in range(n//2):
        if num[i]!=num[n-i-1]:
            raise Exception("Not Symmetric Integer")
try:
    num=int(input("please input a symmetric integer number:"))
    try:
        is_symmetric(str(num))
        print("you got a symmetric integer number %d"%num)
    except Exception as result:
        print(result)
except ValueError:
    print("you should input a integer number")

# def input_password():
#     pwd = input("请输入密码：")
#     if len(pwd) >= 8:
#         return pwd
#     print("主动抛出异常")
#     ex = Exception("密码长度不够")
#     raise ex
#
# try:
#     print(input_password())
# except Exception as result:
#     print(result)