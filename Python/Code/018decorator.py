# 学习装饰器
def now():
    print('2024-6-1')
f = now
print(f.__name__)  # 拿到函数的名字

# 在代码运行期间动态增加功能的方式，称之为“装饰器”

# 装饰器就是一个返回函数的高阶函数
def log(func):
    def wrapper(*arg, **kw):  # kw是接受关键字参数，可以理解为一个字典
        print('call %s():' % func.__name__)
        return func(*arg, **kw)
    return wrapper

#上面的log()函数就是一个decorator，它接收一个函数作为参数，并返回一个函数
@log   # 装饰器的语法糖
def now():
    print('2024-6-1')
# 等价于now = log(now)

now()  # 调用函数


# ---------------------------------------------------------------------
# 如果decorator本身需要传入参数，那就需要编写一个返回decorator的高阶函数
def log(text):
    def decorator(func):
        def wrapper(*arg, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*arg, **kw)
        return wrapper
    return decorator
# 调用方式
@log('execute')
def now():
    print('2024-6-1')
# 等价于now = log('execute')(now)

now()
print(now.__name__)  # wrapper

# 解决方法：使用functools.wraps
import functools
def log(func):
    @functools.wraps(func)  # 将func的属性复制到wrapper上
    def wrapper(*arg, **kw):
        print('call %s():' % func.__name__)
        return func(*arg, **kw)
    return wrapper

# 练习---------------------------------------------------------------------
# 请设计一个decorator，它可作用于任何函数上，并打印该函数的执行时间：
import time, functools

def metric(fn):
    @functools.wraps(fn)  # 将fn的属性复制到wrapper上
    def wrapper(*arg, **kw):
        print('%s executed in %s ms' % (fn.__name__, 10.24))
        return fn
    return wrapper

# 测试
@metric
def fast(x, y):
    time.sleep(0.0012)
    return x + y

@metric
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z

f = fast(11, 22)
s = slow(11, 22, 33)
if f != 33:
    print('测试失败!')
elif s != 7986:
    print('测试失败!')
else :
    print('测试成功！')


# 请编写一个decorator，能在函数调用的前后打印出'begin call'和'end call'的日志。
# 再思考一下能否写出一个@log的decorator，使它既支持：
def log(func):
    @functools.wraps(func)
    def wrapper(*arg, **kw):
        print('begin call %s():' % func.__name__)
        result = func(*arg, **kw)
        print('end call %s():' % func.__name__)
        return result
    return wrapper

@log
def f():
    pass
f()