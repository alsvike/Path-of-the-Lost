# packages
import time

# file imports
from constants import weapons, chapter1_choices
from classes import Player, Monster
from functions import menu, show_instructions, animated_text, combat, clear_console, print_weapons
from chapters import chapter1

def chapter1():
    # Introduction
        name = input("A distant voice calls through the mist. What is your name, wanderer? ")

        animated_text(f"\nWelcome, {name}... to The Grey Hollow.")
        time.sleep(1.5)

        animated_text("\nChapter 1: The Awakening")
        time.sleep(1.5)

        animated_text("\nYour consciousness stirs, caught somewhere between dreams and darkness, lost in fragments of memories you can’t grasp.")
        time.sleep(1.5)

        animated_text("You sense the cold before you fully awaken, the damp earth pressing against your skin like a shroud.")
        time.sleep(2)

        animated_text("\nThe silence around you is thick, pressing, holding its breath as you slowly open your eyes to an unfamiliar, foreboding landscape.")
        time.sleep(2)

        animated_text("A sense of purpose stirs within you, an urgent need to press forward into the unknown.")
        time.sleep(2.5)

        animated_text("\nBut first, you will need a weapon. The Hollow is not a place for the unarmed.")
        time.sleep(2)

        animated_text("Each choice carries a promise... and a curse. Choose wisely.")
        time.sleep(2)

        clear_console()

        # Weapon Selection
        print_weapons(weapons)
        weapon_choice = input("\nWhich weapon will you claim as your own? (sword, axe, bow, crossbow, or staff)\n").lower()

        if weapon_choice not in weapons:
            print("Invalid weapon choice. Defaulting to sword.")
            weapon_choice = "sword"
        
        animated_text(f"\nYou reach for the {weapon_choice}, feeling its weight, its power—a silent companion for the journey ahead.")
        time.sleep(2.5)

        animated_text("\nThe mist thickens around you, whispering ancient secrets, beckoning you forward into the heart of The Hollow.")
        time.sleep(3)
        animated_text("\nYou are not alone here. The shadows are alive with danger, with creatures that hunger for your soul.")
        time.sleep(3)

        animated_text("\nLet's begin your journey...")
        time.sleep(2)
        clear_console()

        # storyline begins
        animated_text("\nYou stumble upon a crumbling shrine covered in vines, with offerings left at its base. A small inscription suggests that paying tribute may bring protection, but it’s unclear if it still holds power.")
        animated_text("You have a choice to make: leave the shrine untouched, or make an offering.")
        time.sleep(3)
        choice = input("\nWill you make an offering? (yes or no)\n").lower()
        if choice == "yes":
            print("\nYou leave a small trinket at the base of the shrine, a token of your respect for the spirits that dwell here.")
            time.sleep(2)
            print("The shadows seem to recede slightly, as if the spirits have taken notice of your offering.")
            time.sleep(2)
            print("\nAs you continue on your journey, you feel a sense of protection surrounding you, a shield against the darkness.")
            chapter1_choices["ancient_shrine"] = True
        elif choice == "no":
            print("\nYou decide to leave the shrine untouched, wary of the unknown forces that may dwell within.")
            time.sleep(2)
            print("The shadows seem to grow darker, as if the spirits are displeased with your choice.")
            time.sleep(2)
            print("\nAs you continue on your journey, you feel a sense of unease, as if the darkness is closing in around you.")
            chapter1_choices["ancient_shrine"] = False
        else:
            print("\nInvalid choice. The shadows grow restless, sensing your indecision. You choose per default to make an offering.")
            time.sleep(2)
            print("You leave a small trinket at the base of the shrine, a token of your respect for the spirits that dwell")
            time.sleep(2)
            print("The shadows seem to recede slightly, as if the spirits have taken notice of your offering.")
            time.sleep(2)
            print("\nAs you continue on your journey, you feel a sense of protection surrounding you, a shield against the darkness.")
            chapter1_choices["ancient_shrine"] = True

        print("\nYou press on, the path ahead shrouded in mist and mystery, the shadows whispering your name.")
        time.sleep(2)
        print("You reach a fork in the road, the path to the left leading to an abandoned camp, while the path to the right disappears into a dense thicket of thorns.")
        time.sleep(2)
        print("You must choose your path wisely, for each step brings you closer to the heart of The Hollow.")
        time.sleep(2)
        clear_console()
        print("Do you go left towards the abandoned camp, or right into the thicket of thorns?")
        time.sleep(2)
        choice = input("\nWhich path will you take? (left or right)\n").lower()
        if choice == "left":
            print("\nYou find an old, abandoned camp with a rusted shield and broken supplies strewn about.")
            time.sleep(2)
            print("It seems untouched for ages, yet something feels off.")
            time.sleep(2)
            print("Do you search the camp for supplies, or continue on your journey?")
            time.sleep(2)
            choice = input("\nWill you search the camp? (yes or no)\n").lower()
            if choice == "yes":
                print("\nYou rummage through the broken supplies, finding a few useful items hidden among the debris.")
                time.sleep(2)
                print("As you leave the camp, you feel a sense of satisfaction, as if fate has smiled upon your choice.")
            if choice == "no":
                print("\nYou decide to leave the camp undisturbed, wary of the shadows that linger here.")
                time.sleep(2)
                print("As you continue on your journey, you feel a sense of unease, as if unseen eyes watch your every move.")
        elif choice == "right":
            print("\nYou push through the thicket of thorns, feeling the sting of their sharp edges against your skin.")
            time.sleep(2)
            print("The path twists and turns, the shadows closing in around you, the air thick with the scent of decay.")
            time.sleep(2)
            print("You come upon a clearing, a small patch of suspicious mushrooms glowing with an otherworldly light.")
            time.sleep(2)
            print("Do you eat the mushrooms, or press on into the darkness?")
            time.sleep(2)
            choice = input("\nWill you eat the mushrooms? (yes or no)\n").lower()
            if choice == "yes":
                print("\nYou consume the glowing mushrooms, feeling a surge of energy coursing through your veins.")
                time.sleep(2)
                print("The shadows seem to retreat, as if repelled by the strange light within you.")
                time.sleep(2)
                print("As you press on, you feel a sense of clarity, a sharpness of mind that was lacking before.")
            elif choice == "no":
                print("\nYou decide to press on, wary of the strange glow emanating from the mushrooms.")
                time.sleep(2)
                print("The shadows seem to grow darker, as if drawn to the light that you have rejected.")
                time.sleep(2)
                print("As you continue on your journey, you feel a sense of unease, as if the darkness is closing in around you.")