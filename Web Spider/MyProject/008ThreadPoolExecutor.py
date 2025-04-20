# 运用线程池加速爬取北京新发地
# -*- encoding = utf-8 -*-
# author : houliabc
import requests
# import json
import csv
from concurrent.futures import ThreadPoolExecutor

f=open('./Web Spider/MyProject/files/xinfadi.csv','w',encoding='utf-8',newline='')
c=csv.writer(f)

url="http://www.xinfadi.com.cn/getPriceData.html"
dt={
    'limit': 20,
    'current': 1,
    'pubDateStartTime': '',
    'pubDateEndTime': '',
    'prodPcatid': '',
    'prodCatid': '',
    'prodName': ''
}

def getInfo(page):
    dt['current']=page
    res=requests.post(url,data=dt).json()['list']
    # print(res.json()['list'])
    for i in res:
        c.writerow([i['id'],i['prodName'],i['prodCat'],i['lowPrice'],i['highPrice'],i['avgPrice'],i['place'],i['unitInfo'],i['pubDate']])
    # print(page,'提取完毕！')


if __name__ == '__main__':
    # for i in range(1,2):   #19198
    #     getInfo(i)
    with ThreadPoolExecutor(30) as t:
        for i in range(1,19198):
            t.submit(getInfo,i)
            # print()
    print("全部下载完毕！")