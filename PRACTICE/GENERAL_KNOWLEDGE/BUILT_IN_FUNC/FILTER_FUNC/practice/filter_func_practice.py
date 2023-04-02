grades = {"John": 8.6,
          "Alice": 7.9,
          "Bob": 6.7,
          "Derek": 9.9}


def filtering_function_by_condition(pair):
    key, values = pair
    if values < 8:
        return True
    else:
        return False


def filtering_function_by_key(pair):
    key, value = pair
    wanted_key = ["Alice", "Bob"]
    if key in wanted_key:
        return True
    else:
        return False


results = list(filter(filtering_function_by_condition, grades.items()))
print(results)

results2 = list(filter(filtering_function_by_key, grades.items()))
print(results2)
