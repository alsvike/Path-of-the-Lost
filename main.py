import random

# Define weapon stats with attack range
weapons = {
    "sword" : {"min_damage" : 10, "max_damage" : 14, "durability" : 12},     # Balanced option
    "axe" : {"min_damage" : 15, "max_damage" : 22, "durability" : 6},        # High damage, lower durability
    "bow" : {"min_damage" : 8, "max_damage" : 12, "durability" : 15},        # Medium-low damage, high durability
    "crossbow" : {"min_damage" : 18, "max_damage" : 25, "durability" : 5},    # High damage, very low durability
    "staff" : {"min_damage" : 5, "max_damage" : 9, "durability" : 18}         # Low damage, high durability
}

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

# game setup


should_we_play = input("Do you want to play? (yes/no)\n").lower()

if should_we_play == "yes" or should_we_play == "y":
    print("Let's play!")
    weapon_choice = input("Choose a weapon (sword/axe/bow/crossbow/staff)\n").lower()

    if weapon_choice not in weapons:
        print("Invalid weapon choice. You will be given a sword.")
        weapon_choice = "sword"
    else:
        print(f"You have chosen the {weapon_choice}!")

    player = Player(name, weapon_choice)

    direction = input("You come across a fork in the road. Do you go left or right? (left/right)\n").lower()
    if direction == "left":
        print("You encounter a goblin!")
        goblin = Monster("Goblin", 20, 5)
        combat(player, goblin)
    elif direction == "right":
        river_choice = input("You come across a river. Do you swim across or find a bridge? (swim/bridge)\n").lower()
        if river_choice == "swim":
            print("You are attacked by a river monster!")
            river_monster = Monster("River Monster", 30, 7)
            combat(player, river_monster)
        elif river_choice == "bridge":
            print("You find a bridge to cross and continue on your journey.")
        else:
            print("Invalid choice. You are swept away by the river and drown.")
    direction = input("You see a castle in the distance. Do you approach it? (yes/no)\n").lower()
    if direction == "yes" or direction == "y":
        print("You approach the castle and are greeted by the evil king!")
        king = Monster("King", 50, 10)
        combat(player, king)
    else:
        print("You decide to avoid the castle and continue on your journey.")
else:
    print("Goodbye!")