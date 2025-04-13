import requests
url="https://www.baidu.com/"
res=requests.get(url)

#以下是requests对象的四个常用属性
print(type(res))
print(res.status_code)  #返回状态，200表示成功，400失败
print(res.encoding)  #编码方式
res.encoding='utf-8'
print(res.encoding)
print(res.text)  #网页源代码的字符串
print(res.content)  #二进制内容

#get两个参数的形式
url="https://www.baidu.com/s?"
kv={'wd':'python'}
r=requests.get(url,kv)
r.encoding=r.apparent_encoding
print(r.request.url)