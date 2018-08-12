#实现上下文管理是通过__enter__和__exit__这两个方法实现的
#紧跟with后面的语句被求值后，返回对象的__enter__()方法被调用，这个方法的返回值将被赋值给as后面的变量。
#当with后面的代码块全部被执行完之后，将调用前面返回对象的__exit__()方法。

class Query(object):
    def __init__(self,name):
        self.name = name
        
    def __enter__(self):
        print('Begin')
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type:
            print('Error')
        else:
            print('End')
            
    def query(self):
        print('query info about %s' % self.name)
        

with Query('zhangsan') as q:
    q.query()
