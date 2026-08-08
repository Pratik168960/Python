

# PIP & THIRD-PARTY PACKAGES (PyPI)

# PyPI (Python Package Index) is a massive repository of community-built 
# Python packages. You can browse them at pypi.org.

# 'pip' is the tool we use to install them into our projects.



# 1. HOW TO INSTALL (Run in Terminal)
# You DO NOT write pip commands inside your Python script. 
# You write them in your Terminal / Command Prompt!

'''
TERMINAL COMMANDS:

# To install a package (e.g., 'requests', a popular package for fetching web data):
> pip install requests

# To see a list of all packages currently installed on your system:
> pip list

# To uninstall a package:
> pip uninstall requests
'''



# 2. USING THE INSTALLED PACKAGE

# Once a package is installed via pip, you can import it exactly 
# like a built-in module!
import requests 

# The 'requests' package makes it incredibly easy to talk to websites.
# Here, we are fetching data from the public GitHub API.
print("Fetching data from GitHub...")
response = requests.get("https://api.github.com")

# A status code of 200 means "OK / Success!"
print(f"Server Response Code: {response.status_code}")


'''
Output:
Fetching data from GitHub...
Server Response Code: 200
'''