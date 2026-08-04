
# IF, ELIF, AND ELSE STATEMENTS
# We use if statements to build programs that can make decisions based 
# on certain conditions.

is_hot = False 
is_cold = True 

if is_hot:
    print("It's a hot day")
    print("Drink plenty of water")
elif is_cold:
    print("It's cold day")
    print("Wear warm clothes")
else:
    print("It's a lovely day")

print("Enjoy your day")
# as we defined the variable to True it will execute the block of code of if block 
# and the remaining ones 

# output :
# It's cold day
# Wear warm clothes
# Enjoy your day
    


# PRACTICAL EXAMPLE: DOWN PAYMENT

price = 1000000
has_good_credit = True 

if has_good_credit:
    # 10% down payment for good credit
    down_payment = 0.1 * price
else:
    # 20% down payment for bad credit
    down_payment = 0.2 * price

print(f"Down payment: ${down_payment}")

# output 
# Down payment: $100000.0