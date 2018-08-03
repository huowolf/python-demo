import json

#把Python对象变成一个JSON
d=dict(name='lisi',age=20,score=89)
print(json.dumps(d))

#有关中文编码的问题
obj = dict(name='小明', age=20)
s = json.dumps(obj, ensure_ascii=False)
print(s)


#JSON反序列化为Python对象
json_str='{"name": "lisi", "age": 20, "score": 89}'
d=json.loads(json_str)
print(d)

#将对象序列化
class Student(object):
    def __init__(self,name,age,score):
        self.name = name
        self.age = age
        self.score = score
        

def student2dict(std):
    return {
        'name':std.name,
        'age':std.age,
        'score':std.score
    }

def dict2student(d):
    return Student(d['name'],d['age'],d['score'])

s=Student('zhangsan',20,89)
#指定转换函数    
print(json.dumps(s,default=student2dict))
#任意class的实例变为dict
print(json.dumps(s,default=lambda obj:obj.__dict__))

json_str = '{"age": 20, "score": 88, "name": "Bob"}'
stu=json.loads(json_str,object_hook=dict2student)
print(stu)
