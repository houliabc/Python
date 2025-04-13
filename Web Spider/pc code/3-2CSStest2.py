from bs4 import BeautifulSoup
doc="<body>demo<div>A</div><b>X</b><p>B</p><span><p>C</p></span><p>D</p></body>"
soup=BeautifulSoup(doc,"lxml")
# print(soup)
# print(type(soup))
# tags=soup.select("div ~ p")  #查找div后面同级别的所有p节点，为B、D
# print(type(tags))
# for tag in tags:
#    print(tag)
# tags=soup.select("div + p")    #查找div下一个兄弟节点p，因为div的下一个兄弟节点是<b>X</b>，所以没有
# for tag in tags:
#     print(tag)
