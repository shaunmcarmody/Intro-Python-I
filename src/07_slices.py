"""
Python exposes a terse and intuitive syntax for performing 
slicing on lists and strings. This makes it easy to reference
only a portion of a list or string. 

This Stack Overflow answer provides a brief but thorough
overview: https://stackoverflow.com/a/509295

Use Python's slice syntax to achieve the following:
"""

a = [2, 4, 1, 7, 9, 6]

# Output the second element: 4:
b = a[1:2]
print(b)

# Output the second-to-last element: 9
b = a[-2: -1]
print(b)

# Output the last three elements in the array: [7, 9, 6]
b = a[-3:]
print(b)

# Output the two middle elements in the array: [1, 7]
b = a[2:4]
print(b)

# Output every element except the first one: [4, 1, 7, 9, 6]
b = a[1:]
print(b)

# Output every element except the last one: [2, 4, 1, 7, 9]
b = a[:-1]
print(b)

# For string s...

s = "Hello, world!"

# Output just the 8th-12th characters: "world"
t = s[7:12]
print(t)