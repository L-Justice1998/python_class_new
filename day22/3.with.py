# Creator:justice 廖振谊
# Creat time:2022/6/24 18:37
from contextlib import contextmanager
@contextmanager
def my_open(path,open_mode):
    f=open(path,open_mode,encoding='utf8')
    yield f
    f.close()

with my_open('file','w+') as f:
    f.write("I am going home!")