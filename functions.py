# ==========================================
# FUNCTIONS: POSITIONAL & KEYWORD ARGUMENTS
# ==========================================
# Functions allow us to write reusable blocks of code.
# We pass data into functions using parameters.

def greet_user(first_name, last_name):  
    print(f"Hi {first_name} {last_name}!")
    print('Welcome aboard')

# ------------------------------------------
# 1. POSITIONAL ARGUMENTS
# ------------------------------------------
print("--- 1. POSITIONAL ARGUMENTS ---")
# By default, arguments are assigned to parameters based on their position.
# "Pratik" goes to first_name, "Singh" goes to last_name.
greet_user("Pratik", "Singh")

# ------------------------------------------
# 2. KEYWORD ARGUMENTS
# ------------------------------------------
print("\n--- 2. KEYWORD ARGUMENTS ---")
# We can explicitly state which parameter gets which value.
# This allows us to ignore the order of the parameters!
greet_user(last_name="Singh", first_name="Pratik")

# MIXING THEM: 
# You can mix positional and keyword arguments, but POSITIONAL MUST COME FIRST.
# Valid:   greet_user("Pratik", last_name="Singh")
# Invalid: greet_user(first_name="Pratik", "Singh") <-- This will crash!

'''
Output:
--- 1. POSITIONAL ARGUMENTS ---
Hi Pratik Singh!
Welcome aboard

--- 2. KEYWORD ARGUMENTS ---
Hi Pratik Singh!
Welcome aboard
'''

# ------------------------------------------
# 3. THE POWER OF KEYWORD ARGUMENTS
# ------------------------------------------
print("\n--- 3. WHY KEYWORD ARGUMENTS ROCK ---")

def calc_cost(total, shipping, discount):
    final_price = total + shipping - (total * discount)
    print(f"Total cost: ${final_price}")

# If we just look at calc_cost(50, 5, 0.1), it is hard to know what those numbers mean.
# Keyword arguments make the code highly readable and self-documenting!
calc_cost(total=50, shipping=5, discount=0.1)

'''
Output:
--- 3. WHY KEYWORD ARGUMENTS ROCK ---
Total cost: $50.0
'''