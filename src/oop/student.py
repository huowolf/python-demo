class student(object):
    
    def __init__(self,name,age):
        self.__name = name      #私有属性
        self.__age = age
    
    def print_student(self):
        print('%s : %s' % (self.__name,self.__age))
        
    def get_name(self):
        return self.__name
    
    def get_age(self):
        return self.__age
    
    def set_name(self,name):
        self.__name=name
        

zhangsan=student('zhangsan',25)
lisi=student('lisi',22)

zhangsan.print_student()
lisi.print_student()

#非法操作,私有属性不可以直接访问
# print(lisi.__name)
# lisi.__name='wangwu'
# lisi.print_student()

print(zhangsan.get_name())
print(zhangsan.get_age())

zhangsan.set_name("zhangsan2")
print(zhangsan.get_name())



