import requests
import json
import pprint  #好看打印

def wea_forecast():
    ct=input('请输入城市：')
    url=f'https://geoapi.qweather.com/v2/city/lookup?location={ct}&key=4f380ca1e6ff48d0adb558c6b090eae7'
    res=requests.get(url)
    data=json.loads(res.text)
    city=data['location'][0]['name']
    id=data['location'][0]['id']

    url2=f'https://devapi.qweather.com/v7/weather/7d?location={id}&key=4f380ca1e6ff48d0adb558c6b090eae7'
    res2=requests.get(url2)
    data2=json.loads(res2.text)
    for i in data2['daily']:
        # pprint.pprint(i)
        date=i['fxDate']
        textday=i['textDay']
        wind=i['windScaleDay']+'级风'
        temp=i['tempMin']+'-'+i['tempMax']+'℃'
        print(date,textday,wind,temp)
wea_forecast()