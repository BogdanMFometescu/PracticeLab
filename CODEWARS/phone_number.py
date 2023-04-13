# Write a function that accepts an array of 10 integers (between 0 and 9), that returns a
# string of those numbers in the form of a phone number.

def create_phone_number(arr: list):
    prefix = arr[0:3]
    middle = arr[3:6]
    end = arr[6:]
    prefix.insert(0,"(")
    prefix.append(")")
    s = "".join(str(e) for e in prefix)
    m = "".join(str(e) for e in middle)
    e = "".join(str(e) for e in end)
    final = s + " " + m + "-" + e
    print(final)


def create_phone_number2(n):
    m = ''.join(map(str, n))
    return f"({m[:3]}) {m[3:6]}-{m[6:]}"


def create_phone_number3(n):
    return "({}{}{}) {}{}{}-{}{}{}{}".format(*n)

create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])

# => returns "(123) 456-7890"

# Make a list for prefix, mid and last using slice
# Add () , space and -
# Make a single string
