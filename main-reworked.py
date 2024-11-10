# packages
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
        # Introduction
        name = input("A distant voice calls through the mist. What is your name, wanderer? ")

        print(f"\nWelcome, {name}... to The Grey Hollow.")
        time.sleep(1.5)

        print("\nYou awaken from a haze of memories, your mind clouded, your limbs heavy.")
        time.sleep(1.5)

        print("The ground beneath you is cold and damp, the scent of moss and decay filling the air around you.")
        time.sleep(2)

        print("\nAs you rise, shadows cling to you, the forest looming dark and twisted, as if alive.")
        time.sleep(2)

        print("A sense of purpose stirs within you, an urgent need to press forward into the unknown.")
        time.sleep(2.5)

        print("\nBut first, you will need a weapon. The Hollow is not a place for the unarmed.")
        time.sleep(2)

        print("Each choice carries a promise... and a curse. Choose wisely.")
        time.sleep(2)

        # Weapon Selection
        weapon_choice = input("\nWhich weapon will you claim as your own? (sword, axe, bow, crossbow, or staff)\n").lower()
        print(f"\nYou reach for the {weapon_choice}, feeling its weight, its power—a silent companion for the journey ahead.")
        time.sleep(2.5)

        print("\nThe mist thickens around you, whispering ancient secrets, beckoning you forward into the heart of The Hollow.")
        time.sleep(3)
    elif option == 2:
        show_instructions()
    elif option == 3:
        break
    else:
        print("Invalid option. Please try again.")
    
    print()
    menu()
    option = int(input("Choose an option: "))