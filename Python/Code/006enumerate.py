#把某个可迭代对象变成“索引-元素”队，在for中同时迭代索引和元素本身
for i,j in enumerate(['a','b','c']):
    print(i,j)



def findMinAndMax(L):
    return (None, None)

# 测试
if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')
