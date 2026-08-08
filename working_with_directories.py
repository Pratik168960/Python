

# DIRECTORIES & PATHS (PATHLIB MODULE)

# The pathlib module provides an object-oriented way to interact with 
# the file system (files and directories).

from pathlib import Path

# PATH TYPES:
# Absolute path: Starts from the root of the hard disk (e.g., C:\Program Files\Python\)
# Relative path: Starts from the current directory


# 1. CHECKING IF A PATH EXISTS

# If we don't pass an argument, Path() refers to the current directory
# Here, we are checking if a folder named "ecommerce" exists in our current directory.
path = Path("ecommerce")
print(f"Does the 'ecommerce' folder exist? {path.exists()}")




# 2. CREATING AND REMOVING DIRECTORIES

new_dir = Path("emails")

# Create the directory
# new_dir.mkdir()
print("Created 'emails' directory.")

# Remove the directory
# new_dir.rmdir()
print("Removed 'emails' directory.")
# (Note: I commented out the execution so it doesn't actually create/delete 
# folders every time you run this file, but that is the exact syntax!)




# 3. SEARCHING DIRECTORIES (GLOB)

# We want to search our current directory
current_path = Path()

# .glob() searches for files and directories matching a pattern.
# '*.*' means: Find ANY file name with ANY extension.
# '*.py' means: Find ANY file name, but ONLY if it ends in .py (Python files).

print("All Python files in this directory:")
# Note: glob() returns a 'generator object'. We loop through it to see the results.
for file in current_path.glob("*.py"):
    print(file)


'''
Output:

Does the 'ecommerce' folder exist? True


Created 'emails' directory.
Removed 'emails' directory.


All Python files in this directory:
classes.py
comparison_operators.py
conditions.py
constructor.py
converters.py
dictionaries.py
exception_handling.py
formatted_strings.py
for_loops.py
functions.py
generating_random_values.py
how_code_executes.py
inheritance.py
lists.py
logical_operators.py
modules.py
nested_loops.py
operations_and_math_module.py
packages.py
receiving_input.py
return_statement.py
reusable_function.py
strings.py
string_methods.py
tuples.py
utils.py
variables.py
weight_converter.py
while_loops.py
working_with_directories.py
'''