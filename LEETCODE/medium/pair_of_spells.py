# You are given two positive integer arrays spells and potions, of length n and m respectively, where spells[i]
# represents the strength of the ith spell and potions[j] represents the strength of the jth potion.
# You are also given an integer success. A spell and potion pair is considered successful
# if the product of their strengths is at least success.
# Return an integer array pairs of length n where pairs[i] is the number of potions
# that will form a successful pair with the ith spell.
from typing import List


# Example :

# Input: spells = [5,1,3], potions = [1,2,3,4,5], success = 7
# Output: [4,0,3]
# Explanation:
# - 0th spell: 5 * [1,2,3,4,5] = [5,10,15,20,25]. 4 pairs are successful.
# - 1st spell: 1 * [1,2,3,4,5] = [1,2,3,4,5]. 0 pairs are successful.
# - 2nd spell: 3 * [1,2,3,4,5] = [3,6,9,12,15]. 3 pairs are successful.
# Thus, [4,0,3] is returned.
#

class Solution:
    @staticmethod
    def successful_pairs(spells: List[int], potions: List[int], success: int) -> List[int]:
        product = []
        length_of_cases = len(spells)
        final_res = []
        for spell in spells:
            for potion in potions:
                result = spell * potion
                product.append(result)

        start_index = 0
        end_index = len(potions)
        step = 1

        while step <= length_of_cases:
            case = len(list(filter(lambda x: x >= success, product[start_index:end_index])))
            start_index = end_index
            end_index = end_index + len(potions)
            step += 1

            final_res.append(case)

        return final_res


solution = Solution()
print(solution.successful_pairs([5, 1, 3], [1, 2, 3, 4, 5], 7))
