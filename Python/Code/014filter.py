def isOdd(n):
    return n % 2 == 1  #奇数
print(list(filter(isOdd, [1, 2, 3, 4, 5])))  # 也是返回惰性序列

def noEmpty(s):
    return s and s.split()
print(list(filter(noEmpty, ['a', ' ', '', None, 'C', ' '])))

# -------------------------------------------------------------
# 用filter求素数
def oddIter():
    n = 1
    while 1:
        n += 2
        yield n
def noSu(n):
    return lambda x: x % n > 0

def primes():   # 新的生成器，不断返回下一个素数
    yield 2
    it = oddIter()  # 初始序列的迭代器
    while 1:
        n = next(it)  # 依次访问序列内容
        yield n
        it = filter(noSu, it)  # 过滤非素数
for i in primes():
    if i < 100:
        print(i)
    else:
        break


# -------------------------------------------------------------
def is_palindrome(n):
    return str(n) == str(n)[::-1]

# 测试:
output = filter(is_palindrome, range(1, 1000))
print('1~1000:', list(output))
if list(filter(is_palindrome, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191]:
    print('测试成功!')
else:
    print('测试失败!')
