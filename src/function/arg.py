#默认参数
def power(x,n=2):
    s=1
    while n>0:
        n = n-1
        s = s*x
    return s

print(power(5))
print(power(5, 3))


#默认参数必须指向不可变对象
def addEnd(L=[]):
    L.append('End')
    return L

#print(addEnd([1,2,3]))
#print(addEnd(['x','y','z']))
#print(addEnd())
#print(addEnd())

def addEnd2(L=None):
    if L is None:
        L=[]
    L.append('End')
    return L

print(addEnd2())
print(addEnd2())


#可变参数
def calc(*numbers):
    result = 0
    for n in numbers:
        result += n*n
    return result


print(calc(1,2,3))
print(calc(1,3,5,7))

#将list或tuple转变成可变参数
nums=[1,2,3]
print(calc(*nums))


#关键字参数
def person(name,age,**kw):
    print('name:',name,'age:',age,'other:',kw)
    
person("huowolf", 30)
person('bob', 25, city='beijing')
person('ada', 45,gender='M',job='Engineer')

#将dict转换为关键字参数
extra={'city':'beijing','job':'Engineer'}  
person('jack', 24,**extra)  


#命名关键字参数
def people(name,age,*,city,job):
    print(name,age,city,job)

#使用Tab快捷键定位下一个参数    

#命名关键词参数调用必须给出参数名
person('jack', 25,'beijing','Engineer')   #非法调用

#只接受city和job参数名字的调用
people('jack', 24,city='beijing',job='Engineer')    
# people('jack', 24,city='beijing',job='Engineer',zipcode='11000') #非法调用

