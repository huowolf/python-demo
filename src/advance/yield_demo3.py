'''
Created on 2018年9月7日

@author: huowolf
'''
# send(msg) 和 next() 的返回值比较特殊，是下一个yield表达式的参数(yield 5，则返回 5)
def s():
    print('study yield')
    m=yield 5
    print(m)
    d=yield 16
    print('go on')
    

c=s()
s_d1=next(c)         # 相当于send(None)
s_d2=c.send('Fighting') # (yield 5)表达式被赋予了'Fighting'
print(s_d1,s_d2)
