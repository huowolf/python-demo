classmates=['zhangsan','lisi','wangwu']
print(classmates)

#获得元素个数
print(len(classmates))

#访问元素
print(classmates[0])
print(classmates[1])
print(classmates[2])
print(classmates[-1])
print(classmates[-2])
print(classmates[-3])

#添加元素
classmates.append("Ada")
print(classmates)
#插入到指定位置
classmates.insert(1, 'jack')
print(classmates)

#删除元素
classmates.pop(1)
print(classmates)

#更新元素
classmates[1]='lisi2'
print(classmates)

#默认升序排序
classmates.sort()
print(classmates)

#list中的元素的数据类型可以不同
L=["abc",123,True]
print(L)

#list中的元素可以是另外一个list
L=['java','python',['mysql','oracle'],123]
print(L)