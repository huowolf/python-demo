from io import BytesIO

#BytesIO写操作：
f=BytesIO()
f.write('中文'.encode(encoding='utf_8'))
print(f.getvalue())

#BytesIO读操作：
f=BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
s=f.read()
print(s.decode(encoding='utf_8'))


