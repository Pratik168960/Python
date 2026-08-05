
# COMPARISON OPERATORS

# We use comparison operators to compare a variable with a value.
# These include: > (greater than), < (less than), >= (greater than or equal to), 
# <= (less than or equal to), == (equal to), and != (not equal to).

# 1. TEMPERATURE CHECKER
temperature = 30 

# Because 30 is NOT greater than 30 (it is exactly equal), 
# this condition evaluates to False, and the 'else' block runs.
if temperature > 30:
    print("It's a hot day")
else:
    print("It's not a hot day")


# Output:
# It's not a hot day


# 2. NAME LENGTH VALIDATOR
# This is a practical, real-world example of form validation 
# (like creating a username on a website).

name = "Pratik"

# comparing the len of string 
if len(name) < 3:
    print("Name must be at least 3 characters")
elif len(name) > 50:
    print("Name must be a maximum of 50 characters")
else:
    print("Name looks good") 


# Output:
# Name looks good