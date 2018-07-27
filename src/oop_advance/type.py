def fn(self,name='world'):
    print('hello,%s' % name)

#通过type()函数创建出Hello类    
Hello=type('Hello',(object,),dict(hello=fn))

# 要创建一个class对象，type()函数依次传入3个参数：
# class的名称；
# 继承的父类集合，注意Python支持多重继承，如果只有一个父类，别忘了tuple的单元素写法；
# class的方法名称与函数绑定，这里我们把函数fn绑定到方法名hello上。

h=Hello()
h.hello()
print(type(Hello))  #<class 'type'>
print(type(h))      #<class '__main__.Hello'>