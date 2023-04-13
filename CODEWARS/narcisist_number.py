# A Narcissistic Number (or Armstrong Number) is a positive number which is the sum of its own digits,
# each raised to the power of the number of digits in a given base. In this Kata, we will restrict ourselves to decimal
# (base 10).
#
# For example, take 153 (3 digits), which is narcissistic:
# 1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153

def narc_number(num):
    s = str(num)
    expo = len(s)
    n = [x for x in s]
    result = sum(map(lambda x: (int(x) ** expo), n))
    return True if result == num else False


print(narc_number(153))


# Take each digit in the num and make a list
# Sum the exponential results
# Check if the result is equal to the initial number

def narcissistic2(value):
    return value == sum(int(x) ** len(str(value)) for x in str(value))
