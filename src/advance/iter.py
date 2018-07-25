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

# 下标循环
for i,value in enumerate(['A','B','C']):
    print(i,value)
    
    