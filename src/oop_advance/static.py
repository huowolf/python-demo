class A(object):
    @staticmethod
    def foo():
        print('foo')

#静态方法无须实例化        
A.foo()

#也可以实例化后调用
obj=A()
obj.foo()