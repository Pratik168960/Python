

# utils.py (Module)
# Utility modules often contain helper functions that can 
# be reused across many different programs.

def find_max(numbers):
    maximum = numbers[0]
    for number in numbers:
        if number > maximum:
            maximum = number 
    return maximum