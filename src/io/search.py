#编写一个程序，能在当前目录以及当前目录的所有子目录下查找文件名包含指定字符串的文件，并打印出相对路径
import os

s=input("search text:")
def get_path(s,paths='.'):
    for root,dirs,files in os.walk(paths):
        # 返回的是一个三元组(root,dirs,files)。
        # root 所指的是当前正在遍历的这个文件夹的本身的地址
        # dirs 是一个 list ，内容是该文件夹中所有的目录的名字(不包括子目录)
        # files 同样是 list , 内容是该文件夹中所有的文件(不包括子目录)
        #print(roots)
        #print(dirs)
        #print(files)
        #print("----------------")
        
        for file in files:
            if s in file:
                print(os.path.join(root,file))

get_path(s)