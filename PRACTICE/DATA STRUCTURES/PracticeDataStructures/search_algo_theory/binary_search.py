# Binary search
# 1. find the middle element in a list
# 2. if it matches query number, return the middle position as the answer
# 3. if it's less than the query number, then search the first half of the list
# 4. if it's greater than the query number, then search the second half of the list
# 5. If no more elements remain , return -1


li_ascending = [1, 2, 3, 4, 5, 6, 7, 8]
li_descending = [9, 8, 7, 6, 5, 4, 3, 2]
item = 5


# For lists with elements sorted in descending order
def test_location(cards, query, mid):
    mid_number = cards[mid]
    if mid_number == query:
        if mid - 1 >= 0 and cards[mid - 1] == query:
            return "left"
        else:
            return "found"
    elif mid_number < query:
        return "left"
    else:
        return "right"


def locate_cards(cards, query):
    lo, hi = 0, len(cards) - 1

    while lo <= hi:
        mid = (lo + hi) // 2
        result = test_location(cards, query, mid)

        if result == "found":
            return mid
        elif result == "left":
            hi = mid - 1
        elif result == "right":
            lo = mid + 1
    return -1


# Big O Complexity
# O(log N) and O(1)

result_descending = locate_cards(li_descending, item)
print(result_descending)


def binary_search_method(sequence, item):
    low = 0
    high = len(sequence) - 1

    while low <= high:
        midpoint = (low + high) // 2
        midpoint_value = sequence[midpoint]

        if item == midpoint_value:
            return midpoint
        elif item < midpoint_value:
            high = midpoint - 1
        else:
            low = midpoint + 1
    return -1


result_ascending = binary_search_method(li_ascending, item)
print(result_ascending)
