from player import Player
from enemy import generate_enemy, generate_boss
from battle import battle
from save_system import save_game, load_game, list_saves, get_save_preview, delete_save

def manage_inventory(player):
    while True:
        print("\n🎒 Inventory:")
        for i, item in enumerate(player.inventory):
            equipped = ""
            if item == player.equipment.get("weapon") or item == player.equipment.get("armor"):
                equipped = "(Equipped)"
            print(f"{i+1}. {item} {equipped}")

        print("\nE. Equip Item")
        print("U. Use Potion")
        print("B. Back")

        choice = input("Choose: ").strip().lower()

        if choice == "b":
            break
        elif choice == "e":
            idx = input("Enter item number to equip: ").strip()
            if idx.isdigit():
                idx = int(idx) - 1
                if 0 <= idx < len(player.inventory):
                    item = player.inventory[idx]
                    if "Sword" in item:
                        player.equipment["weapon"] = item
                        player.attack += 5
                        print(f"⚔ Equipped {item} as weapon!")
                    elif "Armor" in item:
                        player.equipment["armor"] = item
                        player.hp += 20
                        print(f"🛡 Equipped {item} as armor!")
                    elif "Potion" in item:
                        print("💊 Potions cannot be equipped.")
                    else:
                        print("❌ Cannot equip this item.")
                else:
                    print("❌ Invalid item number.")
            else:
                print("❌ Invalid input.")
        elif choice == "u":
            idx = input("Enter potion number to use: ").strip()
            if idx.isdigit():
                idx = int(idx)-1
                if 0<=idx<len(player.inventory):
                    item = player.inventory[idx]
                    if "Potion" in item:
                        heal = 20
                        player.hp += heal
                        player.inventory.pop(idx)
                        print(f"💊 You used {item} and healed {heal} HP!")
                    else:
                        print("❌ That is not a potion.")
                else:
                    print("❌ Invalid item number.")
            else:
                print("❌ Invalid input.")
        else:
            print("❌ Invalid option.")

def main():
    print("=== 🐉 SHADOW OF TERMUX 🐉 ===")
    player = None

    while True:
        print("\n1. New Game")
        print("2. Load Game")
        print("3. Quit")

        choice = input("Choose: ").strip()

        if choice == "1":
            name = input("Enter hero name: ").strip().lower()
            saves = list_saves()
            if name in saves:
                print("❌ Save name already exists!")
                continue
            player = Player(name)
            player.save_slot = name
            print(f"🔥 Welcome, {name}!")
            break

        elif choice == "2":
            saves = list_saves()
            if not saves:
                print("❌ No save file found.")
                continue

            while True:
                print("\nAvailable Saves:\n")
                for i, save_name in enumerate(saves):
                    level, hp = get_save_preview(save_name)
                    print(f"{i+1}. {save_name} — Lv{level} • HP {hp}")

                print("\nD. Delete Save")
                print("B. Back")

                select = input("Select option: ").strip().lower()
                if select == "b":
                    break
                elif select == "d":
                    del_name = input("Enter save name to delete: ").strip().lower()
                    if delete_save(del_name):
                        print("🗑 Save deleted.")
                        saves = list_saves()
                    else:
                        print("❌ Save not found.")
                elif select.isdigit():
                    index = int(select)-1
                    if 0<=index<len(saves):
                        selected_name = saves[index]
                        data = load_game(selected_name)
                        player = Player.from_dict(data)
                        player.save_slot = selected_name
                        print("✅ Game loaded!")
                        break
                    else:
                        print("❌ Invalid number.")
                else:
                    print("❌ Invalid option.")

            if player:
                break

        elif choice == "3":
            print("Goodbye!")
            return
        else:
            print("❌ Invalid option!")

    while player.is_alive():
        print("\n1. Explore")
        print("2. Save Game")
        print("3. Inventory / Equip")
        print("4. Quit")

        choice = input("Choose: ").strip()

        if choice == "1":
            if player.level % 5 == 0 and player.level != 0:
                enemy = generate_boss(player.level)
            else:
                enemy = generate_enemy(player.level)
            battle(player, enemy)
        elif choice == "2":
            save_game(player)
            print("💾 Game saved!")
        elif choice == "3":
            manage_inventory(player)
        elif choice == "4":
            print("Goodbye, hero!")
            break
        else:
            print("❌ Invalid option!")

    print("\nGame Over.")

if __name__ == "__main__":
    main()
