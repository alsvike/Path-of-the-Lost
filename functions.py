#imports
import time
import os
import keyboard

# constants
from constants import weapons

# Description: Contains the functions used in the game.

# Print weapon information
def print_weapons(weapons):
    print("Available Weapons:\n")
    for weapon, stats in weapons.items():
        print(f"Weapon: {weapon.capitalize()}")
        print(f"  Min Damage : {stats['min_damage']}")
        print(f"  Max Damage : {stats['max_damage']}")
        print(f"  Durability : {stats['durability']}")
        print("-" * 30)

# Function to clear the screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Display menu function with selection
def display_menu(options, selected):
    clear_screen()
    print("=== Main Menu ===\n")
    
    # Display options, highlighting the selected one
    for i, option in enumerate(options):
        if i == selected:
            print(f"> [{i + 1}] {option} <")  # Highlight selected option
        else:
            print(f"  [{i + 1}] {option}")
    print("\nUse 'w' or UP for up, 's' or DOWN for down, and Enter to select.")

# Main menu function with navigation
def menu():
    options = ["Start Game", "Instructions", "Exit"]
    selected = 0
    
    # Display the menu for the first time
    display_menu(options, selected)

    # Wait for key presses
    while True:
        # Move up with 'w' or UP arrow key
        if (keyboard.is_pressed('w') or keyboard.is_pressed('up')) and selected > 0:
            selected -= 1
            display_menu(options, selected)
            time.sleep(0.2)  # Prevent fast cycling
            while keyboard.is_pressed('w') or keyboard.is_pressed('up'):  # Wait for key release
                pass
        # Move down with 's' or DOWN arrow key
        elif (keyboard.is_pressed('s') or keyboard.is_pressed('down')) and selected < len(options) - 1:
            selected += 1
            display_menu(options, selected)
            time.sleep(0.2)  # Prevent fast cycling
            while keyboard.is_pressed('s') or keyboard.is_pressed('down'):  # Wait for key release
                pass
        # Select the option with Enter
        elif keyboard.is_pressed('enter'):
            while keyboard.is_pressed('enter'):  # Wait for Enter release
                pass
            return selected + 1

# instructions function
def show_instructions():
    print("\n--- Instructions ---")
    print("1. Choose your weapon carefully. Each weapon has different damage and durability.")
    print("2. You will encounter different monsters on your journey.")
    print("3. During combat, press 'Enter' to attack.")
    print("4. Make choices wisely as they affect the outcome of your adventure.")

# animated text function
def animated_text(text, delay=0.055):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(delay)
    print()

# combat function
def combat(player, monster):
    print(f"A wild {monster.name} appears with {monster.hp} HP!")
    while monster.is_alive() and player.hp > 0:
        # Wait for the player to press Enter or Space to proceed with the attack
        action = input("Press 'Enter' to attack!")
        
        if action == "":
            player.attack(monster)
        else:
            print("Press 'Enter' to continue.")
            continue

        if monster.is_alive():
            player.take_damage(monster.attack)
        else:
            print(f"{monster.name} has been defeated!")

    # After combat ends
    if player.hp <= 0:
        print("You have been defeated!")
    else:
        print(f"You have defeated the monster! You continue on your journey with {player.hp} HP remaining.")

# Clear the console
def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')