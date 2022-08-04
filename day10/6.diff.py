# Creator:justice 廖振谊
# Creat time:2022/6/9 18:56
import os

def dfs_dir(path_name,width):
    file_name=os.listdir(path_name)
    for file in file_name:
        print(' '*width+file)
        current_path=path_name+'/'+file
        if os.path.isdir(current_path):
            dfs_dir(current_path,width+4)
dfs_dir("D:\python班\python项目",0)