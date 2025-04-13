import requests
url="https://www.szpu.edu.cn/xwzt/szyw.htm"
res=requests.get(url)
res.encoding='utf-8'
print(res.text)

#szpu logo保存
url="https://www.szpu.edu.cn/images/2023/logo_red.png"
res=requests.get(url)
with open('szpu.png','wb') as f:
    f.write(res.content)

#baidu logo保存
url="https://www.baidu.com/img/flexible/logo/pc/result.png"
res=requests.get(url)
with open('baidu.png','wb') as f:
    f.write(res.content)
