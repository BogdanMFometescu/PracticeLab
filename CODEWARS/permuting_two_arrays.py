def two_arrays(k: int, A: list, B: list):
    a = sorted(A)
    b = sorted(B)[::-1]
    h = list(map(sum, zip(a, b)))
    print(b)
    print(h)
    return "YES" if min(h) >= k else "NO"


print(two_arrays(5, [1, 2, 2, 1], [3, 3, 3, 4]))
