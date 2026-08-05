

# NESTED LOOPS IN PYTHON

# A nested loop is simply a loop inside another loop. 
# The "inner loop" will finish all of its iterations for EVERY single 
# iteration of the "outer loop".

# 1. GENERATING COORDINATES

# Outer loop (runs 4 times: 0, 1, 2, 3)
for x in range(4):
    # Inner loop (runs 3 times: 0, 1, 2 for EACH x)
    for y in range(3):
        # We use an f-string to easily format the output as (x, y)
        print(f'({x}, {y})')

'''
Output:
(0, 0)
(0, 1)
(0, 2)
(1, 0)
(1, 1)
(1, 2)
(2, 0)
(2, 1)
(2, 2)
(3, 0)
(3, 1)
(3, 2)
'''






# 2. DRAWING A SHAPE (The 'F' Shape)
print("\n--- 2. DRAWING AN 'F' SHAPE ---")

# This list dictates how many 'x's we want on each line
numbers = [5, 2, 5, 2, 2]

# Outer loop goes through each number in our list
for i in numbers:
    # We reset our output string to be empty at the start of every new line
    output = ''
    
    # Inner loop runs 'i' times to build the string character by character
    for count in range(i):
        output += 'x'
        
    print(output)

'''
Output:
--- 2. DRAWING AN 'F' SHAPE ---
xxxxx
xx
xxxxx
xx
xx
'''