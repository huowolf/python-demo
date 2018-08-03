#如果断言失败，assert语句本身就会抛出AssertionError
def foo(s):
    n=int(s)
    assert n!=0,'n is zero!'
    return 10/n

foo('0')