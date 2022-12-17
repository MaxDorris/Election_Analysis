# Incorporate the random library
import random

# Print Title
print("Let's Play Rock Paper Scissors!")

# Specify the three options
options = ["r", "p", "s"]

# Computer Selection
computer_choice = random.choice(options)

# User Selection
while True :
    user_choice = input("Make your Choice: (r)ock, (p)aper, (s)cissors? ")

# Run Conditionals
    if (user_choice == 'r' and computer_choice == 's') or (user_choice == 's' and computer_choice == 'p') or (user_choice == 'p' and computer_choice == 'r') :
        print(f"{user_choice} beats {computer_choice}, you win!")
        break
    elif (user_choice == 's' and computer_choice == 'r') or (user_choice == 'p' and computer_choice == 's') or (user_choice == 'r' and computer_choice == 'p') :
        print(f"{user_choice} beats {computer_choice}, you lose!")
        break
    else :
        print("Please input r, p, or s")
        
