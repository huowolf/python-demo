#https://www.cnblogs.com/JohnABC/p/4076855.html
#经典的错误代码
def foo():
    a=1
    
    def bar():
        #显式的指定a不是闭包的局部变量
        nonlocal a
        a=a+1
        return a
    
    return bar

c=foo()
#UnboundLocalError: local variable 'a' referenced before assignment
print(c())
print(c())
print(c())