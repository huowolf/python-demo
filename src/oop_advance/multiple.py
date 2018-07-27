class Animal(object):
    pass

class Runnable(object):
    def run(self):
        print('running...')
        
class Flyable(object):
    def fly(self):
        print('flying...')

#哺乳类
class Mammal(Animal):
    pass

class Bird(Animal):
    pass

# 各种动物:
class Dog(Mammal,Runnable):
    pass

# 蝙蝠
class Bat(Mammal,Flyable):
    pass

# 鹦鹉
class Parrot(Bird,Flyable):
    pass

# 鸵鸟
class Ostrich(Bird,Runnable):
    pass

d=Dog()
d.run()

        
