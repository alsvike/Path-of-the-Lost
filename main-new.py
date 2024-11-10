# packages
import time

# file imports
from constants import weapons
from classes import Player, Monster
from functions import menu, show_instructions, animated_text, combat, clear_console
from chapters import chapter1

# Show menu and get the first option
option = menu()  # Assigning the result of menu() to option

# Main loop
while option != 0:
    if option == 1:
        # Start chapter 1
        chapter1.chapter1()
    elif option == 2:
        show_instructions()
    elif option == 3:
        break  # Exit the game
    else:
        print("Invalid option. Please try again.")
    
    print()
    option = menu()  # Update option by calling menu() again


print("Thank you for playing!")
