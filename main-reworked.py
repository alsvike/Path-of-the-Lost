import random
import time

# values
# Define weapon stats with attack range
weapons = {
    "sword" : {"min_damage" : 10, "max_damage" : 14, "durability" : 12},     # Balanced option
    "axe" : {"min_damage" : 15, "max_damage" : 22, "durability" : 6},        # High damage, lower durability
    "bow" : {"min_damage" : 8, "max_damage" : 12, "durability" : 15},        # Medium-low damage, high durability
    "crossbow" : {"min_damage" : 18, "max_damage" : 25, "durability" : 5},    # High damage, very low durability
    "staff" : {"min_damage" : 5, "max_damage" : 9, "durability" : 18}         # Low damage, high durability
}

# classes
# define monster stats
class Monster:
    def __init__(self, name, hp, attack):
        self.name = name
        self.hp = hp
        self.attack = attack
    def is_alive(self):
        return self.hp > 0

# Define player
class Player:
    def __init__(self, name, weapon_choice):
        self.name = name
        self.hp = 100
        self.weapon = weapons[weapon_choice]  # Correctly assigns the dictionary of the chosen weapon stats

    def attack(self, monster):
        # Use random to determine damage within the weapon's attack range
        damage = random.randint(self.weapon["min_damage"], self.weapon["max_damage"])
        monster.hp -= damage
        print(f"{self.name} attacks {monster.name} with their weapon for {damage} damage!")
    
    def take_damage(self, damage):
        self.hp -= damage
        print(f"{self.name} takes {damage} damage! Current HP: {self.hp}")

# functions
def menu():
    print("[1] Start Game")
    print("[2] Instructions")
    print("[3] Exit")

def show_instructions():
    print("\n--- Instructions ---")
    print("1. Choose your weapon carefully. Each weapon has different damage and durability.")
    print("2. You will encounter different monsters on your journey.")
    print("3. During combat, press 'Enter' to attack.")
    print("4. Make choices wisely as they affect the outcome of your adventure.")

def animated_text(text, delay=0.07):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(delay)
    print()

# define combat function
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