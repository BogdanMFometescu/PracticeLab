# Given two strings needle and haystack, return the index of the first occurrence of needle in haystack,
# or -1 if needle is not part of haystack.


# Input: haystack = "sadbutsad", needle = "sad"
# Output: 0
# Explanation: "sad" occurs at index 0 and 6.
# The first occurrence is at index 0, so we return 0.


def find_occurrence(haystack, needle):
    end = len(needle)
    for start in range(len(haystack)):
        if haystack[start:end] == needle:
            return start
        end += 1
    return -1


print(find_occurrence('hello', 'll'))
