# 1.	State the problem clearly. Identify the input and output formats.
# 2.	Come up with some example of inputs and outputs. Try cover all edge cases
# 3.	Come up with a correct solution for the problem. State it in plane English
# 4.	Implement the solution and test it using example inputs. Fix bugs
# 5.	Analyze the algorithm’s complexity and identify inefficiencies
# 6.	Apply the right technique to overcome the inefficiencies. Repeat steps 3 to 6


def locate_card(cards, query):
    pass


# Test case
cards = [13, 11, 10, 7, 4, 3, 1, 0]
query = 7
output = 3

# Run the function
results = locate_card(cards, query)
print(results)

# Check results
print((results == output))

test = {"input": {
    "cards": [13, 11, 10, 7, 4, 3, 1, 0],
    "query": 7},
    "output": 3}

print(locate_card(**test["input"]) == test["output"])

# Query occurs in the middle

tests = []
tests.append(test)

tests.append({"input": {
    "cards": [13, 11, 10, 7, 4, 3, 1, 0],
    "query": 1},
    "output": 6})

# Query occurs in the first element
tests.append({"input": {
    "cards": [13, 11, 10, 7, 4, 3, 1, 0],
    "query": 13},
    "output": 0})

# Minimum 3-5 test cases(edge cases)

# Write the solution in plain English
