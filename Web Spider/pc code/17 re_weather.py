import requests
import re
import csv
import time
fp=open("17 re_weather.csv","w",encoding='utf-8-sig',newline='')
c=csv.writer(fp)
c.writerow(['城市','日期','天气','气温','风度'])
url='http://www.weather.com.cn/weather/101280601.shtml'
hd={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36'}

def sprawl(url):
    res = requests.get(url, headers=hd)
    res.encoding = res.apparent_encoding
    city=re.findall(r'<a href="http://www.weather.com.cn/weather/\d*.shtml" target="_blank">(.*?)</a>',res.text,re.S)[0]
    li=re.findall('<li class="sky skyid.*?">(.*?)</li>',res.text,re.S)
    for i in li:
        day=re.findall('<h1>(.*?)</h1>',i,re.S)[0]
        weather = re.findall('<p .*? class="wea">(.*?)</p>', i, re.S)[0]
        temp = re.findall('<p class="tem">(.*?)</p>', i, re.S)[0]
        # print(temp)
        temp = ''.join(re.findall('<span>(.*?)</span>(.*?)<i>(.*?)</i>', temp, re.S)[0])
        # print(temp)
        # temp= re.split(">(.*?)<",temp.strip())
        # temp=temp[1]+temp[3]+temp[-2]
        wind = re.findall('<i>(.*?)</i>', i, re.S)[1]
        print([city,day, weather, temp, wind])
        c.writerow([city,day, weather, temp, wind])
    time.sleep(0.01)
for u in [url,'http://www.weather.com.cn/weather/101280101.shtml','http://www.weather.com.cn/weather/101130101.shtml','http://www.weather.com.cn/weather/101290101.shtml']:
    sprawl(u)
    print()
fp.close()