#tuple 有序，一旦初始化就不能修改
persons=('zhangsan','lisi','wangwu')
print(persons)

#不能修改
#persons[0]='zhang'  #非法操作

#访问元素
print(persons[0])
print(persons[1:])

#定义只有一个元素的tuple
t=(1,)
print(t)