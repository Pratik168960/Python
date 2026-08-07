
# ERROR HANDLING (TRY / EXCEPT)
# EXIT CODES:
# Exit code 0: The program executed successfully with no errors.
# Exit code 1: The program crashed (encountered an unhandled error).


# As a good programmer, we should anticipate situations where a user might 
# provide bad input or where math might fail, and handle those exceptions gracefully
# so the program doesn't crash.



# age = int(input('Age: '))     # input in string passing to int function and storing it 
# print(age)

# output:
# Age: 20
# 20



# but what if we run this program and instead of entering numerical value
# we enter something like asd

# we get a value error with message invalid interval 
#  so 0 always means success and anything but 0 means crash 



# so as a good programmer we should handle the situation and print a proper 
# error message 

# now how can we handle these errors , in python we have a construct called 
# try except 



# HANDLING MULTIPLE EXCEPTIONS

try:
    age = int(input('Age: '))
    income = 20000
    risk = income / age 
    print(age)

except ZeroDivisionError:
    print('Age cannot be 0')
except ValueError:  # type of the error that our program may encounter 
    # and in this block we can define what should happen if our program encounters 
    # an error of type ValueError, in this case we need to print a proper error msg 
    print('Invalid value')

# so our program no longer crashes exit 

# we can handle more errors with exception for example right after age let's 
# define a variable income and set it up 20000 and risk = income / age 

# if we enter 0 as age it will give ZeroDivisionError because we can't divide 
# a number by 0 so we couldn't catch this kind of exception or error with this 
# except block it is only catching ValueError
# we can add another except statement for an exception of type Zero Division Error 

# so now our program did not crash at entering age 0 


# As a good programmer we should always anticipate these kind of exceptions and 
# handle them properly 



# output :
# Age: 20
# 20


# Age: 0
# Age cannot be 0


# Age: asd 
# Invalid value