import requests
from bs4 import BeautifulSoup
import time
f=open('11 kugouTop500.txt','w',encoding='utf-8')
u='https://www.kugou.com/yy/rank/home/'
hd={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36'}

def sprawl(url):
    res = requests.get(url, headers=hd)
    res.encoding = res.apparent_encoding
    soup = BeautifulSoup(res.text, 'lxml')
    list=soup.select(".pc_temp_songlist li")
    for li in list:
        num = li.select('span.pc_temp_num')[0].text.strip()
        song = li.select('a.pc_temp_songname')[0].text.split('-')[0].strip()
        singer = li.select('a.pc_temp_songname')[0].text.split('-')[-1].strip()
        time = li.select("span.pc_temp_time")[0].text.strip()
        end=num + ',' + song + ',' + singer + ',' + time
        print(end)
        f.write(end + '\n')
# with open('kugou.txt','w',encoding='utf-8') as f:
for i in range(1,24):  #24
    url=u+str(i)+"-8888.html"
    print("--------------------------------------------第"+str(i)+"页--------------------------------------------")
    sprawl(url)
    time.sleep(1)
f.close()