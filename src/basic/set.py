#set中，key不能重复

s=set([1,2,3])
print(s)

#重复元素在set中自动被过滤：
s=set([1,2,2,3,3])
print(s)

#添加元素
s.add(4)
print(s)

#删除元素
s.remove(4)
print(s)

#集合间的运算
s1=set([1,2,3])
s2=set([2,3,4])

#交集
print(s1&s2)
#并集
print(s1|s2)
#差集
print(s1-s2)