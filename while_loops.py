

# WHILE LOOPS IN PYTHON
# We use while loops to execute a block of code multiple times as long 
# as a certain condition remains True.



i = 1
while i <= 5:
    # In Python, we can multiply strings! '*' * 3 results in '***'
    print('*' * i)
    i = i + 1 

print("Done\n")


# Output:
# *
# **
# ***
# ****
# *****
# Done





# 1. GUESSING GAME (Using While-Else)

secret_number = 9 
guess_count = 0 
guess_limit = 3 

while guess_count < guess_limit:
    guess = int(input('Guess: '))
    guess_count += 1 
    
    if guess == secret_number:
        print("You won!")
        # 'break' immediately terminates the loop entirely
        break

# A unique feature in Python: The 'else' block on a while loop 
# ONLY executes if the loop finishes naturally WITHOUT hitting a 'break'.
else:
    print('Sorry, You failed')

print("\n")


# Example Output (Winning):
# Guess: 5
# Guess: 9
# You won!

# Example Output (Losing):
# Guess: 1
# Guess: 2
# Guess: 3
# Sorry, You failed




# 2. CAR GAME ENGINE (Infinite Loop & State)
print("Type 'help' for instructions.")

# We use a boolean variable to keep track of the car's "state"
started = False

# 'while True' creates an infinite loop. It will run forever until it hits a 'break'.
while True:
    # We add .lower() so that if the user types "START" or "Start", it still works!
    command = input("> ").lower()
    
    if command == "start":
        if started:
            print("Car is already started!")
        else:
            started = True
            print("Car started... Ready to go!")
            
    elif command == "stop":
        if not started:
            print("Car is already stopped!")
        else:
            started = False
            print("Car stopped.")
            
    elif command == "help":
        print("""
start - to start the car
stop  - to stop the car 
quit  - to exit the game
        """)
        
    elif command == "quit":
        print("Exiting game...")
        break # This breaks us out of the infinite loop
        
    else:
        print("Sorry, I don't understand that command.")


# Example Output (Interactive Session):
# Type 'help' for instructions.
# > help

# start - to start the car
# stop  - to stop the car 
# quit  - to exit the game
        
# > start
# Car started... Ready to go!
# > start
# Car is already started!
# > stop
# Car stopped.
# > fly
# Sorry, I don't understand that command.
# > quit
# Exiting game...
