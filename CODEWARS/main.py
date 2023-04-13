from typing import List


def is_valid(s: str):
    d = {"(": ")",
         "[": "]",
         "{": "}"}

    stack = []
    for i in s:
        if i in d:
            stack.append(i)
        elif len(stack) == 0 and d[stack.pop()] != i:
            return False
    return len(stack) == 0


print(is_valid("{}{}}}"))


def reverse_matrix(matrix: List):
    n = len(matrix)
    s = 0
    for i in range(n // 2):
        for j in range(n // 2):
            s += max(matrix[i][j], matrix[i][n - j - 1], matrix[n - i - 1][j], matrix[n - i - 1][n - j - 1])
    return s


print(reverse_matrix([[112, 42, 83, 119],
                [56, 125, 56, 49],
                [15, 78, 101, 43],
                [62, 98, 114, 108]]))
