from bs4 import BeautifulSoup
fp=open("2.1HtmlDaima1.txt","r")
soup=BeautifulSoup(fp,'lxml')
print(soup)
# print(soup.prettify())  #整理好格式，好看
print(soup.a)  #访问第一个a标签
print(soup.h1)  #访问第一个h1标签
print(soup.h1['id'])  #拿第一个h1的id属性名的属性值
print(soup.h1.attrs)  #某标签地下的属性名和属性值的字典
print(soup.h1.string)  #找h1的下一层

print(soup.find_all(name='a',attrs={'class':'link'}))  #找所有a标签,attrs设置属性
fp.close()