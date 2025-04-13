from bs4 import BeautifulSoup
fp=open("2.2HtmlDaima2.txt","r")
soup=BeautifulSoup(fp,'lxml')

tags=soup.find_all(name='a',attrs={'class':'sister'})  #找所有a标签,attrs设置属性
# print(tags[0])
for tag in tags:
    print(tag)
    print(tag['href'])

print(soup.find(name='a', attrs={'id': 'link3'}))
print(soup.find(name='a',attrs={'id':'link3'}).name)  #标签名
print(soup.find(name='a',attrs={'id':'link3'}).contents)  #子标签列表
print(soup.find(name='a',attrs={'id':'link3'}).string)  #标签文本内容
print(soup.find(name='a',attrs={'id':'link3'}).attrs)  #标签属性字典

print(soup.find('p',attrs={'class':'title'}))
print(soup.find('p',attrs={'class':'title'}).contents)
print(soup.find('p',attrs={'class':'title'}).string)

print(soup.find('p',attrs={'class':'story'}))
print(soup.find('p',attrs={'class':'story'}).contents)
print(soup.find('p',attrs={'class':'story'}).name)
print(soup.find('p',attrs={'class':'story'}).string)
print(soup.find('p',attrs={'class':'story'}).attrs)
print(soup.find('p',attrs={'class':'story'}).text)
fp.close()