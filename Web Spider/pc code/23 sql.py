import sqlite3

#先在终端中建立数据库
# sqlite3 d:\pc\weather.db   #表示用已有的数据库，或者没有就新建一个weather.db的数据库
# SQLite version 3.39.3 2022-09-05 11:02:23
# sqlite> .database
# sqlite> create table tt(date varchar(20),wea  varchar(20),temp  varchar(20),wind  varchar(20));

#连接数据库，打开游标
con=sqlite3.connect('d:/pc/test.db')
yb=con.cursor()

#通过游标操作数据库，插入数据
# yb.execute('insert into t values("333","jishu")')
# print(yb.rowcount)
#游标的查询操作
yb.execute('select * from t;')
values=yb.fetchmany(2)  #表示拿几条
values=yb.fetchall()  #拿全部
print(values)
#通过输入来插入
a=input()
b=input()
yb.execute('insert into t values(?,?)',(a,b))
print(yb.rowcount)

#关闭游标、提交数据、数据库
yb.close()
con.commit()
con.close()