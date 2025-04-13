import re
import requests
import time
url='https://www.szpu.edu.cn/xwzt/szyw.htm'
url1='https://www.szpu.edu.cn/xwzt/szyw/'
hd={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36'}
f=open("16 re_news.txt","w",encoding='utf-8')
def getnews(url):
    res=requests.get(url,headers=hd)
    res.encoding=res.apparent_encoding
    ul=re.findall(r'<ul class="list23">(.*?)</ul>',res.text,re.S)[0]
    li=re.findall('<li.*?>(.*?)</li>',ul,re.S)
    n=1
    for i in li:
        h4=re.findall('<h4.*?>(.*?)</h4>',i,re.S)[0]
        p = re.findall('<p.*?>(.*?)</p>', i, re.S)[0]
        h6 = re.findall('<h6.*?>(.*?)</h6>', i, re.S)[0]
        print(str(n)+'.'+h6+'------'+h4)
        print(p)
        n+=1
        f.write(h6+','+h4+','+p+'\n')
for i in range(104):
    if i==0:
        print("-----第1页-----")
        getnews(url)
    else:
        url2=url1+str(104-i)+".htm"
        print("-----第"+str(i+1)+"页-----")
        getnews(url2)
    time.sleep(0.001)
f.close()