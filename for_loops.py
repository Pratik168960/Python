

# FOR LOOPS IN PYTHON
# We use 'for' loops to iterate over items in a collection, such as a 
# string, a list, or a sequence of numbers.

# 1. ITERATING OVER STRINGS & LISTS
for char in 'Python':
    print(char)

for name in ['Pat', 'Mosh', 'Sarah']:
    print(name)

'''
Output:
P
y
t
h
o
n

Pat
Mosh
Sarah
'''


# 2. THE RANGE() FUNCTION

# range() generates a sequence of numbers. 
# Syntax: range(start, stop, step)

# This means: start at 5, go up to (but exclude) 10, jumping by 2 each time.
for item in range(5, 10, 2):
    print(item)

'''
Output:
5
7
9
'''


# 3. PRACTICAL EXAMPLE (Shopping Cart Total)

prices = [10, 20, 30]
total = 0

for price in prices:
    # We add each price to our running total. 
    total = total + price

print(f"Total: ${total}")

'''
Output:
Total: $60
'''