# For a non-degenerate triangle, its sides should follow these constraints,
# A + B > C    and
# B + C > A    and
# C + A > B
# where A, B and C are length of sides of the triangle.

def maximum_perimeter_triangle(sticks):
    sticks.sort(reverse=True)
    for i in range(len(sticks) - 2):
        a = sticks[i]
        b = sticks[i + 1]
        c = sticks[i + 2]
        if a < b + c:
            return c, b, a
    return [-1]


print(maximum_perimeter_triangle([1, 2, 3, 4, 5, 10, 11, 33, 42]))

arr = [1, 2, 3, 4, 5, 6, 7,8,9,10,11]

print(len(arr))

for i in range(len(arr) - 3):
    a = arr[i]
    b = arr[i + 1]
    c = arr[i + 2]
    d = arr[i + 3]
    print(a, b, c, d)
