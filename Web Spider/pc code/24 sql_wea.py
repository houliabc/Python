import requests
import sqlite3
from bs4 import BeautifulSoup

#先在终端cmd中建立数据库
# sqlite3 d:\pc\weather.db   #表示用已有的数据库，或者没有就新建一个weather.db的数据库
# SQLite version 3.39.3 2022-09-05 11:02:23
# sqlite> .database  #显示数据库的命令
# sqlite> create table tt(date varchar(20),wea  varchar(20),temp  varchar(20),wind  varchar(20));
# sqlite> select * from tt;

class WeatherDb():  #将数据库操作封装成类
    def __init__(self):   #self每个方法必须自带，但传参不需要
        #连接数据库，打开游标
        self.con=sqlite3.connect('d:/pc/weather.db')
        self.yb=self.con.cursor()
    def insert(self,li):  #插入方法
        # 通过游标操作数据库，插入数据
        self.yb.execute('insert into tt values(?,?,?,?)', li)
        # print(yb.rowcount)
    def close(self):  #关闭数据库方法
        # 关闭游标、提交数据、数据库
        self.yb.close()
        self.con.commit()
        self.con.close()

class Sprawl():
    def get_html(self,url):
        res = requests.get(url)
        res.encoding = res.apparent_encoding
        html=res.text
        return html
    def get_info(self,html):
        sztq = WeatherDb()  #可以在类的方法中实例化
        soup=BeautifulSoup(html,'lxml')
        li=soup.select("ul.t.clearfix > li")
        for i in li:
            date=i.h1.string
            weather=i.select('p.wea')[0].text   #i.p.text
            temp=i.select('p.tem')[0].text.strip()
            wind=i.select('p.win > i')[0].text.strip()
            ss=date+"   "+temp+"   "+weather+"  "+wind
            print(ss)
            sztq.insert((date,weather,temp,wind))
        sztq.close()

url='http://www.weather.com.cn/weather/101280601.shtml'
sz=Sprawl()
HTML=sz.get_html(url)
sz.get_info(HTML)