import requests
import sqlite3
from bs4 import BeautifulSoup
import time

#先在终端cmd中建立数据库
# sqlite3 d:\pc\kugou.db   #表示用已有的数据库，或者没有就新建一个kugou.db的数据库
# sqlite> .database  #显示数据库的命令
# sqlite> create table kg(num int,song varchar(20),singer varchar(20),time varchar(20));
# sqlite> select * from kg;

class Db():  #将数据库操作封装成类
    def __init__(self):   #self每个方法必须自带，但传参不需要
        #连接数据库，打开游标
        self.con=sqlite3.connect('d:/pc/kugou.db')
        self.yb=self.con.cursor()
    def insert(self,li):  #插入方法
        # 通过游标操作数据库，插入数据
        self.yb.execute('insert into kg values(?,?,?,?)', li)
        # print(self.yb.rowcount)
    def close(self):  #关闭数据库方法
        # 关闭游标、提交数据、数据库
        self.yb.close()
        self.con.commit()
        self.con.close()

class Sprawl():
    def get_html(self,url):
        res = requests.get(url,headers=hd)
        res.encoding = res.apparent_encoding
        html=res.text
        return html
    def get_info(self,html):
        kg = Db()  #可以在类的方法中实例化
        soup=BeautifulSoup(html,'lxml')
        list = soup.select(".pc_temp_songlist li")
        # print(list)
        for li in list:
            num = li.select('span.pc_temp_num')[0].text.strip()
            song = li.select('a.pc_temp_songname')[0].text.split('-')[0].strip()
            singer = li.select('a.pc_temp_songname')[0].text.split('-')[-1].strip()
            time = li.select("span.pc_temp_time")[0].text.strip()
            ss=num+"   "+song+"   "+singer+"  "+time
            print(ss)
            kg.insert((num,song,singer,time))
        kg.close()


# 使用类爬取酷狗Top500的（排名、歌曲、歌手和时长)信息，并将数据存入sqlite数据库中。
u='https://www.kugou.com/yy/rank/home/'
hd={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36'}
kugou=Sprawl()
for i in range(1,24):  #24
    url=u+str(i)+"-8888.html"
    print("--------------------------------------------第"+str(i)+"页--------------------------------------------")
    HTML = kugou.get_html(url)
    kugou.get_info(HTML)
    time.sleep(0.05)