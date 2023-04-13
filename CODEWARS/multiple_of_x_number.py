def solution(number):
    nums = []
    for item in range(number):
        if item % 3 ==0 or item %5 ==0:
            nums.append(item)
        elif item % 3 ==0 and item %5 ==0:
            nums.append(item)
        elif number < 0:
            return -1

    result = sum(nums)
    return result

print(solution(10))