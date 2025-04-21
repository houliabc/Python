# -*- encoding = utf-8 -*-
# author : houliabc

d={'a':1,'b':2}
d['c']=2
# print(d)
print(d.pop('d',0))  #失败则返回0
print(d.get('e',0))
print(d)


#可变对象
a = ['c', 'b', 'a']
a.sort()
print(a)



#不可变对象
a = 'abc'
print(a.replace('a', 'A'))
print(a)
