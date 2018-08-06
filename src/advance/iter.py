d = {'a':1,'b':2,'c':3}


# for ... in 循环
for key in d:
    print(key)

print("---------------------")
    
for value in d.values():
    print(value)
    
print("---------------------")

for k,v in d.items():
    print(k,v)

print("---------------------")

#通过序列索引迭代(类似于java中的for循环)
fruits = ['banana', 'apple',  'mango']
for index in range(len(fruits)):
    print(fruits[index])


# 下标循环
for i,value in enumerate(['A','B','C']):
    print(i,value)
    
    