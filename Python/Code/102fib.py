# # 题目描述：计算 n! 末尾有多少个零（如 10! = 3628800，末尾有 2 个零）。
# n = int(input("请输入一个整数 n: "))
# s = 1
# for i in range(1, n + 1):
#     s *= i
# print(str(s).count('0'))  # 计算末尾有多少个零

# # 题目描述：计算斐波那契数列的第 N 项（N 可能非常大，如 10^6）。
# n = int(input("请输入一个整数 n: "))
# a, b = 0, 1
# for _ in range(n):
#     a, b = b, a + b
# print(a)

text = "ababcabcabc"
pattern = "abc"
# 查找字符串中所有匹配模式的起始位置
positions = []
start = 0
while True:
    # pos = text.find(pattern)
    pos = text.find(pattern, start)
    if pos == -1:
        break
    positions.append(pos)
    start = pos + 1
print(positions)

import re
# 题目描述：将文本中的所有 old 子串替换为 new
text = "ababcabcabc"
old = "abc"
new = "xyz"
# 使用正则表达式进行替换
text = re.sub(old, new, text)
print(text)  # 输出: abxyzabxyzabxyz