# map() function returns a map object(which is an iterator) of the results after applying the given
# function to each item of a given iterable (list, tuple etc.)
# map() function always takes 2 parameters : a function and an iterable (list, etc)

# First we define a function
def multiply_func(x, y):
    return x * y


# We create a list for the two function parameters

first_list = [1, 2, 3, 5]
second_list = [2, 3, 4, 5]

# We use the map function to multiply the items from the two lists and print the result.

result = map(multiply_func, first_list, second_list)
print(type(result))  # Type of result is <class 'map'>

# We need to use 'list' to check the result.

print(list(result))

# We can use a lambda function also instead of defining a function
result = map(lambda x, y: x * y, first_list, second_list)
print(list(result))

# We can listify the list of strings also.

list_of_strings = ["age", "name", "location"]
result = list(map(list, list_of_strings))
print(result)
