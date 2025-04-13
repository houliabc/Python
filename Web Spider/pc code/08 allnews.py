import requests
from bs4 import BeautifulSoup
import time
url='https://www.szpu.edu.cn/xwzt/szyw.htm'
url1='https://www.szpu.edu.cn/xwzt/szyw/'
hd={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36'}

def getnews(url):
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
        print(p)
        # print('\n')
        n+=1
for i in range(102):
    if i==0:
        print("-----第1页-----")
        getnews(url)
    else:
        url2=url1+str(103-i)+".htm"
        print("-----第"+str(i+1)+"页-----")
        getnews(url2)
    time.sleep(1)