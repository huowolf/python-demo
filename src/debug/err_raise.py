class FooError(ValueError):
    pass

def foo(s):
    n=int(s)
    if n==0:
        raise FooError('invalid value:%s' % s)
    return 10/n

foo('0')

#只有在必要的时候才定义我们自己的错误类型
#尽量使用Python内置的错误类型
        