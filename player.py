import json

class Player:
    def __init__(self, name, hp=100, attack=10, level=1, xp=0, potions=3, save_slot=None):
        self.name = name
        self.hp = hp
        self.attack = attack
        self.level = level
        self.xp = xp
        self.potions = potions
        self.save_slot = save_slot

    def is_alive(self):
        return self.hp > 0

    def use_potion(self):
        if self.potions > 0:
                self.hp += 30
                self.potions -= 1
                print(f"\n🧪 You used a potion! +30 HP")
                print(f"Potions left: {self.potions}")
        else:
                print("\n❌ No potions left!")


    def gain_xp(self, amount):
        self.xp += amount
        if self.xp >= 50:
            self.level_up()

    def level_up(self):
        self.level += 1
        self.hp += 20
        self.attack += 5
        self.xp = 0
        print(f"\n🔥 LEVEL UP! You are now level {self.level}!")
        print(f"HP increased to {self.hp}")
        print(f"Attack increased to {self.attack}")

    def to_dict(self):
        return {
            "name": self.name,
            "hp": self.hp,
            "attack": self.attack,
            "level": self.level,
            "xp": self.xp,
            "potions": self.potions,
            "save_slot":self.save_slot
        }

    @staticmethod
    def from_dict(data):
        return Player(
            data["name"],
            data["hp"],
            data["attack"],
            data["level"],
            data["xp"],
            data["potions"],
            data.get("save_slot")
        )
