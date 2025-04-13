import requests
import re
import csv
import time
url='https://kaoshi.wjx.top/vm/w2FLHCJ.aspx?code=091v7b0w3V7FN334sF0w3OWGbF3v7b0-&state=soj'
hd={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36'}

def sprawl(url):
    res = requests.get(url, headers=hd)
    res.encoding = res.apparent_encoding
    # print(res.text)
    city=re.findall(r"<div class='field ui-field-contain' topic=.*?  id='div.*?'  req='1'  data-role='fieldcontain' type='3'>(.*?)<div class='errorMessage'>",res.text,re.S)
    # print(city)
    
    for i in city:
        x=re.findall("<div class='topichtml'>(.*?)</div>",i,re.S)[0]
        y=re.findall("<div class='label' .*?>(.*?)</div>",i,re.S)
        print(x)
        for j in y:
            print(j)
        print()
    print(len(city))
sprawl(url)