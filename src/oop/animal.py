class Animal(object):
    def run(self):
        print('Animal is running...')
        
        
class Dog(Animal):
    def run(self):
        print('dog is running...')
    
    def eat(self):
        print('dog eats meat')


class Cat(Animal):
    def run(self):
        print('cat is running...')


dog=Dog()
dog.run()
cat=Cat()
cat.run()

#----------------------
#理解多态
#不一定需要传入Animal类型。我们只需要保证传入的对象有一个run()方法就可以了
def run_twice(animal):
    animal.run()
    animal.run()
    
run_twice(Animal())
run_twice(Dog())
run_twice(Cat())