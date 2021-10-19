import pymysql

#获取连接对象
conn = pymysql.connect(host="127.0.0.1",
                       user="root",
                       passwd="123456",
                       db="sakila",
                       charset='utf8')



cursor = conn.cursor()
sql = "select * from actor"
cursor.execute(sql)
# print(cursor.fetchone())
print('============================')
print(cursor.fetchmany(3))
print('============================')
print(cursor.fetchall())

conn.close()