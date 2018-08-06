import re

#判断是否匹配
if re.match(r'\d{3}\-\d{3,8}', '010-12345'):
    print('ok')
else:
    print('failed')
    
#切分字符串
print(re.split(r'\s+', 'a b   c'))
print(re.split(r'[\s\,]+', 'a,b, c  d'))
print( re.split(r'[\s\,\;]+', 'a,b;; c  d'))

#分组
#除了简单地判断是否匹配之外，正则表达式还有提取子串的强大功能。
#用()表示的就是要提取的分组（Group）
m=re.match(r'^(\d{3})-(\d{3,8})$', '010-12345')

#group(0)永远是原始字符串
print(m.group(0))
print(m.group(1))
print(m.group(2))

#分组的嵌套
mm=re.match('((hello)world)','helloworld!!')
print('-------------')
print(mm.group(1))
print(mm.group(2))
print('------------')


#正则匹配默认是贪婪匹配，也就是匹配尽可能多的字符
#匹配出数字后面的0
print(re.match(r'^(\d+)(0*)$', '102300').groups())
#让\d+采用非贪婪匹配（也就是尽可能少匹配）
#加个?就可以让\d+采用非贪婪匹配
print(re.match(r'^(\d+?)(0*)$', '102300').groups())

#预编译该正则表达式
# 编译
re_telephone = re.compile(r'^(\d{3})-(\d{3,8})$')
print(re_telephone.match('010-12345').groups())
print(re_telephone.match('010-8086').groups())