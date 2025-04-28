# 偏函数的使用
# int函数的拓展
print(int('10', base=8))  # 转换成base进制的整形

def int8(x, base=8):  # 我需要大量转换成八进制
    return int(x, base)
for i in [str(x) for x in range(22,25)]:  # bin() converts to binary, [2:] removes '0b' prefix
    print(int8(i))


# -----------------------------------------------
# functools.partial就是帮助我们创建一个偏函数的，不需要我们自己定义int2()
import functools
int2 = functools.partial(int, base = 2)
print(int2('10010'))   # 相当于：kw = { 'base': 2 }   int('10010', **kw)

max2 = functools.partial(max, 1000)
# 相当于10作为*args的一部分自动加到左边
print(max2(1, 4, 6, 5))