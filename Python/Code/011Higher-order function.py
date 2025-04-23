# 高阶函数，就是让函数的参数能够接收别的函数。
print(abs)
f=abs  #abs就是指向abs函数的变量，因此可以另造一个变量指向该abs函数
print(f(-1))

#将函数作为另一个函数的参数==高阶函数
def func(x,y,f):
    return f(x) + f(y)  #运用传递进来的变量名（指向函数）来调用原函数

print(func(-2,-5,abs))