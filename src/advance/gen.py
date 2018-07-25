#生成器
g=(x*x for x in range(10))
#生成器是可以迭代的，但是只可以读取它一次
for n in g:
    print(n)
    
#无任何输出    
print('-------------------')
for n in g:
    print(n)
print('-------------------')

#理解yield
def odd():
    print('step 1')
    #每执行到一个 yield 语句就会中断，并返回一个迭代值，下次执行时从 yield 的下一个语句继续执行
    yield '111111111'
    print('step 2')
    yield '222222222'
    print('step 3')
    yield '333333333'
    

o = odd()
#===============================================================================
# print(next(o))
# print('------------------')
# print(next(o))
# print('------------------')
# print(next(o))
# print('------------------')
#===============================================================================
#print(next(o))          # StopIteration错误
for i in odd():
    print(i)
    
    
#输出斐波那契数列的前N个数
def fib(max):
    n,a,b=0,0,1
    while n<max:
        yield b
        a,b=b,a+b
        n=n+1
    return 'done'


for n in fib(6):
    print(n)
    
#拿到generator的return语句的返回值
g=fib(6)
while True:
    try:
        x=next(g)
        print('g:',x)
    except StopIteration as e:
        print('return:',e.value)
        break
        
        