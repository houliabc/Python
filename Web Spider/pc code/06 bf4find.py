import requests
from bs4 import BeautifulSoup
#第一节课
url='https://www.baidu.com/'
hd={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36'}
res=requests.get(url,headers=hd)
res.encoding=res.apparent_encoding
# print(res.status_code)
# print(res.text)

#第二节课
soup=BeautifulSoup(res.text,'lxml')
# span_all=soup.find_all('span',attrs={'class':'title-content-title'})
# for span in span_all:
#     print(span.text)

#第三节课
title=soup.find('div',attrs={'class':'title-text c-font-medium c-color-t'})['aria-label']
print(title+":")

lis=soup.find('ul',attrs={'id':'hotsearch-content-wrapper'}).find_all('li')
for li in lis:
    index=int(li['data-index'])+1
    content=li.find('span',attrs={'class':'title-content-title'}).text
    print(str(index)+content)