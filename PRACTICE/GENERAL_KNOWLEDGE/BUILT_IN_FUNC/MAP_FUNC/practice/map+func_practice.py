# Exercise 1  - Sum some random numbers from user input

print("**********************")
print("SUM OF 5 NUMBERS FROM USER INPUT")
numbers = input("Please enter 5 numbers separated by a comma :").split(",")

# Make a list from the numbers the user entered
numbers_list = [numbers]

# Flatten the list
flat_list = [item for sublist in numbers_list for item in sublist]

# Get the sum of the elements in the list using map() and sum() function
result = sum(list(map(int, flat_list)))

print(f"The sum of the numbers is : {result}")
