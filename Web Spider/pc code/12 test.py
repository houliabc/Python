import requests
from bs4 import BeautifulSoup
import time
import csv  #内置
f=open('12 test.csv','w',encoding='utf-8-sig',newline='')  #utf-8会乱码
wt=csv.writer(f)  #创建一个csv写入对象，之后要写入csv需要使用这个
wt.writerow(['排序','歌曲','歌手','时长'])  #以列表形式写入
u='https://www.kugou.com/yy/rank/home/'
hd={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36'}

def sprawl(url):
    res = requests.get(url, headers=hd)
    res.encoding = res.apparent_encoding
    soup = BeautifulSoup(res.text, 'lxml')
    list=soup.select(".pc_temp_songlist li")
    for li in list:
        num = li.select('.pc_temp_num')[0].text.strip()
        song = li.select('.pc_temp_songname')[0].text.split('-')[0].strip()
        singer = li.select('.pc_temp_songname')[0].text.split('-')[-1].strip()
        time=li.select(".pc_temp_time")[0].text.strip()
        all=(num+","+song+','+singer+','+time)
        print(all)
        wt.writerow(all.split(','))

# with open('kugou.txt','w',encoding='utf-8') as f:
for i in range(1,24):  #24
    url=u+str(i)+"-8888.html"
    print("--------------------------------------------第"+str(i)+"页--------------------------------------------")
    sprawl(url)
    time.sleep(0.5)
f.close()