"""
写数据库演示
"""
import pymysql
#建立数据库连接
db = pymysql.connect (host='localhost',
                      port=3306,
                      user='root',
                      password='skydream666',
                      database='stu',
                      charset='utf8')
#创建游标对象。操作数据库，执行sql语句
cur = db.cursor()
#执行写操作
try:
    #执行语句
    #插入
    # sql = "insert into class1 (name,age,score) values('dave',21,88);"
    #修改
    # sql = "update class1 set sex = 'm' where name = 'dave';"
    #删除
    # sql = "delete from class1 where name = 'dave';"
    exe = []
    for i in range(3):
        name = input('name:')
        age = int(input('age:'))
        score = float(input('score:'))
        exe.append((name,age,score))
        sql = "insert into class1 (name,age,score) values (%s,%s,%s);"

    cur.execute(sql,exe)
    db.commit() #将操作结果立即提交
except Exception as e:
    db.rollback() #事务回滚
    print(e)


#1. 关闭游标对象 ；断开数据库连接 ：
cur.close()
db.close()
