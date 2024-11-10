# packages
import random
import time

# file imports
from constants import weapons
from classes import Player, Monster
from functions import menu, show_instructions, animated_text, combat

# show menu
menu()
option = int(input("Choose an option: "))

while option != 0:
    if option == 1:
        animated_text(f"Hello, welcome to my game!")
    elif option == 2:
        show_instructions()
    elif option == 3:
        break
    else:
        print("Invalid option. Please try again.")
    
    print()
    menu()
    option = int(input("Choose an option: "))