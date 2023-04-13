# Input

segment = [2, 2, 1, 3, 2]
day = 4  # this is the sum of the elements
month = 2  # length of the segments which have as result the birthday

# Output
result = 2  # [2,2], [1,3]


def sub_array(s: list, d: int, m: int) -> int:
    count = 0
    start = 0
    w_sum = 0
    for end in range(len(s)):
        w_sum += s[end]
        if end + 1 >= m:
            if w_sum == d:
                count += 1
            w_sum -= s[start]
            start += 1
    return count


print(sub_array([2, 2, 1, 3, 2], 4, 2))
