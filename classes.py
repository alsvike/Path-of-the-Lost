# imports
import random
from constants import weapons

class Monster:
    def __init__(self, name, hp, attack):
        self.name = name
        self.hp = hp
        self.attack = attack
    def is_alive(self):
        return self.hp > 0

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