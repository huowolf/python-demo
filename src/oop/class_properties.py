class Student(object):
    name='Student'
    
    
s=Student()
print(s.name)           #实例属性不存在，会查找到类属性
print(Student.name)     #打印类属性

s.name='zhangsan'       #绑定实例属性
print(s.name)           #实例属性优先级高于类属性

print(Student.name)     #类属性并未消失
del s.name              #删除实例属性
print(s.name)           #会查找到类属性