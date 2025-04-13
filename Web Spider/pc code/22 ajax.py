import re
import requests
from lxml import etree
import time
url='https://www.jianshu.com/c/V2CqjW?order_by=added_at&page='
hd={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36'}

#求出总页数
res = requests.get(url+'1', headers=hd)
res.encoding = res.apparent_encoding
all=re.findall('<div class="info">.*?收录了(.*?)篇.*?', res.text, re.S)[0]
page=int(int(all)/10)+1

def sprawl(url):
    res = requests.get(url, headers=hd)
    res.encoding = res.apparent_encoding
    #re正则的方式
    html = res.text
    S = re.S
    # title = re.findall('<h1 class="bt">(.*?)</h1>', html, S)[0]
    # title = re.findall('<h1 class="bt">(.*?)</h1>', res.text, re.S)[0]  #原生
    #xpath的方式
    selector=etree.HTML(res.text)
    div=selector.xpath('//ul/li[@data-shock="0"]/div')
    for i in div:
        title = i.xpath('./a[@class="title"]')[0].xpath('string(.)').strip()
        p = i.xpath('./p[@class="abstract"]')[0].xpath('string(.)').strip()
        author = i.xpath('./div[@class="meta"]/a[@class="nickname"]')[0].xpath('string(.)').strip()
        comment = i.xpath('./div[@class="meta"]/a[@target="_blank"]')[1].xpath('string(.)').strip()
        love = i.xpath('./div[@class="meta"]/span[last()]')[0].xpath('string(.)').strip()
        # print(title)
        # print(p)
        # print(author)
        # print(comment)
        # print(love)
        print([title,p,author,comment,love])
        # print()
# sprawl(url)
for i in range(1,page+1):
    u = url + str(i)
    print(u)
    sprawl(u)
    time.sleep(0.01)