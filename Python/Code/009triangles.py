#杨辉三角线
#gpt版本
def triangles():
    row = [1]  # 初始化第一行
    while True:  #生成器可以直接while True
        yield row  # 生成当前行
        # # 计算下一行：在当前行的首尾各加一个0，然后逐项相加
        # row = [x + y for x, y in zip([0] + row, row + [0])]
        #or
        # 计算下一行：当前行的相邻元素相加，首尾补1
        row = [1] + [row[i] + row[i+1] for i in range(len(row)-1)] + [1]

#我的
# def triangles():
    # results=[]
    # for i in range(100):
    #     if i==0:
    #         l=[1]
    #     elif i==1:
    #         l=[1,1]
    #     else:
    #         l=[1]
    #         for j in range(1,i):
    #             l.append(results[i-1][j-1]+results[i-1][j])
    #         l.append(1)
    #     results.append(l)
    #     yield l

# 期待输出:
# [1]
# [1, 1]
# [1, 2, 1]
# [1, 3, 3, 1]
# [1, 4, 6, 4, 1]
# [1, 5, 10, 10, 5, 1]
# [1, 6, 15, 20, 15, 6, 1]
# [1, 7, 21, 35, 35, 21, 7, 1]
# [1, 8, 28, 56, 70, 56, 28, 8, 1]
# [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
n = 0
results = []
for t in triangles():
    results.append(t)
    n = n + 1
    if n == 10:
        break

for t in results:
    print(t)

if results == [
    [1],
    [1, 1],
    [1, 2, 1],
    [1, 3, 3, 1],
    [1, 4, 6, 4, 1],
    [1, 5, 10, 10, 5, 1],
    [1, 6, 15, 20, 15, 6, 1],
    [1, 7, 21, 35, 35, 21, 7, 1],
    [1, 8, 28, 56, 70, 56, 28, 8, 1],
    [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
]:
    print('测试通过!')
else:
    print('测试失败!')
