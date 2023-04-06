# Reverse integer
# Given a signed 32-bit integer x, return x with its digits reversed.
# If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
#

class Solution:
    @staticmethod
    def reverse(x: int) -> int:
        x = list(str(x))
        x.reverse()
        if x[-1] == '-':
            x = [x[-1]] + x
            x.pop(-1)
        x = "".join(x)
        if -2 ** 31 <= int(x) <= ((2 ** 31) - 1):
            return int(x)
        else:
            return 0


solution = Solution()
print(solution.reverse(-123))


