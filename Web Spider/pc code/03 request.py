import requests
url="https://www.baidu.com/"
hd={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36'}

try:
    res = requests.get(url, headers=hd)
    res.raise_for_status()  #如果爬虫报错就会抛出异常然后去except
    res.encoding = res.apparent_encoding
    # print(res.text)
except:
    print("出错")
