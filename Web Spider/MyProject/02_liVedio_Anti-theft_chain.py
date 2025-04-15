import requests
#使用防盗链下载梨视频的项目

url="https://www.pearvideo.com/video_1799330"
contId = url.split('_')[-1]

videoStatus=f"https://www.pearvideo.com/videoStatus.jsp?contId={contId}&mrd=0.2894818592336348"

headers={
    'Aser-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36',
    #和cookie无关
    'Cookie':'PEAR_UUID=5a12d32b-db12-478f-8cfa-fbd6ad41e3a6; _uab_collina=174470775541176861795832; Hm_lvt_9707bc8d5f6bba210e7218b8496f076a=1744707756; HMACCOUNT=C4BDCE15E5F1B832; p_h5_u=7405694F-4E95-49AD-8820-7CB235767EB6; Hm_lpvt_9707bc8d5f6bba210e7218b8496f076a=1744708123; tgw_l7_route=e0ec575606f95cc9ad003a83f9f8574f; JSESSIONID=4DFC04F59081FDC912CA0443289E8B02',
    #防盗链：溯源，当前本次请求的上一级
    'Referer':f'https://www.pearvideo.com/video_{contId}',
}

res=requests.get(videoStatus,headers=headers)

json=res.json()
videoUrl=json['videoInfo']['videos']['srcUrl']
print(videoUrl)

#利用正则替换“/1744709013181-”内容
# import re
# videoUrl=re.sub(r'/\d+-',f'/cont-{contId}-',videoUrl)
# print(videoUrl)

#另一种处理方式
systemTime=json['systemTime']
videoUrl=videoUrl.replace(systemTime,'cont-'+contId)
print(videoUrl)


#实现下载videoUrl视频
videoContent=requests.get(videoUrl,headers=headers).content
#使用相对路径保存视频
with open('Web Spider/MyProject/assets/vedio.mp4',mode='wb') as f:
    f.write(videoContent)
print('保存完成')
