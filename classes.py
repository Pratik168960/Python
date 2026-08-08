

# CLASSES IN PYTHON


# We use classes to define new types.
# Basic types in Python: Numbers, Strings, Booleans
# Complex types in Python: Lists, Dictionaries
# While these types are extremely useful, they cannot always be used 
# to model complex concepts (like a User, a Product, or a Point).



# 1. DEFINING A CLASS


# Naming Convention: Classes use PascalCase (First letter of every word is capitalized).
# We don't use underscores like we do for variables or functions.
class Point:
    # Functions inside a class are called "Methods"
    # 'self' is automatically added by Python and is required for all methods.
    def move(self):
        print("move")
        
    def draw(self):
        print("draw")



# 2. CREATING OBJECTS (INSTANCES)

# A class is just a blueprint. An object is an actual instance based on that blueprint.

point1 = Point()

# We can dynamically add attributes (variables) to our objects
point1.x = 10
point1.y = 20

print(f"Point 1 X coordinate: {point1.x}")
point1.draw()

# Each object is a different instance of the Point class. 
# They have their own independent attributes!
point2 = Point()
point2.x = 1

print(f"Point 2 X coordinate: {point2.x}")
# Note: If we tried to print(point2.y) right now, it would throw an AttributeError 
# because we haven't given point2 a 'y' attribute yet!

'''
Output:
Point 1 X coordinate: 10
draw
Point 2 X coordinate: 1
'''