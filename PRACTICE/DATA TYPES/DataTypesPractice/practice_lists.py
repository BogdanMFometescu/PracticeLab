li = ["Age", 1, "Name", 34, True, 1, 55, 66, 1, "Name", 1, 56]

# Lists are mutable and ordered, allow duplicates
# Add items to lists( item is added as last element in the list) - append
print(li)

# Retrieve items from lists using index position

print(li[1])

# Replacing item in a list by index position

li[1] = "Replaced item"
print(li)

# Removing items from lists( by name or value)

li.remove("Age")
print(li)

# Reverse the lists values
li.reverse()

print(li)

# Count a specific value in list(need to set a new variable)

xx = li.count("Name")
print(xx)

# Extend a list with specific values

li_2 = [1, 2, 3, 4, 5, 6, 7, ]

li.extend(li_2)
print(li)

# Insert a value at a specific position

li.insert(3, "New item added here")

print(li)

# Remove an item at a specific position

li.pop(1)
print(li)

# Sort the list(must be integers)

# ascending
li_integers = [1, 2, 35, 64, 25, 69]
li_integers.sort()
print(li_integers)
# descending
li_integers.sort(reverse=True)
print(li_integers)

print("_____________________________________________________________________")
# Slicing lists
# Get all values from the list

xx = li[0:]
print(xx)

print("_____________________________________________________________________")

# Get values between 2 index's
xx = li[0:2]
print(xx)

print("_____________________________________________________________________")
# Get values between 2 index's with step
li = [1, 4, 56, 78, 37, 34, 64, 42, 4, 4, 4, 4]
xx = li[0:4:2]
print(xx)

print("_____________________________________________________________________")
# Removing duplicates from a list
li = list(dict.fromkeys(li))
print(li)

print("_____________________________________________________________________")
# Filter list using filter  function

li_filtered = list(filter(lambda x: x > 50, li))
print(li_filtered)

# Filter using list comprehension

print("_____________________________________________________________________")
li_2 = [lix for lix in li if lix > 50]
print(li_2)

# Combining list

li1 = [1, 2, 3, 4]
li2 = [3, 4, 5, 6]

print("_____________________________________________________________________")
li3 = list(zip(li, li2))
print(li3)

# Finding the most common element in a list of strings


li = ["a", "b", "c", "a"]
li2 = max(set(li), key=li.count)
print(li2)

# to find the most frequent element from the list
my_list = ['a', 'a', 'a', 'b', 'c', 'd', 'd', 'e']

most_frequent_value = max(set(my_list), key=my_list.count)

print("The most common element is:", most_frequent_value)

# to flatten a list_of_lists by using list comprehension
list_of_lists = [[1, 2],
                 [3, 4],
                 [5, 6],
                 [7, 8]]

# using list comprehension
my_list = [item for List in list_of_lists for item in List]
print(my_list)

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list1[-5:5])
print(list1[4])

# Operation with lists
a = [2, 3]
b = [4, 5]

# multiply (*) adds the same list in the list

c = (a * 2)  # -----> [2,3,2,3]

# add (+) add the second list to the list
d = a + b  # -------> [2,3,4,5]
print(d)
