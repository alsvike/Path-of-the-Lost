# packages
import time

# file imports
from constants import weapons
from classes import Player, Monster
from functions import menu, show_instructions, animated_text, combat, clear_console
from chapters import chapter1

def chapter1():
    # Introduction
        name = input("A distant voice calls through the mist. What is your name, wanderer? ")

        print(f"\nWelcome, {name}... to The Grey Hollow.")
        time.sleep(1.5)

        print("\nChapter 1: The Awakening")
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

        clear_console()

        # Weapon Selection
        weapon_choice = input("\nWhich weapon will you claim as your own? (sword, axe, bow, crossbow, or staff)\n").lower()

        if weapon_choice not in weapons:
            print("Invalid weapon choice. Defaulting to sword.")
            weapon_choice = "sword"
        
        print(f"\nYou reach for the {weapon_choice}, feeling its weight, its power—a silent companion for the journey ahead.")
        time.sleep(2.5)

        print("\nThe mist thickens around you, whispering ancient secrets, beckoning you forward into the heart of The Hollow.")
        time.sleep(3)
        print("\nYou are not alone here. The shadows are alive with danger, with creatures that hunger for your soul.")
        time.sleep(3)

        print("\nLet's begin your journey...")
        time.sleep(2)
        clear_console()

        # storyline begins
        print("\nYou stumble upon a crumbling shrine covered in vines, with offerings left at its base. A small inscription suggests that paying tribute may bring protection, but it’s unclear if it still holds power.")
        print("You have a choice to make: leave the shrine untouched, or make an offering.")
        time.sleep(3)
        choice = input("\nWill you make an offering? (yes or no)\n").lower()
        if choice == "yes":
            print("\nYou leave a small trinket at the base of the shrine, a token of your respect for the spirits that dwell here.")
            time.sleep(2)
            print("The shadows seem to recede slightly, as if the spirits have taken notice of your offering.")
            time.sleep(2)
            print("\nAs you continue on your journey, you feel a sense of protection surrounding you, a shield against the darkness.")
        elif choice == "no":
            print("\nYou decide to leave the shrine untouched, wary of the unknown forces that may dwell within.")
            time.sleep(2)
            print("The shadows seem to grow darker, as if the spirits are displeased with your choice.")
            time.sleep(2)
            print("\nAs you continue on your journey, you feel a sense of unease, as if the darkness is closing in around you.")
        else:
            print("\nInvalid choice. The shadows grow restless, sensing your indecision. You choose per default to make an offering.")
            time.sleep(2)
            print("You leave a small trinket at the base of the shrine, a token of your respect for the spirits that dwell")
            time.sleep(2)
            print("The shadows seem to recede slightly, as if the spirits have taken notice of your offering.")
            time.sleep(2)
            print("\nAs you continue on your journey, you feel a sense of protection surrounding you, a shield against the darkness.")