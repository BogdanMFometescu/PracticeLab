# Given a sorted array of distinct integers and a target value, return the index if the target is found.
# If not, return the index where it would be if it were inserted in order.

# You must write an algorithm with O(log n) runtime complexity.

def search_insert(nums, target):
    position = 0

    while position <= len(nums):
        if nums[position] == target:
            return position
        else:
            nums.append(target)
            nums.sort()
            x = nums.index(target)
            return x


print(search_insert([1, 3, 5, 6], 7))
