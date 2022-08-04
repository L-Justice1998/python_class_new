# Creator:justice 廖振谊
# Creat time:2022/6/28 20:00
def access_check(func):
    def access_check_now():
        print("access check")
        func()
    return access_check_now

@access_check
def func():
    print("this is func needed to be checked")

func()