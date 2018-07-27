#@property装饰器就是负责把一个方法变成属性调用的

class Student(object):
    
    @property
    def score(self):
    #def get_score(self):
        return self._score
    
    @score.setter
    def score(self,score):
    #def set_score(self,score):
        if not isinstance(score, int):
            raise ValueError('score must be an integer')
        if score<0 or score>100:
            raise ValueError('score must between 0~100')
        self._score=score
    
    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self, value):
        self._birth = value
    
    
    @property
    def age(self):
        return 2018-self._birth

s=Student()
# s.set_score(60)
# print(s.get_score())
# s.set_score(9999)    #非法调用

s.score=60          #实际转化为s.set_score(60)
print(s.score)      #实际转化为s.get_score()

# s.score=9999    #error


#@property定义只读属性，只定义getter方法，不定义setter方法就是一个只读属性
s.birth=1993
#s.age=25         #error   
print(s.age)
            