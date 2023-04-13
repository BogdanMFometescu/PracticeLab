# here is a large pile of socks that must be paired by color. Given an array of integers representing
# the color of each sock, determine how many pairs of socks with matching colors there are.


def sock_merchant(arr: list) -> int:
    duplicates = []
    count = 0
    for item in arr:
        a = arr.count(item)
        duplicates.append(a)

    results = set(list(zip(arr, duplicates)))

    for item in results:
        count += item[1] // 2

    return count


print(sock_merchant([10, 20, 20, 10, 10, 30, 50, 10, 20]))
