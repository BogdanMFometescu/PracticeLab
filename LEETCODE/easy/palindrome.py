# Given an integer x, return true if x is a palindrome, and false otherwise.

# Solution using slicing

def is_palindrome(x: int) -> bool:
    if str(x) == str(x)[::-1]:
        return True
    else:
        return False


print(is_palindrome(121))
