
# 1. GENERAL PURPOSE FUNCTIONS vs METHODS
# 'len' and 'print' are general-purpose built-in functions.
# They are not limited to strings; they can be used on many types of objects.

course = 'Python for beginners'
# built-in function to calculate number of characters
print(len(course))
# output : 20
# it is a general purpose function so its not limited to counting the number of
# characters in string we can use this list to count elements 


# when a function belongs to something else or is specific to some kind of object 
# we refer to that function as a method 
print(course.upper()) # converting string to uppercase
# output : PYTHON FOR BEGINNERS

# because this function is specific to string we refer to this a method 
# len and print are general purpose functions they don't belong to string or numbers 
# or other kind of objects 


# IMPORTANT: String methods do NOT modify the original string!
# this method does not modify our original string infact it creates a new string and 
# return it our original string has it's form as it was 

print(course.lower())
# output : python for beginners




# 2. SEARCHING IN STRINGS

# find a character or sequence of characters in string in those situations we can use find method 
print(course.find('o'))# this will return index of first occurence 
# output : 4 
# it is case sensitive if not found it return -1 
# we can also pass sequence of characters 





# 3. REPLACING CHARACTERS

# there is also a method for replacing a char or sequence of characters using replace 
print(course.replace('Beginners', 'Absolute Beginners'))
# output : Python for beginners 
# this method is also case sensitive 




# 4. THE 'IN' OPERATOR (Boolean check)

# if you want to check the existence of a char or sequence of char in your string 
# we have to use in operator 

print('Python' in course) 
# will check Python word is in course or not it will give boolean value in return 
# output : True 