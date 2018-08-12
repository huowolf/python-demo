#bytes
b=b'example'
#str 
s='example'

# str to bytes  
print(bytes(s, encoding = "utf8"))
# bytes to str  
print(str(b, encoding = "utf-8")) 

#ord()函数获取字符的整数表示
print(ord('A'))
#chr()函数把编码转换为对应的字符
print(chr(65))

#Unicode表示的str通过encode()方法可以编码为指定的bytes
print('ABC'.encode('ascii'))
print('中文'.encode('utf-8'))
#把bytes变为str，就需要用decode()方法
print(b'ABC'.decode('ascii'))
print(b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))

#计算str包含多少个字符
print(len('AAAAAAAAA'))
#len()计算bytes的字节数
print(len(b'ABC'))
print(len(b'\xe4\xb8\xad\xe6\x96\x87'))

#循环遍历字符串的每一个字符
name='zhangsan'
for i in name:
    print(i)

name=u"张三你好"
for i in name:
    print(i)
    
#find() 方法检测字符串中是否包含子字符串 str ，如果指定 beg（开始） 和 end（结束） 范围，则检查是否包含在指定范围内
str1='zhangsan example !!!'
str2='exam'
print(str1.find(str2))
print(str1.find(str2,10))