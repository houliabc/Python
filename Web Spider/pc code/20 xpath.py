import requests
from lxml import etree
import time
url='https://www.szpu.edu.cn/xwzt/szyw.htm'
hd={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36'}

def sprawl(url):
    res = requests.get(url, headers=hd)
    res.encoding = res.apparent_encoding
    selector=etree.HTML(res.text)
    div=selector.xpath('//*[@class="txt"]')
    for i in div:
        title=i.xpath('./h4/text()')[0]
        content=i.xpath('./p/text()')[0]
        time = i.xpath('./h6/text()')[0]
        print(title)
        print(content)
        print(time)
        print()
sprawl(url)