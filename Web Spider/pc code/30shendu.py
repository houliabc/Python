import time
import requests
import re

#栈来实现深度遍历
class Stack():
    def __init__(self):
        self.s=[]
    def push(self,url):
        self.s.append(url)
    def pop(self):
        return self.s.pop()  #出最后一个元素
    def is_empty(self):
        return len(self.s)==0

def sprawl(url):
    res = requests.get(url, headers=hd)
    res.encoding = res.apparent_encoding
    # print(res.status_code)
    # print(res.text)
    li = re.findall("<td><a href='(.*?)'>(.*?)</a></td><td><a href='.*?'>(.*?)</a></td>", res.text, re.S)
    for i in li[::-1]:  #倒着进栈，为了出栈按顺序
        print(i[-2]+i[-1])
        new_url = url[:url.rfind('/') + 1] + i[0]
        s.push(new_url)
        time.sleep(0.1)


url='https://www.stats.gov.cn/sj/tjbz/tjypflml/2010/01.html'
hd={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36'}
s=Stack()
s.push(url)
while(not s.is_empty()):
    sprawl(s.pop())