from io import StringIO

#StringIO顾名思义就是在内存中读写str,常用作临时缓冲。
#把str写入StringIO
f=StringIO()
f.write('hello')
f.write(' ')
f.write('world')

print(f.getvalue())


#读取StringIO
f=StringIO('Hello!\nHi!\nGoodbye!')
while True:
    s=f.readline()
    if s=='':
        break
    print(s.strip())    # 把末尾的'\n'删掉