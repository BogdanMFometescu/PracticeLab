# The filter() function returns an iterator where the items are filtered through
# a function to test if the item is accepted or not.
# It accepts as parameter a function  and an iterable which needs to be filtered

numbers = [1, 2, 3, 5, 5, 67, 5, 8, 5, 4]

print("*" * 23)
odd_numbers = list(filter(lambda x: (x % 2 != 0), numbers))
prime_numbers = list(filter(lambda x: (x % 2 == 0), numbers))
higher_than_x = list(filter(lambda x: (x > 10), numbers))
two_conditions = list(filter(lambda x: (x > 10) or (x < 3), numbers))  # we can also use 'and' instead of 'or'

print("*" * 23 + " Odd numbers")
print(odd_numbers)
print("*" * 23 + " Prime numbers")
print(prime_numbers)
print("*" * 23 + " Greater than ")
print(higher_than_x)
print("*" * 23 + " Greater and lowe than")
print(two_conditions)

strings = ["ABC", "DAF", "XAZ"]

print("*" * 23 + " Find a string in a list ")
search_for_string = list(filter(lambda x: (x == "DAF"), strings))

print(search_for_string)

dictionaries = {"Age": 12,
                "Name": "Bogdan",
                "Location": "Romania"}


print("*" * 23 + " Search for a value in a dictionary ")
search_by_values = list(filter(lambda x: True if (x == 12) else False, dictionaries.values()))
print(search_by_values)

print("*" * 23 + " Search for a key in a dictionary ")
search_by_key = list(filter(lambda x: (x == "Age"), dictionaries.keys()))
print(search_by_key)
