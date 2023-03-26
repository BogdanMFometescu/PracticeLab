
def recursive_binary_search_p(sequence, target):
    if len(sequence) == 0:
        return False
    else:
        midpoint = len(sequence) // 2

        if sequence[midpoint] == target:
            return True
        else:
            if sequence[midpoint] < target:
                return recursive_binary_search_p(sequence[midpoint+1:], target)
            else:
                return recursive_binary_search_p(sequence[:midpoint], target)


li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

result = recursive_binary_search_p(li,12)
print(result)