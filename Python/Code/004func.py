# -*- encoding = utf-8 -*-
# author : houliabc
from abstest import my_abs
print(my_abs(-9))  #定义默认参数要牢记一点：默认参数必须指向不变对象！

#可变参数
def calc(numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum
nums = [1, 2, 3]

calc(*nums)  #对列表进行解包之后传递进去函数中作为多个参数，也就是可变函数



def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)

extra = {'city': 'Beijing', 'job': 'Engineer'}
person('Jack', 24, **extra)  #对字典解包后作为关键字参数传递给带关键字参数的函数