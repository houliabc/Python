# -*- encoding = utf-8 -*-
# author : houliabc
def my_abs(x):
    if not isinstance(x, (int, float)):  #只允许整数和浮点数
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x
    return 1, 2  #函数可以返回多个值，返回的是一个元祖
