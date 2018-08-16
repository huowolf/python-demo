#当循环结束以后，循环体中的临时变量i不会销毁，而是继续存在于执行环境中。
flist=[]
for i in range(3):
    #python的函数只有在执行时，才会去找函数体里的变量的值。
    def foo(x):
        print(x+i)
    flist.append(foo)
    
for f in flist:
    f(2)
#当把函数加入flist列表里时，python还没有给i赋值，只有当执行时，再去找i的值是什么，
#这时在第一个for循环结束以后，i的值是2，所以以上代码的执行结果是4,4,4.   

#解决方法
flist=[]
for i in range(3):
    def foo(x,y=i):#定义时立即取得i的值并保存
        print(x+y)
    flist.append(foo)
    
for f in flist:
    f(2)