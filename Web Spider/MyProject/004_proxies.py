#使用代理爬虫
# -*- encoding = utf-8 -*-
# author : houliabc
import requests

proxies={
    'https':'106.12.111.83:9103'  # 代理IP和端口
}

res=requests.get('https://www.baidu.com',proxies=proxies)
res.encoding=res.apparent_encoding
print(res.text)