# Dictionaries ( from  3.7 ) are ordered, mutable and don't allow duplicates

# Creating an empty dictionary
my_dict = {}

# Adding items to a dictionary( key and assign value to it)

my_dict["Age"] = 18
my_dict["Name"] = "Bogdan"
print(my_dict)

# Updating a dict based on other dictionary using update function.
my_dict2 = {"Location": "Romania"}
my_dict.update(my_dict2)
print(my_dict)

print("_____________________________________________________")
# Iterating over dictionaries and get keys - values

for k, v in my_dict.items():
    print(k, v)

print("_____________________________________________________")
# Iterating over dictionaries and get only keys

for k in my_dict:
    print(k)


print("_____________________________________________________")
# Iterating over dictionaries and get only values
for v in my_dict.values():
    print(v)

print("_____________________________________________________")

# Merging dictionaries using ** unpacking
new_dict3 = {**my_dict, **my_dict2}
print(new_dict3)
print(my_dict)
print(my_dict2)
