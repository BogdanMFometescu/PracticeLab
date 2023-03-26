# Sets are mutable, unordered and don't allow duplicates


my_sett = set()  # created empty set

# Adding item to a set using "add"

my_sett.add(1)
my_sett.add(2)
my_sett.add(4)
my_sett.add(8)
my_sett.add(10)
print(my_sett)

# Removing items - as it does not allow indexing, we specify the value
my_sett.remove(2)
print(my_sett)

# Sets allow intersection between two sets or set and a list
my_lst = [1, 4, 8, 10]
my_second_sett = {1, 2, 3, 4}

# Intersection find the common value
xx = my_sett.intersection(my_lst)

# Difference finds the value which is not in the first set where the compare is done.
yy = my_sett.difference(my_second_sett)
print(xx)
print(yy)

# Issubset function - finds if  ALL the items from a list are in a set
zz = my_sett.issubset(my_lst)
print(zz)
print(my_sett)
