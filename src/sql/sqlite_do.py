import sqlite3

conn = sqlite3.connect('test.db')
# 创建一个Cursor:
cursor=conn.cursor()
#执行一条SQL语句，创建user表:
cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
#继续执行一条SQL语句，插入一条记录:
cursor.execute('insert into user (id, name) values (\'1\', \'Michael\')')
# 通过rowcount获得插入的行数:
print(cursor.rowcount)

cursor.close()
conn.commit()
conn.close()


