import pymysql


hostname = 'localhost'
username = 'root'
password = 'root'
database = 'py_test'
conn = pymysql.connect( host=hostname, user=username, passwd=password, db=database)

def create():
    cursor = conn.cursor()
    cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
    # 插入一行记录，注意MySQL的占位符是%s:
    cursor.execute('insert into user (id, name) values (%s, %s)', ['1', 'Michael'])
    print(cursor.rowcount)
    conn.commit()
    cursor.close()

# 运行查询:
def selectAll():
    cursor=conn.cursor()
    cursor.execute('select * from user where id = %s', ('1',))
    value=cursor.fetchall()
    print(value)
    cursor.close()
    
conn.close()
    
selectAll()
    

