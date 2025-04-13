import requests
import json
import csv
import time

fp=open("33stock.csv","w",encoding='utf-8-sig',newline='')
c=csv.writer(fp)
c.writerow(['股票编号','名称','最新价','最高价','最低价'])

def sprawl(url):
    res = requests.get(url, headers=hd)
    res.encoding = res.apparent_encoding
    # print(res.text)
    data = json.loads(res.text)
    for i in data:
        # 股票编号，名称，最新价，最高价，最低价
        symbol = i['symbol']
        name = i['name']
        new = i['trade']
        high = i['high']
        low = i['low']
        print(symbol, name, new, high, low)
        c.writerow([symbol, name, new, high, low])
    time.sleep(0.1)

# url='https://vip.stock.finance.sina.com.cn/mkt/#sh_a'
url='https://vip.stock.finance.sina.com.cn/quotes_service/api/json_v2.php/Market_Center.getHQNodeData?page='
hd={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36'}
for i in range(1,4):
    print(f"-----------------第{i}页-----------------")
    sprawl(url+str(i)+'&num=40&sort=symbol&asc=1&node=sh_a&symbol=&_s_r_a=auto')