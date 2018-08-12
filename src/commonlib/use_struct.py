import struct

#pack函数把任意数据类型变成bytes
print(struct.pack('>I', 10240099))
#unpack把bytes变成相应的数据类型
#I：4字节无符号整数和H：2字节无符号整数
print(struct.unpack('>IH', b'\xf0\xf0\xf0\xf0\x80\x80'))