

# python大题

## 斐波那契数列(Fibonacci)

```python
#方法1
def fib(n):
    if n in (1,2):
        return 1
   	else if n==0:
        return 0
    else:
        return fib(n-2)+fib(n-1)
# 输出了第10个斐波那契数列
print fib(10)
#方法2
def fib(n):
    a, b = 1, 1
    for i in range(n-1):
        a, b = b, a+b
    return a
print fib(10)

#斐波那契数列中大于或者等于t的第一个数。
def fib(t):
    a,b=1,1
    while(t>a):
        a,b=b,a+b
    print(a)
fib(7)
```

## 素数

```python
#素数问题
def sushu(n):
	for i in range(2,int(sqrt(n))+1): #内层循环，检查是否满足素数
        if(n%i==0):
            flag=1
            break
    if(flag==0):
        print(n,end=",")
sushu(100)
```

> sqrt是内置函数
