def reFunction(*args):
    def sum(n):
        sum = 0
        for i in args:
            sum += i
        return sum + 1
    return sum
f = reFunction(1, 2, 3, 4, 5)
print(f)  # 输出的是函数对象，不会立刻执行
print(f(1))  # 只有调用f()时，才会执行sum函数，返回结果


# --------------------------------------------------------------
#  closure：闭包：内部函数引用了外部函数的局部变量
def count():
    fs = []
    for i in range(1, 4):
        def f():
            return i * i  # 内部函数引用了外部函数的局部变量i，称之为闭包
        fs.append(f)  # 将函数对象f添加到列表中
        print(fs)  # 函数对象，所以需要外面加括号
    return fs  
f1, f2, f3 = count()    #闭包中的变量绑定发生在 函数被调用时，而不是在函数被定义时，所以当此时调用函数count时，又到了fs并传递参数形成fs（），也就是说等到此时i=3了才执行的fs（）三次
print(f1 , f1(), f2(), f3())  # 这里的调用f1(),f2(),f3()的值难以想象

#  ！返回闭包时牢记一点：返回函数不要引用任何循环变量，或者后续会发生变化的变量。


# --------------------------------------------------------------
# 如果一定要引用循环变量怎么办？方法是再创建一个函数，用该函数的参数绑定循环变量当前的值，无论该循环变量后续如何更改，已绑定到函数参数的值不变：
def count():
    def f(j):
        def g():
            return j*j
        return g
    fs = []
    for i in range(1, 4):
        fs.append(f(i)) # f(i)立刻被执行，因此i的当前值被传入f()
    return fs
f1, f2, f3 = count()  
print(f1(), f2(), f3())  # 这里的调用f1(),f2(),f3()的值就正常了