import pymysql
import re
#建立数据库连接
db = pymysql.connect (host='localhost',
                      port=3306,
                      user='root',
                      password='skydream666',
                      database='dict',
                      charset='utf8')
#创建游标对象。操作数据库，执行sql语句
cur = db.cursor()

f = open('dict.txt')
args_list = []
for line in f:
    tup = re.findall(r"(\S+)\s+(.*)",line)[0]
    args_list.append(tup)
f.close()

sql = "insert into words (word,mean) values(%s,%s);"

try:
    cur.executemany(sql,args_list)
    db.commit()
except:
    db.rollback()

#1. 关闭游标对象 ；断开数据库连接 ：
cur.close()
db.close()
