# 利用正则库爬取豆瓣TOP250的相关信息（书名，作者，定价，评分和评价人数），屏幕输出结果并存入CSV文件中
import requests
import re
import csv
import time
fp=open("18 top250.csv","w",encoding='utf-8-sig',newline='')
c=csv.writer(fp)
c.writerow(['书名','作者','定价','评分','评价人数'])
url='https://book.douban.com/top250'
hd={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36'}

def sprawl(url):
    res = requests.get(url, headers=hd)
    res.encoding = res.apparent_encoding
    li=re.findall('<td valign="top">(.*?)</td>',res.text,re.S)
    for i in li:
        # book=re.findall('<a .*?>(.*?)<',i,re.S)[0].strip()
        book2 = re.findall('<a .*?>(.*?)</a>', i, re.S)[0].strip()
        if('span' in book2):
            t1 = re.findall('<a .*?>(.*?)<', i, re.S)[0].strip()
            t2=re.findall('<span .*?>(.*?)</span>', book2, re.S)[0].strip()
            book=t1+t2
        else:
            book=book2
        author = re.findall('<p class="pl">(.*?)/', i, re.S)[0].strip()
        price = re.findall('<p class="pl">.*?(.*?)<', i, re.S)[0].split('/')[-1].strip()
        if('元' not in price):
            price+='元'
        score = re.findall('<span class="rating_nums">(.*?)<', i, re.S)[0].strip()
        count = re.findall('<span class="pl">\((.*?)\)<', i, re.S)[0].strip().split('评价')[0]
        print([book,author,price,score,count])
        c.writerow([book,author,price,score,count])
    print()
    time.sleep(0.5)
# sprawl(url)
for i in range(0,226,25):
    u=url+'?start='+str(i)
    print(u)
    sprawl(u)
fp.close()