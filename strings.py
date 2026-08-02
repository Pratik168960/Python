
# 1. HANDLING QUOTES IN STRINGS

# course = 'Python's course for beginners'
# here arises problem string ends on Python's this apstrophe as it assumes the end of string 
# and the remaining part is not considered in the string in this case we should 
# use double quotes ""
# and vice cersa for another case 

course = "Python's course for beginners"

course1 = 'Python for "beginners"'


print(course)
print(course1)


# 2. MULTILINE STRINGS 


# what if we have to define a string that is multiple lengths for eg msg email 
# in that case we need to use triple quotes 


course2 = ''' 
Hi Tony,

here is our first email to you.

Thank you,
The support team

'''
print(course2)


# 3. STRING INDEXING

# we can use [] square brackets for index so we can get the character 
print(course[0]) 

# we also can use negative index it is one of the feature that we don't have in other 
# programming languages we get characters from the end if -1 : last char 



# 4. STRING SLICING


print(course[0:3]) 
# this will return all characters starting from 0 index all the way to 3 index 
# but the 3 is excluded 

# DEFAULT VALUES:
# If we don't give a start index, Python assumes 0.
# If we don't give an end index, Python assumes the length of the string.


another = course[:]
print(another) 
# course will get copied in another variable 

name = 'Jennifer'
print(name[1:-1]) 
# output :
# ennife

