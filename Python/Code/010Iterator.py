#注意区分迭代对象和迭代器
from collections.abc import Iterable,Iterator
#迭代对象
print(isinstance({},Iterable))

#迭代器：可以被next（）调用的
print(isinstance([],Iterator))  #列表只是迭代对象，而非迭代器
print(isinstance((i for i in range(3)),Iterator))

# 可以把这个数据流看做是一个有序序列，但我们却不能提前知道序列的长度，只能不断通过next()函数实现按需计算下一个数据，所以Iterator的计算是惰性的，只有在需要返回下一个数据时它才会计算。

#将迭代对象转换为迭代器
print(isinstance(iter([]),Iterator))




#遍历的方式
for x in [1, 2, 3, 4, 5]:
    pass
#等价于
#用迭代器的方式
it = iter([1, 2, 3, 4, 5])
# 循环:
while True:
    try:
        # 获得下一个值:
        x = next(it)
    except StopIteration:
        # 遇到StopIteration就退出循环
        break
