# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".


from typing import List


def longest_com_prefix(strs: List) -> str:
    pass





l = ["flower", "flow", "flight"]

res = list(zip(*l))
print(res)


def longest_common_prefix(strs: List[str]) -> str:
    match = 0

    for vals in zip(*strs):
        if len(set(vals)) == 1:
            match += 1
        else:
            break

    return strs[0][:match]


print(longest_common_prefix(["flower", "flow", "flight"]))




def find_common(strs : List)-> str:
    for i, char in enumerate(strs[0]):
        for word in strs[1:]:
            if i >= len(word) or  word[i] != char:
                return strs[0][:i]
    return strs[0]        



find_common(l)