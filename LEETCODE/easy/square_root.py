# Given a non-negative integer x, return the square root of x rounded down to the nearest integer.
# The returned integer should be non-negative as well.

# You must not use any built-in exponent function or operator.


# Input: x = 8
# Output: 2
# Explanation: The square root of 8 is 2.82842..., and since we round it down to the nearest integer, 2 is returned.


def square_root(x: int) -> int:
    left, right = 0, x

    while left<=right:
        midpoint = (left + right)//2
        if midpoint * midpoint > x:
            right = midpoint-1
        elif midpoint*midpoint< x:
            left = midpoint+1

        else:
            return midpoint

    return  right

print(square_root(88))