from player import Player
from enemy import Enemy
from battle import battle
from save_system import (
    save_game,
    load_game,
    list_saves,
    get_save_preview,
    delete_save
)

def main():
    print("=== 🐉 SHADOW OF TERMUX 🐉 ===")

    player = None

    # ===== MAIN MENU =====
    while True:
        print("\n1. New Game")
        print("2. Load Game")
        print("3. Quit")

        choice = input("Choose: ").strip()

        # ===== NEW GAME =====
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

        # ===== LOAD GAME =====
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
                    index = int(select) - 1

                    if 0 <= index < len(saves):
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

    # ===== GAME LOOP =====
    while player.hp > 0:
        print("\n1. Explore")
        print("2. Save Game")
        print("3. Quit")

        choice = input("Choose: ").strip()

        if choice == "1":
            enemy = Enemy.generate(player.level)
            battle(player, enemy)

        elif choice == "2":
            save_game(player)
            print("💾 Game saved!")

        elif choice == "3":
            print("Goodbye, hero!")
            break

        else:
            print("❌ Invalid option!")

    print("\nGame Over.")


if __name__ == "__main__":
    main()
