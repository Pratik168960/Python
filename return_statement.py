
# FUNCTIONS: RETURN STATEMENTS & NONE
# Functions can send data back to the code that called them 
# using the 'return' statement.


# 1. RETURNING A VALUE (The Right Way)
def square(number):
    return number * number 
    # now to return this number * number outside this function we use return 

result = square(3)

# name = input()
# this is just like input function it waits for the user to give input which returns 
# in name variable 
print(result)

# we can directly call this inside of the print function without defining a 
# separate variable 

print(square(3))


# what happens if we dont use the return statement in our function and 
# directly use print in function 

# output 
# 9 
# 9

# 2. PRINTING INSTEAD OF RETURNING (The 'None' Bug)

def square_with_print(number):
    # Here we just print the number, but we DO NOT use the 'return' keyword.
    print(number * number) 

# What happens if we try to print the result of this function?
print(square_with_print(3))


# Output:
# 9
# None


# EXPLANATION: WHAT IS HAPPENING HERE?

# 1. Python executes the outer print() statement, which calls square_with_print(3)
# 2. The control moves into our function
# 3. Inside the function, it calculates 3 * 3 and prints '9' to the terminal
# 4. The function reaches the end
# 5. IMPORTANT: By default, if you do not explicitly use a 'return' statement, 
#    Python automatically returns 'None'
# 6. 'None' is an object that represents the absence of a value (like 'null' in other languages)
# 7. Finally, the outer print() statement receives that returned value and prints 'None'