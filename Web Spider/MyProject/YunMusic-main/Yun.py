# -*- encoding = utf-8 -*-
# author : manlu

import argparse
import os

import requests

from getId import GetId
from getMusic import GetMusic


class Downloader:
    def __init__(self,flag,keys,number,path):
        self.flag=flag
        self.keys=keys
        self.number=number
        self.path=path
        self.encoding=encoding

    def download(self):
        if self.flag:
            self.downList()
        else:
            self.downOne(self.keys,self.number)
    def downOne(self,key,number):
        midGetter=GetId(key,number)
        tmp=midGetter.get()
        mids=[a[0] for a in tmp]
        names=[a[1] for a in tmp]
        singers=[a[2] for a in tmp]
        for i in range(number):
            mid=mids[i]
            name=names[i]
            singer=singers[i]
            urlGetter=GetMusic(mid)
            download_url=urlGetter.get()
            try:
                r=requests.get(download_url,timeout=5)
                with open("%s/%s-%s.mp3"%(path,name,singer),'wb') as f:
                    f.write(r.content)
                print("%s-%s 保存成功"%(name,singer))
            except Exception as e:
                # midGetter=GetId(key,number+1)
                print("%s-%s 下载失败"%(name,singer))
    def downList(self):
        for key in self.keys:
            self.downOne(key,self.number)

def title():
    print("+------------------------------------------")
    print("+ \033[34;1m网易云音乐下载器\033[0m")
    print("+ \033[34;1m用法：python.exe Yun.py [-h] [-k KEYWORD] [-n NUMBER] [-p PATH] [-f FILE] [-e ENCODING]\033[0m")
    print("+ \033[34;1m版本：1.0\033[0m")
    print("+ \033[34;1m下载地址：https://github.com/13337356453/YunMusic\033[0m")
    print("+ \033[34;1m作者：manlu\033[0m")
    print("+------------------------------------------")


if __name__ == '__main__':
    title()
    parser = argparse.ArgumentParser(description='网易云音乐下载器')
    parser.add_argument('-k', '--keyword', help="歌曲关键字")
    parser.add_argument('-n', '--number', help="下载数量", default=1,type=int)
    parser.add_argument('-p', '--path', help="保存地址(默认为‘./music’)", default='./music')
    parser.add_argument('-f', '--file', help="需要下载的歌曲列表", default=None)
    parser.add_argument('-e', '--encoding', help="编码", default='utf-8')
    args = parser.parse_args()
    keyword=args.keyword
    number=args.number
    path=args.path
    file=args.file
    encoding=args.encoding

    if not os.path.exists(path):
        os.mkdir(path)
    if file!=None:
        try:
            f=open(file,'r',encoding=encoding)
            list=[x.strip() for x in f.readlines() if x.strip()!=""]
            f.close()
            downloader=Downloader(1,list,number,path)
            downloader.download()
        except Exception as e:
            print(e)
            exit(-1)
    elif keyword!=None:
        downloader=Downloader(0,keyword,number,path)
        downloader.download()
    else:
        print("请指定关键字")
        exit(-1)


