# isinstance() 与 type() 区别：
# 1、type() 不会认为子类是一种父类类型，不考虑继承关系。
# 2.isinstance() 会认为子类是一种父类类型，考虑继承关系。
# 如果要判断两个类型是否相同推荐使用 isinstance()。


print(type(123)==int)
print(type('abc')==str)

#判断一个对象是否是函数
import types
def fn():
    pass

print(type(fn)==types.FunctionType)
print(type(abs)==types.BuiltinFunctionType)


print('----------------------')



a=2
print(isinstance(a, int))
print(isinstance(a, str))
print(isinstance(a, (int,str,list)))    #是元祖中的一个就返回True

print('---------------------')

class A:
    pass

class B(A):
    pass

print(isinstance(A(), A))   #True
print(type(A())==A)         #True
print(isinstance(B(), A))   #True
print(type(B())==A)         #False