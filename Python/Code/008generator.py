# 一边循环一边计算的机制，称为生成器：
l=(i for i in range(10))
print(l)
print(next(l))
print()
for i in l:  #一般用迭代的方式，用了next，迭代开始就往后走了
    print(i)

print()
def fib(x):
    n,a,b=0,0,1
    while(x>n):
        print(b,end=',')
        a,b=b,a+b
        n+=1
    return 'all'
print(fib(4))


#将普通函数变为一个生成器函数，即generator function
def fib(x):
    n,a,b=0,0,1
    while(x>n):
        yield b   #生成器的另一种方式
        a,b=b,a+b
        n+=1
    return 'all'
f=fib(10)
print(f)

# 变成generator的函数，在每次调用next()的时候执行，遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行。
def odd():
    print(1)
    yield 1
    print(2)
    yield 2
    print(3)
    yield 3   #多次调用generator函数会创建多个相互独立的generator。
o=odd()
next(o)
next(o)  #从上次返回的yield处开始执行
next(o)
# next(o)  #报错，已经结束了