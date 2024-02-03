import random
from prettytable import PrettyTable
import easygui

# Generating a random number between 1 and 102
num = random.randint(1, 102)

# Setting up the table
table = PrettyTable()
table.field_names = ["Guess", "Result"]

# Main game loop
while True:
    # Getting user input
    guess = easygui.enterbox("Guess a number between 1 and 102:")

    try:
        guess = int(guess)
    except ValueError:
        easygui.msgbox("Invalid input! Please enter a valid number.")
        continue

    # Checking if the guess is correct
    if guess == num:
        table.add_row([guess, "Yeah! You won!"])
        easygui.msgbox(str(table))
        break
    else:
        table.add_row([guess, "Oops, try again!"])
        easygui.msgbox(str(table))
