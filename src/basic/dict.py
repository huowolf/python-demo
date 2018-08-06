#字典(map)

d={'zhangsan':95,'lisi':90,'wangu':85}

#访问字典里的值
print(d['zhangsan'])

#修改字典
d['Ada']=67         #添加键值对
print(d['Ada'])

#多次操作同一个key,后面的value会覆盖前一个value
d['Ada']=97         #更新键值对
print(d['Ada'])

#判断key是否存在
print('zhang' in d)
print(d.get('zhang'))  #如果key不存在，返回None

#删除字典元素
d.pop('zhangsan')   #删除指定元素
print(d)

d.clear()           #删除所有元素
print(d)

#dict的key必须是不可变对象
# key=[1,2]
# d[key]="a list"


#dict() 函数用于创建一个字典
#创建空字典
dd=dict()
print(dd)
#传入关键字
dd=dict(a=1,b=2,c=3)
print(dd)
# 可迭代对象方式来构造字典
dd=dict([('one',1),('two',2),('three',3)])
print(dd)
