# Create an array
arr = [1, 2, 3, 4, 5]

# Access an element by index
print(arr[0])  # Output: 1

# Insert an element at a specific index
arr.insert(2, 6)  # Insert 6 at index 2
print(arr)  # Output: [1, 2, 6, 3, 4, 5]

# Delete an element at a specific index
arr.pop(3)  # Delete element at index 3
print(arr)  # Output: [1, 2, 6, 4, 5]

# Update an element at a specific index
arr[2] = 7  # Update element at index 2
print(arr)  # Output: [1, 2, 7, 4, 5]
