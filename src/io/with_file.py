#读操作
with open('hello.txt','r') as f:
    print(f.read())
    
#写操作
with open('test.txt','w') as f:
    f.write('hello world\n')
    f.write('hello world\n')
    f.write('hello world\n')