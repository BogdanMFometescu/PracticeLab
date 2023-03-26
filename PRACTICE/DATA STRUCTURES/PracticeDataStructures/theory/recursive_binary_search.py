# In binary search the list must be ordered
def recursive_binary_search(sequence, target):
    # Check if the list is empty
    if len(sequence) == 0:
        return False
    else:
        # Set the midpoint
        midpoint = len(sequence) // 2

        # Check if midpoint is equal to target value
        if sequence[midpoint] == target:
            return True
        else:
            if sequence[midpoint] < target:
                # Recursion - we give new list to search on the method, "return" is crucial here
                return recursive_binary_search(sequence[midpoint + 1:], target)
            else:
                # Recursion - we give new list to search on the method, "return" is crucial here
                return recursive_binary_search(sequence[:midpoint], target)


li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

Result = recursive_binary_search(li, 12)
print(Result)
