def find_bugger(num):
    if num < 10:
        return 0
    s = str(num)
    total = 1
    for i in s:
        total = total * int(i)

    return 1 + find_bugger(total)


print(find_bugger(11))
