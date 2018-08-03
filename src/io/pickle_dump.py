import pickle

#序列化
d=dict(name='bob',age=20,score=88)
f=open('dump.txt','wb')
pickle.dump(d,f)
f.close()
