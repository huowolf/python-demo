class Student(object):
    pass


#动态绑定(在程序运行期间绑定)

#定义一个函数作为实例方法
def set_age(self,age):
    self.age=age
    

from types import MethodType
s=Student()

#给实例绑定一个方法
s.set_age = MethodType(set_age,s)  
s.set_age(25)
print(s.age)

#给一个实例绑定的方法，对另一个实例是不起作用的
s2=Student()
#s2.set_age(25)    #非法操作


#---------------------------------

def set_score(self,score):
    self.score=score
    
#给class绑定方法后，所有实例均可调用
Student.set_score=set_score

s.set_score(100)
print(s.score)
s2.set_score(98)
print(s2.score)

#--------------------------

class person(object):
    __slots__=('name','age')    #用tuple定义允许绑定的属性名称
    
p=person()
p.name='zhangsan'
p.age=25
#p.score=89      #非法绑定


#__slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的
class man(person):
    pass

m=man()
m.score=99      #依然可以绑定score属性
print(m.score)
