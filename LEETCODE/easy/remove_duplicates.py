

def remove_duplicates(nums):
    nums [:] = sorted(set(nums))
    return len(nums)



nums = [1,4,5,7,7,8,8,99,]
print(nums[:])
