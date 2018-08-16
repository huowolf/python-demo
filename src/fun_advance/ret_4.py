#闭包中是不能修改外部作用域的局部变量的
def foo():
    m=0   
    def foo1():
        m=1
        print('foo1:',m)
        
        
    print('foo old:',m)  
    foo1() 
    #m最后依旧是0,没有被改变 
    print('foo new:',m)

foo()


def bar(l):
    def bar_in():
        l.append(4)
        return l
    return bar_in

l=[1,2,3]
ret=bar(l)
print(ret())


    
    
    