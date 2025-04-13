import requests
from bs4 import BeautifulSoup
import pymysql
class Db():
    def __init__(self):
        self.conn=pymysql.connect(host='localhost', user='root', password='123456', port=3306, db='class3')
        self.yb = self.conn.cursor()
    def insert(self,li):
        self.yb.execute('insert into weather values(%s,%s,%s,%s)',li)
    def close(self):
        self.yb.close()
        self.conn.commit()
        self.conn.close()
class Sprawl():
    def get_html(self,url):
        res = requests.get(url,headers=hd)
        res.encoding = res.apparent_encoding
        return res.text
    def get_info(self,html):
        sz=Db()
        soup = BeautifulSoup(html, 'lxml')
        li = soup.select("ul.t.clearfix > li")
        for i in li:
            date = i.h1.string
            weather = i.select('p.wea')[0].text  # i.p.text
            temp = i.select('p.tem')[0].text.strip()
            wind = i.select('p.win > i')[0].text.strip()
            ss = date + "   " + temp + "   " + weather + "  " + wind
            print(ss)
            sz.insert((date,weather,temp,wind))
        sz.close()
url='http://www.weather.com.cn/weather/101280601.shtml'
hd={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36'}
sztq=Sprawl()
wy=sztq.get_html(url)
sztq.get_info(wy)