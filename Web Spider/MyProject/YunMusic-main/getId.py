# -*- encoding = utf-8 -*-
# author : manlu
import base64
import json
import random
from binascii import hexlify

import requests
from Crypto.Cipher import AES


class GetId:
    def __init__(self,keyword,number):
        self.url='https://music.163.com/weapi/cloudsearch/get/web?csrf_token='
        self.keyword=keyword
        self.number=number
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36',
            'Referer': 'https://music.163.com/search/',
            'Host': 'music.163.com',
        }
    def get(self):
        try:
            r=requests.post(self.url,headers=self.headers,data=self.getData(),timeout=5)
            songs=r.json()['result']['songs']
            result=[]
            for i in songs:
                name=i['name']
                singer=i['ar'][0]['name']
                id=i['privilege']['id']
                result.append([id,name,singer])
            return result
        except:
            return
    def getData(self):
        d={"hlpretag":"<span class='s-fc7'>","hlposttag":"</span>","s":self.keyword,"type":"1","offset":"0","total":"true","limit":self.number,"csrf_token":""}
        d=json.dumps(d)
        e='010001'
        f='00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7'
        g='0CoJUm6Qyw8W8jud'
        i=self.a()
        params=self.b(d,g)
        params=self.b(params,i)
        encSecKey=self.c(i,e,f)
        return {'params':params,'encSecKey':encSecKey}
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
        result = base64.b64encode(tmp).decode()
        return result
    def c(self,a,b,c):
        """
        RSA 加密
        """
        a = a[::-1]
        result = pow(int(hexlify(a.encode()), 16), int(b, 16), int(c, 16))
        return format(result, 'x').zfill(131)
if __name__ == '__main__':
    get=GetId('love story',1)
    print(get.get())