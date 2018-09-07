'''
Created on 2018年9月7日

@author: huowolf
'''
def addlist(alist):
    for i in alist:
        yield i+1
    

alist=[1,2,3,4]
results=addlist(alist)
print(results)
for result in results:
    print(result)
