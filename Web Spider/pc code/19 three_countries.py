import requests
import re
import csv
import time
fp=open("19 three_countries.csv","w",encoding='utf-8-sig',newline='')
# c=csv.writer(fp)
# c.writerow(['书名','作者','定价','评分','评价人数'])
url='https://www.shicimingju.com/book/sanguoyanyi'
hd={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36'}

def sprawl(url):
    for n in range(1,121):
        res = requests.get(url+'/'+str(n)+'.html', headers=hd)
        res.encoding = res.apparent_encoding
        title = re.findall('<h1 class="bt">(.*?)</h1>', res.text, re.S)[0]
        list = re.findall('<div class="text p_pad">(.*?)</div>', res.text, re.S)[0].strip()
        text=re.findall('<p>(.*?)</p>', list, re.S)
        print(title)
        for i in text:
            # re.sub(r'[&nbsp|\s];','',i)
            print(i.strip('&nbsp;').strip())
        print()
    #     print([book,author,price,score,count])
    #     c.writerow([book,author,price,score,count])
    print()
    time.sleep(0.3)
sprawl(url)
# for u in range(0,226,25):
#     u=url+'?start='+str(u)
#     print(u)
#     sprawl(u)
fp.close()