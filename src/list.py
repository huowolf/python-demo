#列表生成式
L=[x*x for x in range(1,11)]
print(L)

#筛选
L=[x*x for x in range(1,11) if x%2==0]
print(L)

#两层循环
L=[m+n for m in'ABC' for n in 'XYZ']
print(L)

#列出当前目录下的所有文件和目录名
import os
print([d for d in os.listdir('.')])

#使用两个变量的列表生成式
d={'Asia':'亚洲','Africa':'非洲','Europe':'欧洲'}
L=[k+"="+v for k,v in d.items()]
print(L)

#把一个list中所有的字符串变成小写
L = ['Hello', 'World', 'IBM', 'Apple']
L = [s.lower() for s in L] 
print(L)
