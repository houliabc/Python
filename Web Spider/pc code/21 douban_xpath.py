import re
import requests
from lxml import etree
import time
url='https://book.douban.com/top250'
hd={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36'}

def sprawl(url):
    res = requests.get(url, headers=hd)
    res.encoding = res.apparent_encoding
    selector=etree.HTML(res.text)
    td=selector.xpath('//tr/td[@valign="top"][2]')  #2不是下标的2，就是第几个
    for i in td:
        book=i.xpath('./div[@class="pl2"]/a')[0].xpath('string(.)')
        book=re.sub(r'\s','',book)
        author=i.xpath('./p[@class="pl"]/text()')[0].strip().split('/')[0].strip()
        price = i.xpath('./p[@class="pl"]/text()')[0].strip().split('/')[-1].strip()
        score = i.xpath('./div[@class="star clearfix"]/span[@class="rating_nums"]/text()')[0].strip()
        num = i.xpath('./div[@class="star clearfix"]/span[@class="pl"]/text()')[0].strip()[1:-2].strip()
        # print(book)
        # print(author)
        # print(price)
        # print(score)
        # print(num)
        print([book,author,price,score,num])
        # print()
# sprawl(url)
for i in range(0,226,25):
    u = url + '?start=' + str(i)
    print(u)
    sprawl(u)
    time.sleep(0.5)