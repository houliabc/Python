import requests
from bs4 import BeautifulSoup
import csv
import time
fp=open("13 weather.csv","w",encoding='utf-8-sig',newline='')
c=csv.writer(fp)
c.writerow(['城市','日期','天气','气温'])
url='http://www.weather.com.cn/weather/101280601.shtml'
hd={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36'}

def sprawl(url):
    res = requests.get(url, headers=hd)
    res.encoding = res.apparent_encoding
    soup = BeautifulSoup(res.text, 'lxml')
    # list=soup.select(".t .skyid")
    list = soup.select("ul.t.clearfix li")
    city = soup.select(".crumbs.fl a")[-1].text
    # print(city)
    for li in list:
        # day=li.select("h1")[0].text
        # weather=li.select(".wea")[0].text
        # t=li.select(".tem")[0]
        # temp=t.select('span')[0].text+"/"+t.select('i')[0].text
        # wind=li.select(".win i")[0].text
        # print(day,weather,temp,wind)
        day=li.h1.text
        p=li.select('p')
        weather=p[0].text.strip()
        temp=p[1].text.strip()
        wind=p[2].text.strip()
        c.writerow([day, weather, temp, wind])
    # time.sleep(0.5)
for u in [url,'http://www.weather.com.cn/weather/101280101.shtml','http://www.weather.com.cn/weather/101130101.shtml','http://www.weather.com.cn/weather/101290101.shtml']:
    sprawl(u)
    print()