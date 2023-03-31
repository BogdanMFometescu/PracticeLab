# Exercise 1  - Sum some random numbers from user input

print("**********************")
print("SUM OF  NUMBERS FROM USER INPUT")
numbers = input("Please enter few  numbers separated by a comma :").split(",")

# Make a list from the numbers the user entered
numbers_list = [numbers]

# Flatten the list
flat_list = [item for sublist in numbers_list for item in sublist]

# Get the sum of the elements in the list using map() and sum() function
number_as_integer = list(map(int, flat_list))

sum_of_numbers = sum(list(map(int, flat_list)))

print(f"The sum  is : {sum_of_numbers}")

# Exercise 2 - Find Odd and Prime numbers from user input
# We will use the same numbers from exercise 1, so we don't duplicate code


results = list(map(lambda x: x % 2 == 0, number_as_integer))

results_lst = list(zip(number_as_integer, results))

for result, number in enumerate(results_lst):
    print(f"{results_lst[result][0]} is  {results_lst[result][1]}")

print("*************************************************")


# This can be coded similar without map() by using a simple function or using filter() function

def find_odd_and_prime_num(num_list):
    for item in num_list:
        if item % 2 == 0:
            print(f"{item} is Prime")
        else:
            print(f"{item} is Odd")


find_odd_and_prime_num(number_as_integer)

prime_numbers = list(filter(lambda x: (x % 2 == 0), number_as_integer))
odd_numbers = list(filter(lambda x: (x % 2 != 0), number_as_integer))

print(prime_numbers)
print(odd_numbers)
