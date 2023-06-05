# Given an array of integers nums and an integer target, return indices of the
# two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.
from typing import List


def two_sums(nums: List, target):
    complement_map = {}

    for i, num in enumerate(nums):
        complement = target - num
        if complement in complement_map:
            return [complement_map[complement], i]
        complement_map[num] = i


# INPUT = a list of integers, unsorted and a target integer

# Solution
# We use a hashmap to store the complement and return a list of number and complement
#  is the difference between target and number

# OUTPUT = a list of index of the numbers which sum is equal to target

print(two_sums([2, 11, 7, 15], 9))
