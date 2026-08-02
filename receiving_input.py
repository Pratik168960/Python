name = input('What is your name? ')

# both print and input are functions that are built into python 
# as a metaphor think of a remote control of tv on this remote control we have 
# a bunch of buttons these are functions built into tv you can turn it on, 
# turn it off, change the volume and so on 
# in python also we have some bunch of functions for common tasks such as 
# printing msg, receiving input and so on 

# whenever we have these parenthesis we are going to say we are calling or executing 
# that function it's like pressing a button on a remote control 
print('Hi ' + name)
# this expression combines two strings 

# output :
# What is your name? Pratik
# Hi Pratik


fav_color = input('What is your favoruite color? ')
print(name + ' likes ' + fav_color)


# output:
# What is your favoruite color? Blue
# Pratik likes Blue

# Anything we take as input using input() is ALWAYS stored as a String (text)

birth_year = input('Birth year: ')

# age = 2026 - birth_year 
# ^ ERROR: We cannot subtract a String from an Integer!

age = 2026 - int(birth_year) # int() for conversion of birthyear from string to integer 
# if not done we will get error as operator works on same type of data 
# anything we take as input is in string form 
print(age)

print(type(age)) # datatype of variable 
# output :
# Birth year: 2006
# 20
# <class 'int'>



weight_lbs = input('Enter your weight (in pounds) : ') 
weight_kg = float(weight_lbs) * 0.454 
print(weight_kg)

# output :
# Enter your weight (in pounds) : 145
# 65.83