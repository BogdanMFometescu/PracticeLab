import numpy as np

# Create an array from 2 lists
# 1D array
x = np.array([1, 2, 3])
print(x)
print("1x array")
# 2D array
x = np.array([[0, 1, 2], [3, 4, 5]])
print(x)
print("2D array")

# 3D array
x = np.array([[[1, 2, 3], [4, 5, 6], [7, 8, 9]]])
print(x)
print("3D array")

# Create array with 3 values of "1"
x = np.ones(3)
print(x)
print("only ones 'array'")

# Create an array with "0" values
x = np.zeros(1)
print(x)
print("only 'zeroes ' array")

# Create an empty array with 3 element
x = np.empty(3)
print(x)
print("empty array with 3 elements")
# Arrange an array

x = np.arange(1, 14)
print(x)
print("arrange and array of 14 elements")

# Lin space
x = np.linspace(0, 20, num=6)
print(x)
print("lin space an array with a total numbers of elements - 6  between 0 and 20 and with even difference between them")

# Sort an array

x = np.array([2, 6, 8, 66, 34, 89])
y = np.sort(x)

print(x)
print(y)
print("sorting in ascending order")

# Concatenate array

x = np.array([1, 3, 3, 6])
y = np.array([7, 8, 9, 10, 11, 6])
z = np.concatenate((x, y))  # tuple
print(z)
print("concatenate and array")

# Reshape array
x = np.array([1, 2, 3, 4])
y = x.reshape(2, 2)  # first param = rows, second param = columns

z = np.arange(1, 25).reshape(2, 12)

print(y)
print(z)
print("reshaped array")

# Indexing
x = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print(x[0, 1], x[1, 3])
print("indexing ")

# Slicing
x = np.array([1, 34, 5, 5, 56, 9])

print(x[1:])
print(x[0:3:2])
print(x[:-1])
print(x[-2:])
print(x[:-2])
print("slicing ")

# Sum arrays
x = np.array([1, 2, 3, 4])
y = np.array([5, 6, 7, 8])

z = x + y  # sum up every index by columns - 0 + 0, 1 + 1 , etc , needs to be same size

print(z)
print(sum(x))
print("summing ")

# Conditioning
x = np.array([0, 1, 2, 3, 4, 7, 8, 9, 11])

y = np.nonzero(x > 5)  # get the indices of elements greater than 5 and not equal to zero(0)

z = (x > 5)  # Condition (return True or False)

print(y)
print(x[z])  # original array[condition variable] - gets the values which are meeting the condition
print("conditioning ")

# Min , Max
x = np.array([1, 5, 6, 24, 6, 7])
z = x.min()
y = x.max()
print(z)
print(y)

# Reverse array
x = np.array([1, 5, 6, 24, 6, 7])
y = np.flip(x)
print(y)

#Reshape array
x = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
y = x.ravel()                                               #Modify the original array, flatten does not.
print(x.shape)
print(x.size)
print(x.ndim)
print(y)
