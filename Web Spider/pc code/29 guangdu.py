import requests
import re
import requests
import time

#广度优先
class Queue:
    def __init__(self):
        self.q=[]
    def push(self,data):
        self.q.append(data)
    def pop(self):
        return self.q.pop(0)
    def is_empty(self):
        return len(self.q)==0

def sprawl(url):
    res=requests.get(url,headers=hd)
    res.encoding=res.apparent_encoding
    # print(res.text)
    li=re.findall(r"<td><a href='(.*?)'>(.*?)</a></td><td><a href='.*?'>(.*?)</a></td>",res.text,re.S)
    # print(li)
    for i in li:
        new_url=url[0:url.rfind('/')+1]+i[0]
        tjj.push(new_url)
        print(i[1]+i[2])
        # print(new_url)
        time.sleep(0.5)
        # sprawl(new_url)

start_url='https://www.stats.gov.cn/sj/tjbz/tjypflml/2010/01.html'
hd={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36'}
tjj=Queue()
tjj.push(start_url)
while (not tjj.is_empty()):
    url=tjj.pop()
    sprawl(url)