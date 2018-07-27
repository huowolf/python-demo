#利用特殊函数定制类

#__str__ , __repr__
class Student(object):
    def __init__(self,name):
        self.name=name
    
    def __str__(self):
        return 'Student Object(name:%s)' % self.name
        
    __repr__=__str__
    
        
print(Student('zhangsan'))

s= Student('lisi')
print(s)


#__iter__
class Fib(object):
    def __init__(self):
        self.a,self.b=0,1    # 初始化两个计数器a，b
        
    def __iter__(self):
        return self          # 实例本身就是迭代对象，故返回自己
    
    def __next__(self):
        self.a,self.b=self.b,self.a+self.b
        if self.a>100000:   # 退出循环的条件
            raise StopIteration
        return self.a       # 返回下一个值
    

for n in Fib():
    print(n)
    

# __getitem__(self,key):返回键对应的值。
class Fib2(object):
    def __getitem__(self,n):
        a,b=1,1
        for x in range(n):
            a,b=b,a+b
        return a
    

f=Fib2()
print(f[0])
print(f[1])
print(f[2])
print(f[3])


#__getattr__()方法，动态返回一个属性
#__getattr__默认返回就是None
class Person(object):
    
    def __init__(self):
        self.name="zhangsan"
    
    #只有在没有找到属性的情况下，才调用__getattr__    
    def __getattr__(self,attr):
        if attr=='score':
            return 99
        #按照约定，抛出AttributeError的错误
        raise AttributeError('Person object has no attribute \'%s\'' % attr)
p=Person()
print(p.name)
print(p.score)

#不存在属性
#print(p.abc)  #默认返回None

#--------------------------------
# 完全动态调用特性：
# 把一个类的所有属性和方法调用全部动态化处理

#链式调用API设计
class Chain(object):
    def __init__(self,path=''):
        self._path=path
        
    def __getattr__(self,path):
        return Chain('%s/%s' %(self._path,path))
    
    def __str__(self):
        return self._path
    
    __repr__=__str__
    

#/status/user/timeline/list
print(Chain().status.user.timeline.list)


#带参数的链式调用
class ParamChain(object):
    def __init__(self,path=''):
        self._path=path
        
    def __getattr__(self,path):
        return ParamChain('%s/%s' %(self._path,path))
    
    def __call__(self,path):
        return ParamChain('%s/%s' %(self._path,path))
    
    def __str__(self):
        return self._path
    
    __repr__=__str__
    

# /users/michael/repos
print(ParamChain().users('michael').repos)  


# __call__:直接在实例本身上调用    
class Teacher(object):
    def __init__(self,name):
        self.name=name
        
    def __call__(self):
        print('Teacher\'s name is %s' % self.name)
        
t=Teacher('lisi')

#直接对实例本身调用
t()  #Teacher's name is lisi

#__call__()还可以定义参数。对实例进行直接调用就好比对一个函数进行调用一样

#通过callable()函数，我们就可以判断一个对象是否是“可调用”对象(Callable)。
print(callable(Student('lisi')))
print(callable(Teacher('lisi')))




        