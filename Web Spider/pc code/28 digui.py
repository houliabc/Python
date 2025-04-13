import requests
import re
import requests
import time

#利用递归实现深度优先
def sprawl(url):
    res=requests.get(url,headers=hd)
    res.encoding=res.apparent_encoding
    # print(res.text)
    li=re.findall(r"<td><a href='(.*?)'>(.*?)</a></td><td><a href='.*?'>(.*?)</a></td>",res.text,re.S)
    # print(li)
    for i in li[::1]:
        new_url=url[0:url.rfind('/')+1]+i[0]
        print(i[1]+i[2])
        # print(new_url)
        time.sleep(0.5)
        sprawl(new_url)

url='https://www.stats.gov.cn/sj/tjbz/tjypflml/2010/01.html'
hd={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36'}
sprawl(url)