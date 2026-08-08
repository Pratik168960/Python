

# PACKAGES IN PYTHON

# A package is a container for multiple modules. In file system terms, 
# a package is just a directory (folder) with an __init__.py file inside
# We use packages to group related modules together (e.g., sales, shipping, customer service)



# Approach 1: Import the module directly from the package
import ecommerce.shipping

# Downside: This is very verbose. You have to type the full path every time.
ecommerce.shipping.calc_shipping()




# Approach 2: Import just the function you need from the module inside the package
from ecommerce.shipping import calc_shipping

# Upside: You can call the function directly! This is very clean.
calc_shipping()






# Approach 3: Import the module from the package
from ecommerce import shipping

# Upside: You prefix the function with the module name. It is shorter than 
# Approach 1, but keeps the context clear so you know exactly where the function came from
shipping.calc_shipping()

'''
Output:
Calculating shipping costs...

Calculating shipping costs...

Calculating shipping costs...
'''