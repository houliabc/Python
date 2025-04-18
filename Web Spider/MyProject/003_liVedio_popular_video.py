#使用防盗链和处理AJAX的方式下载梨视频的热门视频：https://www.pearvideo.com/popular
# -*- encoding = utf-8 -*-
# author : houliabc

import requests
import time
from lxml import etree

#获取热门视频的全部AJAX的url
url=[f"https://www.pearvideo.com/popular_loading.jsp?reqType=41&categoryId=&start={i}&sort={i}&mrd=0.36964496654591505" for i in range(0,500,10)]

headers={
    'Aser-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36',
    #和cookie无关
    'Cookie':'PEAR_UUID=5a12d32b-db12-478f-8cfa-fbd6ad41e3a6; _uab_collina=174470775541176861795832; Hm_lvt_9707bc8d5f6bba210e7218b8496f076a=1744707756; HMACCOUNT=C4BDCE15E5F1B832; p_h5_u=7405694F-4E95-49AD-8820-7CB235767EB6; JSESSIONID=0ECCCC057D789819013A26085F6A76CC; PEAR_UID=kFEqTQI2Ahc3o9+Hnedflg==; PEAR_TOKEN=f7fd30fc-191e-429b-827c-9caa5e055e2a; tfstk=gnNIQxT75HxQftxg-MQZlpEFlbc7Nu1VdUg8ozdeyXhp23Uxb0yFKYJRNoqjYYInT7Z_rlmyLuWneeV_cQRFx94JNblR0i5VgyYEZbIq7SHDkH0-l0Cre4ntt4-a0TKCgy4HWfSLOv12Vk3NOyn82vntX2mtJ3h82dhtj40Jv4dd5PniX2dKeQh9B2urJpE-wNatj4h-Jv5MfVXIby_HRn-SRdAQ8cOJw5gOqbzCMIgUM2MIDyFwaQ8xRviYJcs0dzErBzD7ZUASvye0qqEpvik3yRZsRb1wpjU_eogg9s-ISJzTucUXkIUnO-Nj9JsMIXrQ6fFLhUd85XinBVM6AGiYtPFm6A5AlPFgYyV_zUC-7ooT-Wh5MZcI9DhsS7SM90wTeWknZHIqKze_f2GA4vAqc2T6FFMDNViV5N9kE_QGr5zOSCvZpV0ZgN_63LxDwQJ3aN9JQv3iSLQ15K-C.; Hm_lpvt_9707bc8d5f6bba210e7218b8496f076a=1744715146',
    #防盗链：溯源，当前本次请求的上一级
    'Referer':f'https://www.pearvideo.com/popular',
}

for i in url:
    res=requests.get(i,headers=headers)
    res.encoding=res.apparent_encoding
    href=etree.HTML(res.text).xpath('//a[contains(@class, "popularembd") and contains(@class, "actplay")]/@href')  #获取视频网页的href属性
    contId=[j.split('_')[-1] for j in href]  #视频id列表
    urls=[f"https://www.pearvideo.com/{j}" for j in href]  #视频网页列表
    # print(urls)

    #遍历视频网页列表，获取视频的url
    for u,Id in zip(urls,contId):  #将多个可迭代对象的元素一一对应地组合成一个元组
        videoUrl=f"https://www.pearvideo.com/videoStatus.jsp?contId={Id}&mrd=0.2894818592336348"

        headers2={
            'Aser-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36',
            #和cookie无关
            'Cookie':'PEAR_UUID=5a12d32b-db12-478f-8cfa-fbd6ad41e3a6; _uab_collina=174470775541176861795832; Hm_lvt_9707bc8d5f6bba210e7218b8496f076a=1744707756; HMACCOUNT=C4BDCE15E5F1B832; p_h5_u=7405694F-4E95-49AD-8820-7CB235767EB6; PEAR_UID=kFEqTQI2Ahc3o9+Hnedflg==; PEAR_TOKEN=f7fd30fc-191e-429b-827c-9caa5e055e2a; tfstk=gnNIQxT75HxQftxg-MQZlpEFlbc7Nu1VdUg8ozdeyXhp23Uxb0yFKYJRNoqjYYInT7Z_rlmyLuWneeV_cQRFx94JNblR0i5VgyYEZbIq7SHDkH0-l0Cre4ntt4-a0TKCgy4HWfSLOv12Vk3NOyn82vntX2mtJ3h82dhtj40Jv4dd5PniX2dKeQh9B2urJpE-wNatj4h-Jv5MfVXIby_HRn-SRdAQ8cOJw5gOqbzCMIgUM2MIDyFwaQ8xRviYJcs0dzErBzD7ZUASvye0qqEpvik3yRZsRb1wpjU_eogg9s-ISJzTucUXkIUnO-Nj9JsMIXrQ6fFLhUd85XinBVM6AGiYtPFm6A5AlPFgYyV_zUC-7ooT-Wh5MZcI9DhsS7SM90wTeWknZHIqKze_f2GA4vAqc2T6FFMDNViV5N9kE_QGr5zOSCvZpV0ZgN_63LxDwQJ3aN9JQv3iSLQ15K-C.; Hm_lpvt_9707bc8d5f6bba210e7218b8496f076a=1744715968; tgw_l7_route=e0ec575606f95cc9ad003a83f9f8574f; JSESSIONID=6F49870333C4214EABE71C87DD2AA954',
            #防盗链：溯源，当前本次请求的上一级
            'Referer':f'https://www.pearvideo.com/video_{Id}',
}
        #爬取每个视频网页的防爬文件
        res2=requests.get(videoUrl,headers=headers2)

        json=res2.json()
        videoUrl=json['videoInfo']['videos']['srcUrl']

        #处理视频url，替换掉系统时间
        systemTime=json['systemTime']
        videoUrl=videoUrl.replace(systemTime,'cont-'+Id)
        # print(videoUrl)

        #实现下载videoUrl视频
        videoContent=requests.get(videoUrl,headers=headers).content
        #使用相对路径保存视频
        with open(f'Web Spider/MyProject/assets/vedio{Id}.mp4',mode='wb') as f:
            f.write(videoContent)
        print(f'vedio{Id}.mp4',end='，')

        time.sleep(1)
    print()
    time.sleep(3)
print("爬虫结束")