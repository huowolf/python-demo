import os
print(os.name)

print(os.environ)

#查看当前目录的绝对路径
print(os.path.abspath('.'))

# 在当前目录下创建一个新目录，首先把新目录的完整路径表示出来:
newpath=os.path.join('.','testdir')
print(newpath)

#创建
#os.mkdir(newpath)

#删除
#os.rmdir(newpath)

#拆分路径
s=os.path.split('/Users/michael/testdir/file.txt')
print(s)

#获取文件拓展名
print(os.path.splitext('/Users/michael/testdir/file.txt')[1])

#列出当前目录下的所有目录
print([x for x in os.listdir('.') if os.path.isdir(x)])

#列出所有的.py文件
L=[x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py']
print(L)