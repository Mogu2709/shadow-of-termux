import random
from colorama import Fore, Style

def battle(player, enemy):
    print(f"\n⚔ Encounter! {enemy.name} appears! Lv{enemy.level}")
    while player.is_alive() and enemy.is_alive():
        print(f"\nYour HP: {player.hp} | Enemy HP: {enemy.hp}")
        print("1. Attack")
        print("2. Use Potion")
        print("3. Use Skill")

        choice = input("Choose action: ").strip()

        if choice == "1":
            dmg = player.attack
            if player.equipment.get("weapon"):
                dmg += 5
            enemy.hp -= dmg
            print(f"➡ You dealt {dmg} damage!")

        elif choice == "2":
            if player.potions > 0:
                heal = 20
                player.hp += heal
                player.potions -= 1
                print(f"💊 You used a potion and healed {heal} HP!")
            else:
                print("❌ No potions left!")

        elif choice == "3":
            print("Available Skills:")
            for i, s in enumerate(player.skills):
                print(f"{i+1}. {s}")
            idx = input("Select skill: ").strip()
            if idx.isdigit():
                idx = int(idx) - 1
                if 0 <= idx < len(player.skills):
                    skill_name = player.skills[idx]
                    player.use_skill(skill_name, enemy)
                else:
                    print("❌ Invalid skill number.")
            else:
                print("❌ Invalid input.")
        else:
            print("❌ Invalid action!")
            continue

        if enemy.is_alive():
            dmg = enemy.attack
            if player.equipment.get("armor"):
                dmg -= 5
                dmg = max(0, dmg)
            player.hp -= dmg
            print(f"⬅ {enemy.name} dealt {dmg} damage!")

    # After battle
    if player.is_alive():
        print(f"\n✅ You defeated {enemy.name}!")

        if "Dragon" in enemy.name or "Warlord" in enemy.name or "Overlord" in enemy.name:
            print("🎁 Boss defeated! You found 2 extra potions!")
            player.potions += 2

        loot_chance = random.randint(1, 100)
        if loot_chance <= 50:
            item = random.choice(["Iron Sword", "Steel Armor", "Health Potion"])
            player.inventory.append(item)
            print(f"🎁 You found: {item}!")

        xp_gain = enemy.level * 10
        print(f"You gained {xp_gain} XP!")
        player.gain_xp(xp_gain)

    else:
        print(Fore.RED + "\n💀 You were defeated...")
        print(Style.RESET_ALL)
