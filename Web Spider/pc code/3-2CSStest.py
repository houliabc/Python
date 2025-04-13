from bs4 import BeautifulSoup
fp=open('2.2HtmlDaima2.txt','r')
soup=BeautifulSoup(fp,'lxml')
# print(soup.a)
# print(soup.find_all('a'))
# print(soup.select('a'))
# print(soup.find('a',attrs={'id':'link2'}))
# print(soup.select('a#link2'))
# print(soup.select('p.title'))
# print(soup.select('body p'))
# print(soup.select('p a'))
# print(soup.select("p[class='story'] a"))
# print(soup.select('p.story a'))
# print(soup.select('p[class] a'))
# print(soup.select('html head title'))
# print(soup.select('body [class]'))
# print(soup.select('p [class]'))
# print(soup.select('body [class]'))
# print(soup.select('body [class] a'))
# print(soup.select("a[href='http://example.com/lacie']"))    #带有属性
# print(soup.select("a[href^='http://example.com']"))     #指定开头
# print(soup.select("a[href$='sie']"))    #指定结尾
# print(soup.select("a[href*='example']"))   #指定包含



