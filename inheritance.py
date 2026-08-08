

# INHERITANCE & THE DRY PRINCIPLE

# In programming, we have a principle called DRY (Don't Repeat Yourself)
# If we duplicate code in multiple classes and an issue arises, we have to 
# fix it everywhere. 

# Inheritance solves this by allowing "child" classes to inherit properties 
# and methods from a "parent" class



# 1. THE PARENT CLASS


# We define a general 'Mammal' class that contains methods common to all mammals
class Mammal:
    def walk(self):
        print("walk")


# 2. THE CHILD CLASSES
# We pass the parent class (Mammal) inside the parentheses to inherit from it

class Dog(Mammal):
    # Note: If we didn't want to add any new methods to Dog, we would have to 
    # type the 'pass' keyword, because Python does not allow completely empty classes
    def bark(self):
        print("bark")


class Cat(Mammal):
    def be_annoying(self):
        print("annoying")



# 3. CREATING OBJECTS
# The Dog object has access to its own methods AND the Mammal methods!
dog1 = Dog()
dog1.walk()
dog1.bark()

# The Cat object has access to its own methods AND the Mammal methods!
cat1 = Cat()
cat1.walk()
cat1.be_annoying()

'''
Output:
walk
bark

walk
annoying
'''