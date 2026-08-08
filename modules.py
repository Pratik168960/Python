

# MODULES IN PYTHON

# A module in Python is basically a file with some Python code
# We use modules to organize our code into files
# This gives us an organized structure and the ability to reuse our code!


# 1. IMPORTING AN ENTIRE MODULE

# This imports the entire file. 
import converters

# We must prefix the function with the module name and a dot (.)
print(f"70 kg in lbs: {converters.kg_to_lbs(70)}")




# 2. IMPORTING SPECIFIC FUNCTIONS
# Instead of importing the whole module, we can import a specific function
# This allows us to call the function directly without the prefix!

from converters import lbs_to_kg
print(f"155 lbs in kg: {lbs_to_kg(155)}")




# 3. PRACTICAL EXERCISE (find_max)

from utils import find_max

numbers = [10, 3, 6, 2]
maximum = find_max(numbers)
print(f"The maximum number is: {maximum}")

'''
Output:
70 kg in lbs: 155.55555555555554

155 lbs in kg: 69.75

The maximum number is: 10
'''