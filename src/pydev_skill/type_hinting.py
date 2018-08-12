#指定参数的类型， 函数的返回类型， 以及局部变量的类型
def foo(a:str, b:str) ->str:
    c=None  #type: str
    return 'hi'

#普通变量
x='' #type:str

#类的成员字段
class Student:
    def __init__(self):
        self.name=None #type: str
        
#集合泛型
my_list=[] #type: list[Student]
my_map={} #type: dict[int,str]
my_list_2=None #type:Tuple[int,Tuple[int]]

#注释后面, 写 list,List 都可以, 
#但不在注释后面的typeHint, 如形参及返回类型, 必须使用typing 包下相应的类. 
from typing import List,Tuple,Set 

def calc_sum(x:List[int]):
    pass

calc_sum([1,2])




        