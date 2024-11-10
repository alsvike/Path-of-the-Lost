#imports
import time

# Description: Contains the functions used in the game.

# menu function
def menu():
    print("[1] Start Game")
    print("[2] Instructions")
    print("[3] Exit")

# instructions function
def show_instructions():
    print("\n--- Instructions ---")
    print("1. Choose your weapon carefully. Each weapon has different damage and durability.")
    print("2. You will encounter different monsters on your journey.")
    print("3. During combat, press 'Enter' to attack.")
    print("4. Make choices wisely as they affect the outcome of your adventure.")

# animated text function
def animated_text(text, delay=0.07):
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
            print("Press only 'Enter' to continue.")
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