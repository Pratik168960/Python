
# WEIGHT CONVERTER (Lbs <-> Kg)

# This program asks the user for their weight and their preferred unit,
# then converts the weight to the opposite unit.

weight = int(input("Weight: "))
unit = input('(L)bs or (K)g: ')

# We use the .upper() method so that whether the user types 'l' or 'L', 
# the condition will still evaluate to True.
if unit.upper() == "L":
    # Convert Pounds to Kilos
    converted = weight * 0.45 
    print(f"You are {converted} kilos")
else:
    # Convert Kilos to Pounds
    # Note: We use the single slash (/) for normal division to keep decimal precision. 
    converted = weight / 0.45
    
    # We can use the round() function to clean up the long decimal output
    print(f"You are {round(converted, 1)} pounds")


# Output:

# Weight: 160
# (L)bs or (K)g: l
# You are 72.0 kilos

# Weight: 72
# (L)bs or (K)g: k
# You are 160.0 pounds
