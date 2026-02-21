import random

class Enemy:
    def __init__(self, name, hp, attack, level=1):
        self.name = name
        self.hp = hp
        self.attack = attack
        self.level = level

    def is_alive(self):
        return self.hp > 0

def generate_enemy(player_level):
    enemies = [
        ("Goblin", 30, 5),
        ("Skeleton", 40, 7),
        ("Orc", 50, 10),
        ("Dark Mage", 45, 12),
        ("Dragon", 80, 15)
    ]

    name, base_hp, base_attack = random.choice(enemies)
    hp = base_hp + (player_level * 5)
    attack = base_attack + (player_level * 2)
    return Enemy(name, hp, attack, level=player_level)

def generate_boss(player_level):
    bosses = [
        ("Orc Warlord", 120, 20),
        ("Dragon King", 200, 30),
        ("Demon Overlord", 300, 40)
    ]

    index = min(max(player_level // 5 - 1, 0), len(bosses) - 1)
    name, base_hp, base_attack = bosses[index]
    hp = base_hp + (player_level * 10)
    attack = base_attack + (player_level * 3)
    return Enemy(name, hp, attack, level=player_level)
