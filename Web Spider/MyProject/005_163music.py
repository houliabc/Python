#爬取网易云的热门评论
import requests
from lxml import etree
import time
from Crypto.Cipher import AES
from base64 import b64encode
import json

url="https://music.163.com/weapi/comment/resource/comments/get?csrf_token="

headers={
    'Aser-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36',
    'Cookie':'wyy_uid=20544906-1671-418a-a250-e09d6f39508c; pageContentBiz=GONG_GONG; pageContentBizProduct=""; lastUrlReferrer="https://docker-practice.github.io/"; hb_MA-AAAB-2D9387BB219C_source=docker-practice.github.io; _ntes_origin_from=bing; NMTID=00OYqbOZvBJMvFmIkRagTNKS8J7pyQAAAGWPSkIyg; _iuqxldmzr_=32; _ntes_nnid=cf1003ba88af882832ccbd46ca6b60ce,1744782822446; _ntes_nuid=cf1003ba88af882832ccbd46ca6b60ce; WEVNSM=1.0.0; WNMCID=tucmzr.1744782824519.01.0; sDeviceId=YD-Qp2JkYxQwgVER1AQQVPGbVqiXZcNTCbD; WM_NI=CrW%2FfE%2F1sbNRnRUG1S26Ywq0lEvgU3eUE0WApEIYjMtCYHpelJHkh8QGjLDiMPs%2BogZVOIf9TG4NeVZ6iEjbr02fuAbxXg%2BLa%2BDb%2FAqg5FBDIS9EGHow5APyq0JoJP6GYzk%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6eeccb54986f59995f440aa9e8bb6c55a928b9bacc75c97f5a7b5e2709b928389eb2af0fea7c3b92a81ae99d0e54fedefbd83cd5aae8e9ba8b459f2ea9798f43cb09bba88d839a78b8bd1d64bb49b87bae947b89d97a9f36fb096888ceb349399a6adc7638f90bdccee6d9a8a81aae5339899fcafe85e9aeaa7a6e96ab2f0fe87f84ba2a89888aa48a3f58c83ae4bb3b9fba7c1508b8df7a6c644ada9fba2d373b3f08690c95cf699979bea37e2a3; WM_TID=njtwJwaJmSdBEVRFAVfXaBvzDNNcMclk; ntes_utid=tid._.eALQnzDX5mxEU0BABEOTaAr2GNYYSCOT._.0; JSESSIONID-WYYY=Mz9oHe6K2cIcR1R%2FvcjKPtrWHQiMkzwbYkT8WGxbOKJHF1nFm6kzfgu96n6FvtZNmWIKn%2F%5CKe2E5ByBRA8l1j0GiBovNFc5nR6jrzp%2BR1f7YkUrJ%5C1VqbNlvxy2961A6oDoOhmGk9rWKZ3QZTA%2Bei3mToNNfpUkq6PqnRngA3DnwFr5e%3A1744802422231',
    #防盗链：溯源，当前本次请求的上一级
    # 'Referer':f'https://www.pearvideo.com/popular',
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
