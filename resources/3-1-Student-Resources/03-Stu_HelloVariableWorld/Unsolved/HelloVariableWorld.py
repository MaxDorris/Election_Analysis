
import time as t

# Create a variable called 'name' that holds a string

name = "Max"

# Create a variable called 'country' that holds a string

country = "The United States of America"

# Create a variable called 'age' that holds an integer

age = 21

# Create a variable called 'hourly_wage' that holds an integer

hourly_wage = 2.17

# Calculate the daily wage for the user

daily_wage = hourly_wage*8

# Create a variable called 'satisfied' that holds a boolean

satisfied = True

# Print out "Hello <name>!"

print(f"\nHello {name}!\n")

# Print out what country the user entered

print(f"You have entered {country}!\n")

# Print out the user's age

print(f"Based on only your appearance, we are\n documenting your age as {age} on our government\n records.\n\n")

# With an f-string, print out the daily wage that was calculated

print(f"Welcome, and we hope you enjoy your new\n job that pays ${hourly_wage} per hour.\n\n")

# With an f-string, print out whether the users were satisfied


while True :

    satisfaction = input("Are you satisfied with this rate?(Y/N)? : ")

    if satisfaction == 'Y' :
        print("\nGreat !\n")
        satisfied = False
        break

    elif satisfaction == 'N' :
        print("\nToo bad! :D\n")
        break

    else:
        print("\nPlease input 'Y' or 'N'\n")
        t.sleep(1)






