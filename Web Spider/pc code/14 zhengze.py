import re
# a = 'one1two2three3'
# b = re.findall(r'\d+',a)
# print(b)

# a="xxIxxjshhhxxsssxxpythonxx"
# b1=re.findall(r'xx\w*xx',a)  #贪婪
# b2=re.findall(r'xx\w*?xx',a)  #非贪婪
# b3=re.findall('xx.*?xx',a)
# b4=re.findall('xx(.*?)xx',a)   #只取括号内内容
# print(b1)
# print(b2)
# print(b3)
# print(b4)


a="<table><tr><td>dddf</td><td>djjjf</td><td>kkke</td></tr></table>"
p1=re.findall(r'<td>\w*</td>',a)  #‘<'不算\w
p2=re.findall(r'<td>.*</td>',a)
p3=re.findall(r'<td>(\w*)</td>',a)
p1=re.findall(r'<td>.*?</td>',a)
p2=re.findall(r'<td>(.*?)</td>',a)  #(.*?)常用
p3=re.findall(r'<td>(.*?)</td>',a)[1]
print(p1)
print(p2)
print(p3)

a='liu@163.com,chdliuchenchen@163.com,sjssj@111.com,liuchen@szpu.edu.cn,kjdfkj,kjkjkjekrjkj'
b=re.findall(r"\w*@\w*.\w*,",a)
print(b)


