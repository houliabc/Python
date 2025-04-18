#爬取优美图库的所有图片，复习正则表达式和BeautifulSoup
# -*- encoding = utf-8 -*-
# author : houliabc

import requests
import re
from bs4 import BeautifulSoup
import time

def html(url,s=0) -> str:  #s=0表示获取网页源码，s=1表示获取soup
    res = requests.get(url, headers=headers)  #去掉安全验证s
    res.encoding = res.apparent_encoding  #设置编码格式
    if s==0:
        return res.text
    else:
        soup=BeautifulSoup(res.text, 'lxml')  #使用bs4解析网页源码
        return soup  #返回解析后的结果

u = 'https://www.umeituku.com/'
headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36'
}

index=html(u,1)  #获取首页源码
a=index.select('div.NavBox.fc h2 a')
for i in a:
    nav=(i['href'],i.string) 

    html=html(nav[0],0)  #获取分类页面源码
    print(html)
    11
    end=re.findall(r'<a href="(.*?)">末页</a>',html)
    print(end)

