

# LISTS IN PYTHON
# Lists are used to store multiple items in a single variable.


# 1. BASIC LISTS & SLICING

names = ['Pat', 'Tasha', 'Alice', 'Sarah', 'Bob']

# Modify the first item (Index 0)
names[2] = 'Jon'

# Slicing: Get all items starting from index 0 to the 3 index
print(names[:3])

'''
Output:
--- 1. BASIC LISTS & SLICING ---
['Pat', 'Tasha', 'Jon']
'''


# 2. FINDING THE MAXIMUM VALUE
numbers = [3, 6, 2, 8, 4, 10]

max_number = numbers[0]

for number in numbers:
    if number > max_number:
        max_number = number
        
print(f"The maximum number is: {max_number}")

'''
Output:
The maximum number is: 10
'''


# 3. 2D LISTS (MATRICES)
# A 2D list is simply a list where each item is another list.

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Modify an item: row 0, column 1 (the '2') becomes '20'
matrix[0][1] = 20
print(f"Modified value: {matrix[0][1]}")

# We use nested loops to go through a 2D list
for row in matrix:
    for item in row:
        print(item)

'''
Output:
Modified value: 20
1
20
3
4
5
6
7
8
9
'''


# 4. LIST METHODS (INSERT)

numbers = [5, 2, 1, 7, 4]

# insert() takes two arguments: the index, and the value to insert.
# Here we insert '20' at index 0.
numbers.insert(0, 20)
print(numbers)

'''
Output:
[20, 5, 2, 1, 7, 4]
'''


# 5. REMOVING DUPLICATES (PRACTICAL EXERCISE)

numbers = [2, 2, 4, 6, 3, 4, 6, 1]
uniques = []

for number in numbers:
    # We check if the number is NOT already in our new list
    if number not in uniques:
        uniques.append(number)
        
print(uniques)

'''
Output:
[2, 4, 6, 3, 1]
'''