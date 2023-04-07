# Problem: Sean invented a game involving a matrix where each cell of the matrix contains an integer.
# He can reverse any of its rows or columns any number of times. The goal of the game is to maximize the sum
# of the elements in the n X n submatrix located in the upper-left quadrant of the matrix 2n X 2n.

# For example, given the matrix:
#
# 1 2
# 3 4
# It is 2 X 2, so we want to maximize the top left matrix that is 1 X 1.
#
# Reverse 2nd row
# Reverse Ist column we get,
# 4 2
# 1 3
# The maximal sum is 4
#
# Example 2:
#
# 112 42 83 119
# 56 125 56 49
# 15 78 101 43
# 62 98 114 108
# The maximal sum is 414


def reverse_matrix(matrix) -> int:
    n = len(matrix)  # length of the matrix
    s = 0  # sum of max numbers, this is the result

    for i in range(n // 2):
        # i - row
        # j - column
        for j in range(n // 2):
            # We find the max value for each  mirrored item and sum it.
            s += max(matrix[i][j], matrix[i][n - j - 1], matrix[n - i - 1][j], matrix[n - i - 1][n - j - 1])
    return s


# Matrix looks like this, with mirrored items.

# ABBA
# CDDC
# CDDC
# ABBA


print(reverse_matrix([[112, 42, 83, 119],
                      [56, 125, 56, 49],
                      [15, 78, 101, 43],
                      [62, 98, 114, 108]]))
