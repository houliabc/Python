#爬取网易云的热门评论
import requests
from lxml import etree
import time
from Crypto.Cipher import AES
from base64 import b64encode
from binascii import hexlify
import json
import random

url="https://music.163.com/weapi/comment/resource/comments/get?csrf_token="

headers={
    'Aser-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36'
}


"""
    function a(a) {  #a=16
        var d, e, b = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789", c = "";
        for (d = 0; a > d; d += 1)
            e = Math.random() * b.length,  #取随机数
            e = Math.floor(e),  #取整
            c += b.charAt(e);  #charAt()方法返回指定位置的字符
        return c
    }
    function b(a, b) {  #a=加密的字符串，b=密钥
        var c = CryptoJS.enc.Utf8.parse(b)  #将字符串b转换为字节数组，b就是密钥，g是秘钥
          , d = CryptoJS.enc.Utf8.parse("0102030405060708")  #将字符串转换为字节数组
          , e = CryptoJS.enc.Utf8.parse(a) #将字符串a转换为字节数组，e是数据
          , f = CryptoJS.AES.encrypt(e, c, {  #AES加密，c是密钥
            iv: d,   #iv为初始向量，偏移量
            mode: CryptoJS.mode.CBC   #CBC模式
        });
        return f.toString()  #返回加密后的字符串
    }
    function c(a, b, c) {  #a=16位随机数，b和g都是固定的。c里面不产生随机数
        var d, e;
        return setMaxDigits(131),   
        d = new RSAKeyPair(b,"",c),  #RSA加密
        e = encryptedString(d, a)  #加密后的字符串
    }
    function d(d, e, f, g) {
        var h = {}
          , i = a(16);  #i为16位随机数==zLWDZDWLp6pFJqtx
        h.encText = b(d, g)   第一次加密，g是固定的，只有d是动态的，g是秘钥
        h.encText = b(h.encText, i) #第二次加密，i是定死了，i是秘钥
        h.encSecKey = c(i, e, f)   #i定死时，那么encSecKey也是定死的
        return h
    }
"""
# 这段代码是加密函数的实现，主要是对数据进行加密处理
# d(d, e, f, g)

data = {
    'csrf_token': "",
    'cursor': "-1",
    'offset': "0",
    'orderType': "1",
    'pageNo': "1",
    'pageSize': "20",
    'rid': "A_PL_0_2474537199",
    'threadId': "A_PL_0_2474537199"
}
e='010001'
f='00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7'
g='0CoJUm6Qyw8W8jud'
i='zLWDZDWLp6pFJqtx'

def get_encSecKey():  #获取加密的文本
    return "52533a730665edc89cdc771dac2fa8c01b5d25372ad85e5c691275254810952a0124f44e7b5002b073c4b79792a396433ad66ed66d9cf53d325ef5cf3a191f34d1e98e2368636c9cb355eb41f9e3bc1897e3f91fbbdbd35aa56cdf2ee2dc5376e9e3df6f197c1896863cff29e63b3fe6dd7677aad5421eb9d531b3678f532994"

def to_16(data):
    pad=16-len(data)%16  #计算填充的长度
    data+=chr(pad)*pad  #填充数据，chr()函数将整数转换为对应的字符
    return data  #返回填充后的数据

def enc_params(data,key):  #加密过程，模拟AES加密
    iv="0102030405060708"
    data=to_16(data)  #将数据转换为16的倍数
    aes=AES.new(key.encode('utf-8'),AES.MODE_CBC,iv.encode('utf-8'))   #创建加密器
    bs=aes.encrypt(data.encode('utf-8'))  #加密
    return str(b64encode(bs),encoding='utf-8')  #返回加密后的字符串，bs是字节数组，b64encode()函数将字节数组转换为base64编码的字符串

def get_params(data):  #默认这里接受的是字符串  获取加密后的参数
    first=enc_params(data,g)  #第一次加密
    second=enc_params(first,i)  #第二次加密
    return second

res=requests.post(url,headers=headers,data={
    'params':get_params(json.dumps(data)),  #加密后的参数
    'encSecKey':get_encSecKey()  #加密后的密钥
})
print(res.json())  #打印返回的json数据

#接下来处理拿到的数据，显示评论
data=res.json()
comments=data['data']['comments']  #获取评论数据
for i in comments:
    print(f"评论人：{i['user']['nickname']}, 评论内容：{i['content']}, 点赞数：{i['likedCount']}")
    time.sleep(1)  #延时1秒，防止请求过快被封


def a(self,a=16):
    """
    获取16位随机字符串
    """
    words="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    result=''
    for i in range(a):
        result+=words[random.randint(0,len(words)-1)]
    return result
def b(self,data,key):
    """
    AES 加密
    """
    iv = b'0102030405060708'
    pad = 16 - len(data) % 16
    data = data + chr(2) * pad

    aes = AES.new(key.encode(), AES.MODE_CBC, iv)
    tmp = aes.encrypt(data.encode())
    result = b64encode(tmp).decode()
    return result
def c(self,a,b,c):
    """
    RSA 加密
    """
    a = a[::-1]
    result = pow(int(hexlify(a.encode()), 16), int(b, 16), int(c, 16))
    return format(result, 'x').zfill(131)