# While loop usually needs a variable assigned above the loop
# Basic syntax is while + condition
#  loop statement + increment + a brake condition


# 1. Loop without brake  and continue
# In this case the else statement is executed after the loop break
i = 0

while i <= 5:
    print(i)
    # Incrementing i
    i += 1
else:
    print("Out of the loop")
print("_______________________________________________________")

# 2. Loop with brake condition
# In this case the else statement is not executed after the loop break

i = 0
while i <= 5:
    # Incrementing i
    i += 1
    # The brake condition - if i ==3 then the loop ends and the else is ignored
    if i == 3:
        break
    print(i)
else:
    print("Out of the loop")
print("_______________________________________________________")

# 3 Loop with continue statement
# In this case after the loop finds the condition, ignore all the code after the continue statement
# The else clause if executed

i = 0

while i <= 5:
    # Incrementing i
    i += 1
    # Ignore the code after "continue" , but executes the else statement
    if i == 3:
        continue
    print(i)
else:
    print("Out of the loop")
