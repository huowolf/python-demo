def lazy_sum(*args):
    def sum():
        ax=0
        for n in args:
            ax=ax+n
        return ax
    return sum

#返回的函数并没有立刻执行，而是直到调用了f()才执行
f=lazy_sum(1,2,3,4)
print(f)
print(f())

def count():
    fs=[]
    for i in range(1,4):
        def f():
            return i*i     
        fs.append(f)
    
    #返回了新创建的3个函数对象    
    return fs

#print(count()[0]())
f1,f2,f3=count()
print(f1())
print(f2())
print(f3())

#返回闭包时牢记一点：返回函数不要引用任何循环变量，或者后续会发生变化的变量。

def count2():
    def f(j):
        def g():
            return j*j
        return g
    fs=[]
    for i in range(1,4):
        fs.append(f(i)) # f(i)立刻被执行，因此i的当前值被传入f()
    return fs

f1,f2,f3=count2()
print(f1())
print(f2())
print(f3())