

my_list = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]

final_list = list(filter(lambda x: (x % 2 != 0), my_list))
print(final_list)

adult_list = [13, 90, 17, 59, 21, 60, 5]

result_list = list(filter(lambda x: x > 10, adult_list))
print(result_list)

li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]

final_list = list(map(lambda x: x * 2, li))
print(final_list)