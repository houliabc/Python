def normalize(name):
    name = name.lower()
    name = name[0].upper() + name[1:]
    return name

# 测试:
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)

#--------------------------------------------
from functools import reduce  #其实是内置的，不用也可以

def prod(L):
    return reduce(lambda x, y: x * y, L)

print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
if prod([3, 5, 7, 9]) == 945:
    print('测试成功!')
else:
    print('测试失败!')

#--------------------------------------------
from functools import reduce

# 把字符串'123.456'转换成浮点数123.456：
def str2float(s):
    l = s.split('.')
    digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '.': '.'}
    positive = reduce(lambda x, y: x * 10 + y, map(lambda x: digits[x], l[0]))
    # nagative = round(reduce(lambda x, y: x / 10 + y, map(lambda x: digits[x], l[1][::-1])) / 10, len(l[1]))
    nagative = reduce(lambda x, y: x / 10 + y, map(lambda x: digits[x], l[1][::-1])) * 0.1
    return positive + nagative

print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')
