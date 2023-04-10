# There are two  n element arrays of integers A  and B  .
# Permute them into some A' and B'  such that the relation  A'[i] +B'[i] >=k  holds for all i were 0<=i<n.
# return YES if some permutation  A'  B',  satisfying the relation exists. Otherwise, return NO.

def permuting_arr(k: int, A: list, B: list) -> str:
    a = sorted(A)
    b = sorted(B)[::-1]
    h = list(map(sum, zip(a, b)))
    return "YES" if min(h) >= k else "NO"


print(permuting_arr(5, [1, 2, 2, 1], [3, 3, 3, 4]))
print(permuting_arr(10, [2, 1, 3], [7, 8, 9]))
