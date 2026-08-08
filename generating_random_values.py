


# BUILT-IN MODULES: THE RANDOM MODULE
# Python comes with a massive standard library of built-in modules
# This means there is already a ton of functionality we can reuse!
# Tip: Search for "Python 3 Module Index" on Google to see them all.

import random 

# 1. GENERATING RANDOM NUMBERS

for i in range(3):
    # random.random() generates a float between 0 and 1
    # random.randint(a, b) generates an integer between a and b (inclusive)
    print(random.randint(10, 20)) 


# 2. CHOOSING A RANDOM ITEM FROM A LIST

members = ['Pat', 'Tash', 'Bob', 'Alice']

# .choice() automatically picks one random item from a list or tuple
leader = random.choice(members)
print(f"The randomly selected leader is: {leader}")




# 3. PRACTICAL EXERCISE (Dice Roller)

class Dice:
    def roll(self):
        first = random.randint(1, 6)
        second = random.randint(1, 6)
        # We return these two values as a Tuple (a read-only list).
        # You can write (first, second) or just first, second.
        return (first, second)


# PEP 8 NOTE: Python Enhancement Proposal 8 is the official style guide.
# It recommends leaving exactly TWO blank lines after defining a class or function 
# to keep the code readable. (IDEs like PyCharm or VSCode will often warn you about this!)

dice = Dice()
print(f"You rolled: {dice.roll()}")


'''
EXAMPLE OUTPUTS:
14
19
11

The randomly selected leader is: Tash

You rolled: (4, 1)
'''