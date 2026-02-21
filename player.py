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

        # Inventory & Equipment
        self.inventory = []
        self.equipment = {"weapon": None, "armor": None}

        # Skills
        self.skills = ["Slash", "Fireball"]

    def is_alive(self):
        return self.hp > 0

    # Convert to dictionary for saving
    def to_dict(self):
        return {
            "name": self.name,
            "hp": self.hp,
            "attack": self.attack,
            "level": self.level,
            "xp": self.xp,
            "potions": self.potions,
            "save_slot": self.save_slot,
            "inventory": self.inventory,
            "equipment": self.equipment,
            "skills": self.skills
        }

    # Load from dictionary
    @staticmethod
    def from_dict(data):
        p = Player(
            data["name"],
            data["hp"],
            data["attack"],
            data["level"],
            data["xp"],
            data["potions"],
            data.get("save_slot")
        )
        p.inventory = data.get("inventory", [])
        p.equipment = data.get("equipment", {"weapon": None, "armor": None})
        p.skills = data.get("skills", ["Slash", "Fireball"])
        return p

    # Use a skill
    def use_skill(self, skill_name, target):
        if skill_name == "Slash":
            dmg = self.attack + 5
            target.hp -= dmg
            print(f"⚡ {self.name} used Slash! {dmg} damage dealt!")
        elif skill_name == "Fireball":
            dmg = self.attack + 10
            target.hp -= dmg
            print(f"🔥 {self.name} cast Fireball! {dmg} damage dealt!")
        elif skill_name == "Heal":
            heal_amount = 30
            self.hp += heal_amount
            print(f"💖 {self.name} used Heal! Restored {heal_amount} HP!")
        else:
            print(f"❌ Unknown skill: {skill_name}")

    # Gain XP (simple leveling)
    def gain_xp(self, amount):
        self.xp += amount
        while self.xp >= self.level * 50:
            self.xp -= self.level * 50
            self.level += 1
            self.hp += 10
            self.attack += 2
            print(f"🎉 {self.name} leveled up to Lv{self.level}!")
