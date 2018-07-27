from enum import Enum,unique

Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 
'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

print(Month.Jan.value)  # 1
for name,member in Month.__members__.items():
    print(name,'=>',member,',',member.value)
    

#自定义枚举类

#@unique装饰器可以帮助我们检查保证没有重复值。
@unique
class Weekday(Enum):
    Sun = 0 # Sun的value被设定为0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6

#用成员名称引用枚举常量    
print(Weekday.Tue)
print(Weekday['Tue'])

#直接根据value的值获得枚举常量
print(Weekday(1))
    
    
    