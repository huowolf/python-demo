from collections import namedtuple,deque,defaultdict,OrderedDict,Counter,ChainMap

# namedtuple('名称', [属性list]):
Point=namedtuple('Point', ['x','y'])
p=Point(1,2)
print(p.x)
print(p.y)
print(isinstance(p, Point))
print(isinstance(p, tuple))

#deque:双端列表
q=deque(['a','b','c'])
q.append('x')
q.appendleft('y')
print(q)
q.pop()
print(q)
q.popleft()
print(q)

#保留最后N个元素
d=deque([1,2,3],maxlen=3)
d.append(4)
print(d)

#defaultdict
#key不存在时，返回一个默认值
#可调用函数作为初始化函数参数
dd=defaultdict(lambda:'N/A')
dd['key1']='abc'
print(dd['key1'])
#key2不存在
print(dd['key2'])

#类型名称作为初始化函数参数
ddd=defaultdict(int)
ddd['key']=12
print(ddd['key'])
print(ddd['key1'])

#OrderedDict的Key会按照插入的顺序排列
od=OrderedDict(a=1,b=2,c=3)
print(od)

od=OrderedDict()
od['z']=1
od['y']=2
od['x']=3
print(list(od.keys()))


'''
Remove and return a (key, value) pair from the dictionary.
Pairs are returned in LIFO order if last is true or FIFO order if false.

popitem(self, last=True)
'''
#last为True是LIFO,即为栈，反之是FIFO，即为队列
#默认last为True，默认表现为栈
#栈：后进先出，所以是弹出最后加入的那个元素
print(od.popitem())             #('x', 3)
#对列：先进先出，所以是弹出最先加入的那个元素
print(od.popitem(last=False))   #('z', 1)

#Counter是一个简单的计数器
c=Counter()
for ch in 'programming':
    c[ch]=c[ch]+1
print(c)
print(c['p'])
#获取列表出现次数最多的元素
c = Counter('abracadabra')
print(c.most_common(3))


#合并多个字典或映射
a = {"x": 1, "y": 2}
b = {"y": 3, "z": 4}
#ChainMap在将这些字典进行合并“操作”时，遇到相同的键，那么第一次映射的值将会被返回
c=ChainMap(a,b)
print(list(c.keys()))
print(list(c.values()))
for k,v in c.items():
    print(k,v)
#原字典的数据发生了改变，会映射到ChainMap
a['x']=5
print(a)
print(c)
print(c['x'])