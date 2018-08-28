#lambda x: x * x
#关键字lambda表示匿名函数，冒号前面的x表示函数参数

def build(x,y):
    return lambda: x * x + y * y

ret=build(3, 4)
print(ret())