import requests
from bs4 import BeautifulSoup
url='https://www.szpu.edu.cn/xwzt/szyw.htm'
hd={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36'}
res=requests.get(url,headers=hd)
res.encoding=res.apparent_encoding

soup=BeautifulSoup(res.text,'lxml')

all=soup.find('ul',attrs={'class':'list23'}).find_all('div',attrs={'class':'txt'})
n=1
for i in all:
    h4=i.find('h4').text
    h6=i.find('h6').text
    p=i.find('p').text
    print(str(n)+'.'+h4+'------'+h6)
    print(p+'\n')
    n+=1

# lis=soup.find('ul',attrs={'id':'hotsearch-content-wrapper'}).find_all('li')
# for li in lis:
#     index=int(li['data-index'])+1
#     content=li.find('span',attrs={'class':'title-content-title'}).text
#     print(str(index)+content)