from contextlib import contextmanager,closing
from urllib.request import urlopen


class Query(object):
    def __init__(self,name):
        self.name = name
        
    def query(self):
        print('query info about %s...' % self.name)
        

@contextmanager  
def create_query(name):
    print('Begin')
    q=Query(name)
    yield q
    print('End')
    
    
with create_query('bob') as q:
    q.query()
    

#----------------------------------
#在某段代码执行前后自动执行特定代码，也可以用@contextmanager实现
@contextmanager
def tag(name):
    print('<%s>' % name)
    yield
    print('<%s>' % name)
    
with tag('h1'):
    print('hello')
    print()
    
#===============================================================================
# 代码的执行顺序是：
# 1.with语句首先执行yield之前的语句，因此打印出<h1>；
# 2.yield调用会执行with语句内部的所有语句，因此打印出hello和world；
# 3.最后执行yield之后的语句，打印出</h1>。
#===============================================================================

#用closing()来把该对象变为上下文对象
with closing(urlopen('https://www.python.org')) as page:
    for line in page:
        print(line)