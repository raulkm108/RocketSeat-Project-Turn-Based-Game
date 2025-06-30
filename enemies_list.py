import random

enemies = [
    {
        "name":"Crab",
        "hp": 30,
        "lvl": 3,
        "ability": "ClawBurst",
        "type": "Water"
    },
    {
        "name": "Wolf",
        "hp": 50,
        "lvl": 4,
        "ability": "Ferocious Bite",
        "type": "Earth"
    },
    {
        "name": "Ogre",
        "hp": 80,
        "lvl": 5,
        "ability": "Mace Bonk",
        "type": "Air"
    },
    {
        "name": "Golem",
        "hp": 120,
        "lvl": 6,
        "ability": "Rock Slam",
        "type": "Rock"
    }
]

chosen_enemie = random.choice(enemies)
print(chosen_enemie)
print(*list(chosen_enemie.values()))