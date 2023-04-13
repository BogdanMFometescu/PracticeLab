def is_triangle(a, b, c):
    n = [a, b, c]
    n.sort()
    if n[0] + n[1] <= n[2]:
        return False
    else:
        return True


def is_triangle_second(a, b, c):
    return a < b + c and b < c + a and c < a + b
