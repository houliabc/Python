#迭代
#把某个（只能是一个，但可以用列表或元祖包含多个）可迭代对象变成“索引-元素”队，在for中同时迭代索引和元素本身
for i,j in enumerate(['a','b','c']):
    print(i,j)

#zip配合enumerate
for i,(j,k) in enumerate(zip([1,2],(4,6))):  #这里for后面必须只能是一项，因为enumerate只会生成两项，但可以用元祖表示
    print(i,j,k)


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
