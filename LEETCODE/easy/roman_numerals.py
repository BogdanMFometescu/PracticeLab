# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

# I can be placed before V (5) and X (10) to make 4 and 9.
# X can be placed before L (50) and C (100) to make 40 and 90.
# C can be placed before D (500) and M (1000) to make 400 and 900.
# Given a roman numeral, convert it to an integer.

# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000


def roman_numerals(s: str) -> int:
    numerals = {'I': 1,
                'V': 5,
                'X': 10,
                'L': 50,
                'C': 100,
                'D': 500,
                'M': 1000,
                }







# INPUT
# We have as input a string representing roman numerals

# Solution


# OUTPUT
# We return an integer converting the roman numerals

print(roman_numerals('XX'))


def romanToInt( s: str) -> int:

    # rti is a dict for roman to intgers values
    rti = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}

    # ans is for our sum value
    ans=0

    # for loop till len(s)-1 cause for last Roman Value we cant compare
    for i in range(len(s)-1):
        if rti[s[i]] < rti[s[i+1]]:
            ans = ans - rti[s[i]]
        else:
            ans = ans + rti[s[i]]

    # So we add the last value and return the final ans
    return ans+rti[s[-1]]


print(romanToInt('MCMLIV'))