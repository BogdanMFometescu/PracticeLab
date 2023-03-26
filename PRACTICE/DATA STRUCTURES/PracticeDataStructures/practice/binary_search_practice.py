# In binary search the list MUST be ordered
# Ascending order list( we compare item with midpoint)
def binary_search_asc(sequence, target):
    low, high = 0, len(sequence) - 1

    while low <= high:
        midpoint = (low + high) // 2
        midpoint_value = sequence[midpoint]

        if midpoint_value == target:
            return midpoint
        elif target < midpoint_value:
            high = midpoint - 1
        else:
            low = midpoint + 1
    return -1


result_bs_asc = binary_search_asc([1, 2, 3, 4, 5, 6, 7, 8], 5)
print(result_bs_asc)


# Descending order list (we compare midpoint with item)

def binary_search_des(sequence, target):
    low, high = 0, len(sequence) - 1

    while low <= high:
        midpoint = (low + high) // 2
        midpoint_value = sequence[midpoint]

        if midpoint_value == target:
            return midpoint
        elif midpoint_value < target:
            high = midpoint - 1
        elif midpoint_value > target:
            low = midpoint + 1
    return -1


result_bs_des = binary_search_des([9, 8, 7, 6, 5, 4, 3, 2, 1], 1)
print(result_bs_des)
