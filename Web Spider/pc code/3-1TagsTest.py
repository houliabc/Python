from bs4 import BeautifulSoup
fp=open('2.2HtmlDaima2.txt','r')
soup=BeautifulSoup(fp,'lxml')
# print(type(soup))
# print(soup)
## 父级节点
# print(soup.a.parent)
# print(soup.find('a',attrs={"id":"link2"}))
# print(soup.find('a',attrs={"id":"link2"}).parent)
# print(soup.find('a',attrs={"id":"link2"}).parent.name)
# print(soup.head.parent)
# print(soup.head.parent.name)
# print(soup.html.parent.name)
# print(soup.document)
# print(type(soup.document))

## 直接子节点
# print(soup.find('p', attrs={"class":"story"}))
# print(soup.find('p', attrs={"class":"story"}).children)
# mm=soup.find('p', attrs={"class":"story"}).children
# for i in mm:
#     print(i)
# print(soup.a.children)
# aa=soup.a.children
# for i in aa:
#     print(i)
## 子孙节点
# print(soup.find('p', attrs={"class":"story"}).descendants)
# ppp=soup.find('p', attrs={"class":"story"}).descendants
# for i in ppp:
#     print(i)
## 兄弟节点
# print(soup.find('a',attrs={"id":"link2"}))
# print(soup.find('a',attrs={"id":"link2"}).next_sibling)
# print(soup.find('a',attrs={"id":"link2"}).next_siblings)
# for i in soup.find('a',attrs={"id":"link2"}).next_siblings:
#     print(i)
print(soup.find('a',attrs={"id":"link2"}).previous_sibling)
# fp.close()

