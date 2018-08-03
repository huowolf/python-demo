from io import StringIO

f=StringIO()
f.write('hello world')

print(f.getvalue())

#获取stream position
print(f.tell())

#重置stream position
f.seek(0)
s=f.readline()
print(s)