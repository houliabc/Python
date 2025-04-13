import re
str="abc123cd"
#---------------------# search
m=re.search(r'\d',str)
print(m)
print(m.group())  #group()返回取出的字符串
print(m.span())   #span()返回匹配的位置信息，包括开始和不包含结束

#---------------------# findall
m=re.findall(r'\d',str)
print(m)

#---------------------# sub
origin = "hello alex bcd alex lge alex acd 19"
r = re.sub("a","替换字符",origin) #替换匹配成功的指定位置字符串
print(r)
origin = "hello alex b7cd alex lge alex 3acd 19"
r=re.sub(r"\d","看这里",origin)
print(r)

#---------------------# split
origin = "hello alex bcd alex lge alex acd 19"
r = re.split("a", origin)   #根据a进行分组分割字符串，返回列表
print(r)
origin = "hello alex bcd alex lge alex 2acd 19"
r = re.split("a\w+", origin) #根据正则匹配分割字符串
print(r)

#---------------#re.S
a = '<div>指数</div>'
word = re.findall('<div>(.*?)</div>',a)
print(word)
a = '''<div>
指数</div>
'''
word = re.findall('<div>(.*?)</div>',a)  #不饿能匹配上面的换行
print(word)
word = re.findall('<div>(.*?)</div>',a,re.S)  #第三个参数，re.S表示使匹配包括换行在内的所有字符（常用）

print(word)
print(word[0].strip())