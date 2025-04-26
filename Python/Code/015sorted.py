# 高阶函数：sorted
# sorted(iterable, key=None, reverse=False)
print(sorted([36, 5, -12, 9, -21], key = abs))  # 默认升序排列，且按照abs函数也就是绝对值排序

print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse = True))  # 降序排列，且按照str.lower函数也就是小写字母排序