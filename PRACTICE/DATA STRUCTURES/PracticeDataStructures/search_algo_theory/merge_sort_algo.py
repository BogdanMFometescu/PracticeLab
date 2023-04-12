"""
Divide: Find the midpoint of the list and divide into sublist
Conquer: Recursively sort the sublist created in the previous step
Combine: Mere the sorter sublist created in the previous step
"""


def merge_sort_alg(sequence):
    if len(sequence) <= 1:
        return sequence
    # Divide
    left_half, right_half = split_seq(sequence)

    # Conquer
    left = merge_sort_alg(left_half)
    right = merge_sort_alg(right_half)

    # Combine
    return merge_seq(left, right)


def split_seq(sequence):
    """Divide the unsorted list at midpoint into sublists
    Returns two sublist : left_half, right_half
    """
    midpoint = len(sequence) // 2
    left = sequence[:midpoint]
    right = sequence[midpoint:]

    return left, right


def merge_seq(left, right):
    """Merges two lists , sorting them in the process
    Returns merged list"""
    li = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            li.append(left[i])
            i += 1
        else:
            li.append(right[j])
            j += 1

    while i < len(left):
        li.append(left[i])
        i += 1

    while j < len(right):
        li.append(right[j])
        j += 1

    return li


li_test = [54, 26, 93, 67, 31, 33, 45, 24, 99 ]

result = merge_sort_alg(li_test)
print(result)
