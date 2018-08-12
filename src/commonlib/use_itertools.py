from itertools import count,takewhile,islice,repeat,chain,accumulate,groupby,\
    compress,combinations
import operator

#count(初值=0, 步长=1)
natuals=count(1)
#通过takewhile()等函数根据条件判断来截取出一个有限的序列
ns=takewhile(lambda x:x<=10,natuals)
print(list(ns))

#从10开始，到20结束，步长是2
for i in count(10,2):
    if i>20:
        break
    else:
        print(i,end=' ')

print('\n----------')

#从 10 开始，输出 5 个元素后结束
for i in islice(count(10),5):
    print(i)

re=repeat('ABC',3)
for i in re:
    print(i)
    
#可终止的迭代器
#accumulate(可迭代对象[, 函数])
#返回累计求和结果
#===============================================================================
# 0+1=1
# 1+2=3
# 3+3=6
# 6+4=10
#===============================================================================
print(list(accumulate(range(10))))
#===============================================================================
# 1*2=2
# 2*3=6
# 6*4=24
# 24*5=120
#===============================================================================
print(list(accumulate(range(1, 6), operator.mul)))  

#chain 迭代器能够将多个可迭代对象合并成一个更长的可迭代对象
for c in chain('ABC','XYZ'):
    print(c)

#groupby()把迭代器中相邻的重复元素挑出来放在一起
for key,group in groupby('AAABBBCCAAA'):
    print(key,list(group))
    
print('----------------------')
#忽略大小写分组
for key,group in groupby('AaaBBbcCAAa',lambda c:c.upper()):
    print(key,list(group))
    
#compress(数据, 选择器)
# 子模块 compress 在用一个可迭代对象过滤另一个可迭代对象时十分有用。
# 这是通过将作为选择器的可迭代对象取为布尔值列表来实现的。
letters = 'ABCDEFG'
bools = [True, False, True, True, False]
print(list(compress(letters, bools)))

#组合生成器
#combinations(可迭代对象, r)
#combinations 能够让你通过有一定长度的可迭代对象创建一个迭代器。
print(list(combinations('WXYZ', 2)))

for item in combinations('WXYZ',2):
    print(''.join(item))