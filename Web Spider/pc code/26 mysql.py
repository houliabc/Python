import pymysql
# 连接mysql数据库，打开游标
conn = pymysql.connect(host='localhost', user='root', password='123456', port=3306, db='class3')
yb = conn.cursor()
# 通过游标操作数据库
a=input()
b=input()
#mysql占位符是%s，sqlite是?
yb.execute('insert into tt values(%s,%s);',(a,b))
yb.execute('select * from tt;')
values = yb.fetchall()  # 提取游标的操作信息，元组格式
print(values)
yb.close()
conn.commit()
conn.close()
