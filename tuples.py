
# TUPLES & UNPACKING IN PYTHON
# Tuples are similar to lists, but they are IMMUTABLE. 
# This means once a tuple is created, you cannot MODIFY, add, or remove items.
# We define tuples using parentheses () instead of square brackets [].


numbers = (1, 2, 3)

# We can read items just like a list:
print(f"The first number is: {numbers[0]}")

# If we try to change an item, Python will throw an error!
# numbers[0] = 10 
# ^ ERROR: 'tuple' object does not support item assignment

'''
Output:
The first number is: 1
'''


# UNPACKING
# Unpacking is a powerful feature in Python that allows us to assign 
# the items of a tuple (or a list) to multiple variables all at once.

coordinates = (1, 2, 3)

# Instead of writing:
# x = coordinates[0]
# y = coordinates[1]
# z = coordinates[2]

# We can just do this (Unpacking):
x, y, z = coordinates

print(f"x: {x}")
print(f"y: {y}")
print(f"z: {z}")

# Note: Unpacking works exactly the same way with Lists!

'''
Output:
x: 1
y: 2
z: 3
'''