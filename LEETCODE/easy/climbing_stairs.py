# You are climbing a staircase. It takes n steps to reach the top.

# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?


def climb_stairs(n: int) -> int:
    if n == 2:
        res = 2
    else:
        res = (n - 1) + (n - 2)
    return res


print(climb_stairs(5))
