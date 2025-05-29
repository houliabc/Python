import itertools

ls = [1, 2, 3]
for p in itertools.permutations(ls, 2):
    print(p)
print()
for p in itertools.combinations(ls, 2):
    print(p)
print()
for i in itertools.product(ls, repeat=2):
    print(i)

print([1,2]+[3,4])  # 列表拼接
print('---')


def solve_sudoku(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == '.':
                for num in '123456789':
                    if is_valid(board, i, j, num):
                        board[i][j] = num
                        if solve_sudoku(board):
                            return True
                        board[i][j] = '.'
                return False
    return True

def is_valid(board, row, col, num):
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False
    start_row, start_col = (row // 3) * 3, (col // 3) * 3
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False
    return True

# 示例输入处理
# board = [
#     ['5', '3', '.', '.', '7', '.', '.', '.', '.'],
#     ['6', '.', '.', '1', '9', '5', '.', '.', '.'],
#     ['.', '9', '8', '.', '.', '.', '.', '6', '.'],
#     ['8', '.', '.', '.', '6', '.', '.', '.', '3'],
#     ['4', '.', '9', '8', '.', '3', '.', '.', '1'],
#     ['7', '.', '.', '.', '2', '.', '.', '.', '6'],
#     ['.', '6', '.', '.', '.', '.', '2', '8', '.'],
#     ['.', '.', '.', '4', '1', '9', '.', '.', '5'],
#     ['.', '.', '.', '.', '8', '.', '.', '7', '9']
# ]
# solve_sudoku(board)
# for row in board:
#     print(''.join(row))

from collections import Counter
import re
text = 'remove an existing key one level down remove an existing key one level down'
words = re.findall(r'\w+', text)
print(Counter(words).most_common(2))  # 获取出现频率最高的两个单词及其频率

print(pow(10, 6, 7))  # 计算 10^6 mod 7 的结果

from math import comb

n, k = map(int, input().split())
print(comb(n, k))  # 直接调用组合数函数，无需担心溢出