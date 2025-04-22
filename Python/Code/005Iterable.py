from collections.abc import Iterable

#判断一个对象时候是可迭代对象
print(isinstance('abc',Iterable))

print(isinstance(123,Iterable))