

# CONSTRUCTORS IN PYTHON

# THE PROBLEM: In standard classes, we can create an object without 
# giving it the necessary attributes (like a point missing an X coordinate).
# This can cause our program to crash. 

# THE SOLUTION: We use a Constructor! 
# A constructor is a special function that gets called automatically 
# at the exact moment we create a new object.



# 1. THE __init__ METHOD

class Point:
    # __init__ is short for initialize. This is our constructor!
    # 'self' is a reference to the current object being created in memory.
    def __init__(self, x, y):
        self.x = x 
        self.y = y 
        
    def move(self):
        print("move")
        
    def draw(self):
        print("draw")

# Because we defined a constructor that takes x and y, 
# we MUST pass those values when creating the object.
point = Point(10, 20)

# We can still overwrite the values later if we want
point.x = 11 
print(f"Updated X coordinate: {point.x}")

'''
Output:
Updated X coordinate: 11
'''




# 2. PRACTICAL EXERCISE: PERSON CLASS


class Person:
    def __init__(self, name):
        self.name = name
        
    def talk(self):
        # We use self.name to access the attribute of the current object
        print(f"Hi, I am {self.name}")
        
# Creating our first Person object
pat = Person("Pratik Singh")
pat.talk()

# Creating a completely separate Person object
bob = Person("Bob Smith")
bob.talk()

'''
Output:
Hi, I am Pratik Singh
Hi, I am Bob Smith
'''