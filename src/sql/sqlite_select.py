import sqlite3

#查询记录
conn = sqlite3.connect('test.db')
cursor=conn.cursor()
cursor.execute('select * from user where id=?', ('1',))
# 获得查询结果集
values = cursor.fetchall()
print(values)
cursor.close()
conn.close()