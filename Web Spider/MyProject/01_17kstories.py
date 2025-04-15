import requests
import datetime
import mysql.connector

session=requests.Session()

url='https://user.17k.com/ck/author2/shelf?page=1&appKey=2406394919'

headers={
    'Aser-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36',
    'Cookie':'GUID=23da4b5a-2e36-4cdb-8b20-40cef3665971; sajssdk_2015_cross_new_user=1; _openId=ow-yN5g5J2X_0_WEbhe9P6EU5XNs; c_channel=0; c_csc=web; accessToken=nickname%3DLoader369336061%26avatarUrl%3Dhttps%253A%252F%252Fcdn.static.17k.com%252Fuser%252Favatar%252F06%252F46%252F25%252F104082546.jpg-88x88%253Fv%253D1744704852000%26id%3D104082546%26e%3D1760258497%26s%3D792c22262d854d4e; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22104082546%22%2C%22%24device_id%22%3A%221963882d89b25d9-0f1de9048df6018-26011c51-1024000-1963882d89c3167%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%A4%BE%E4%BA%A4%E7%BD%91%E7%AB%99%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fopen.weixin.qq.com%2F%22%2C%22%24latest_referrer_host%22%3A%22open.weixin.qq.com%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC%22%7D%2C%22first_id%22%3A%2223da4b5a-2e36-4cdb-8b20-40cef3665971%22%7D'
}

response=requests.get(url,headers=headers)
for i in response.json()['data']:
    category=i['bookCategory']['name']
    bookName=i['bookName']
    lastUpdateChapter=i['lastUpdateChapter']['name']
    updateTime=i['updateTimeValue']
    #pdateTime是时间戳，下面转换为对应的年月日
    date_time = datetime.datetime.fromtimestamp(updateTime/1000)
    print(category,bookName,lastUpdateChapter,date_time)
    #导入数据库，从创建表开始
    #连接数据库
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="123456"
    )
    mycursor = mydb.cursor()
    mycursor.execute("CREATE DATABASE IF NOT EXISTS Myproject")
    mycursor.execute("USE Myproject")
    #创建表
    mycursor.execute("CREATE TABLE IF NOT EXISTS 17books (category VARCHAR(255), bookName VARCHAR(255), lastUpdateChapter VARCHAR(255), updateTime DATETIME)")

    sql = "INSERT INTO 17books (category, bookName, lastUpdateChapter, updateTime) VALUES (%s, %s, %s, %s)"
    val = (category, bookName, lastUpdateChapter, date_time)
    mycursor.execute(sql, val)

    mydb.commit()

    print(mycursor.rowcount, "record inserted.")