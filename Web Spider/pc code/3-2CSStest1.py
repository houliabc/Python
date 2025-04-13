from bs4 import BeautifulSoup
doc="<div><p>A</p><span><p>B</p></span></div><div><p>C</p></div>"
soup=BeautifulSoup(doc,"lxml")
print(soup)
tags=soup.select("div p")  #查找div下的所有子孙节点P，为A、B、C
print(tags)
for tag in tags:
    print(tag)
tagss = soup.select("div > p")  #查找div下所有直接子节点p，所以不包含
print(tagss)
for tag in tagss:
    print(tag)
