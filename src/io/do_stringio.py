from io import StringIO

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