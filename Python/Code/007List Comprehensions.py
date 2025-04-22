#使用if＋for的列表生成式
from collections.abc import Iterable
l=[i for i in range(5) if i>3]
print(l)

#两层for+if
x=[i+j for i in "abc" for j in 'def' if j=='d']
print(x)

#if+else+for    注：如果没有else，则if不能在for前面
z=[x if x%2==0 else -x for x in range(10)]  #偶数正常，基数负数
print(z)




#练习
L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [i.lower() for i in L1 if i==str(i)]

# 测试:
print(L2)
if L2 == ['hello', 'world', 'apple']:
    print('测试通过!')
else:
    print('测试失败!')
# print(isinstance(L1,Iterable))