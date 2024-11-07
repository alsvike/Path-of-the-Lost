# Path of the Lost

**Path of the Lost** is a text-based adventure game currently in early development. Players embark on a journey through a perilous world, where they encounter monsters, make crucial choices, and rely on their weapons' unique stats to survive. *Note: The game is still in its initial stages, and a full gameplay experience is not yet possible.*


## Features

- **Weapon Selection**: Players choose from five weapons, each with distinct stats:
  - **Sword**: Balanced, with moderate damage and durability.
  - **Axe**: High damage, lower durability.
  - **Bow**: Medium-low damage, high durability.
  - **Crossbow**: Very high damage, very low durability.
  - **Staff**: Low damage, high durability.
- **Turn-Based Combat**: Engage in strategic battles with monsters.
- **Branching Paths**: Players make choices that impact their journey, leading to unique encounters or dangers.
- **Monster Encounters**: Encounter different monsters, each with unique stats and attacks.

## Gameplay

1. **Introduction**: The game prompts for the player’s name and greets them.
2. **Weapon Choice**: Players select their weapon from available options, each with specific damage and durability attributes.
3. **Path Selection**: Players encounter a fork in the road and must choose their path.
4. **Combat**: Players engage in turn-based combat with monsters. Combat continues until either the player or the monster is defeated.
5. **Victory or Defeat**: If the player defeats the monster, they continue on their journey. If they lose all health, the game ends in defeat.

## Example Code Snippet

```python
# Start combat with a monster
goblin = Monster("Goblin", 20, 5)
combat(player, goblin)
```

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/path-of-the-lost.git
   ```
2. Navigate to the project directory:
   ```bash
   cd path-of-the-lost
   ```
3. Run the game:
   ```bash
   python main.py
   ```

## Roadmap

- **Durability**: Make use of the durability the weapons have to make them breakable
- **Additional Weapons**: Add more weapons with unique abilities or effects.
- **New Monsters**: Include more monster types with unique attacks.
- **Extended Storyline**: Increase replayability with additional paths and choices.
- **Inventory System**: Add an inventory system
- **Loot tables**: Add loot tables to monsters
- **Abilities**: Add abilities to the weapons
- **Add a main menu**: Add a main menu
