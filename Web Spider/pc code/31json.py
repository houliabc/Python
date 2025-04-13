import json

jsonstring = '''{
    "name":"网站",
    "num":3,
    "sites":[
    { "name":"Google", "info":["Android","Google搜索","Google翻译"]},
    { "name":"Runoob", "info":["菜鸟教程","菜鸟工具","菜鸟微信"]},
    { "name":"Taobao", "info":["淘宝","网购"]}
    ]
}'''
#json.loads：解码，将json变python
# json.dump：编码，将python变json
data=json.loads(jsonstring)
for key,value in data.items():
    print(key,value)

aa=data['sites'][2]['name']
print(aa)