def quick_sort_p(sequence):
    length = len(sequence)
    if length <= 1:
        return sequence
    else:
        pivot = sequence.pop()

    items_lower = []
    items_greater = []

    for item in sequence:
        if item > pivot:
            items_greater.append(item)
        else:
            items_lower.append(item)

    return quick_sort_p(items_lower) + [pivot] + quick_sort_p(items_greater)


li_test = [66, 32, 55, 535, 53523, 22, 41, 1]

result = quick_sort_p(li_test)
print(result)
