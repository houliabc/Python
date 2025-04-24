# map()函数接收两个参数，一个是函数，一个是Iterable，map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回。
#Iterator是惰性序列
def f(x):
    return x**2
m = map(f, [1, 2, 3, 4])
print(list(m))
#相当于next到最后了，也就是“迭代完了”
for i in m:
    print(i)

#map(函数名，迭代对象)
print(list(map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9])))



#-----------------------------------------------------
#reudce（函数， ）
from functools import reduce
def add(x,y):
    return x + y
print(reduce(add,[1, 3, 5, 7, 9]))

def fn(x,y):
    return x * 10 + y
print(reduce(fn, [1, 3, 5, 7, 9]))  #相当于乘了五个10

#-----------------------------------------------------

#reduce配合map使用
def char2num(s):
    digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    return digits[s]
    #不完全等同，因为如果字符串是数字以外的内容就会有问题了
    # return int(s)
print(reduce(fn, map(char2num, '13579')))

#-----------------------------------------------------
DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
def char2num(s):
    return DIGITS[s]

def str2int(s):
    return reduce(lambda x, y: x * 10 + y, map(char2num, s))
print(str2int('13579'))
