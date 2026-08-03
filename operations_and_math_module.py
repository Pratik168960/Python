# We must import the math module to use complex mathematical calculations
# Best practice is to always put imports at the very top of your file
import math 


# AUGMENTED ASSIGNMENT OPERATORS
x = 10 
x -= 3 # This is the exact same as writing: x = x - 3
print(x) # output : 7 


# OPERATOR PRECEDENCE 
# which means the order of operations 
y = 10 + 3 * 2 
print (y) # output : 16

# Python calculates math in this specific order:
# 1. Parentheses: ()
# 2. Exponentiation: 2 ** 3 
# 3. Multiplication or Division: *, /, //, %
# 4. Addition or Subtraction: +, -



# BUILT-IN MATH FUNCTIONS
y = 2.9 
print(round(y)) # round off to nearest integer --> 3 
print(abs(-2.9)) # this always returns absolute positive value --> 2.9



# THE MATH MODULE

# if we want to write a program that involves complex mathematical calculations
# we need to import the math module 
# A module in Python is a separate file with some reusable code we use these 
# modules to organize our code into different files 
print(math.ceil(2.9)) # output --> 3 
print(math.floor(2.9)) # output --> 2 
