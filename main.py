from player import Player
from enemy import generate_enemy
from enemy import generate_enemy, generate_boss
from battle import battle
from save_system import save_game, load_game, list_saves
from colorama import init
import os

init()

def main():
    print("=== 🐉 SHADOW OF TERMUX 🐉 ===")

    while True:
        print("1. New Game")
        print("2. Load Game")

        start_choice = input("Choose: ")

        if start_choice == "1":
            name = input("Enter your hero name: ")
            player = Player(name)
            break

        elif start_choice == "2":
            saves = list_saves()

            if not saves:
                print("❌ No save files found.")
                continue

            print("\nAvailable Saves:")
            for i, save in enumerate(saves):
                print(f"{i + 1}. {save}")

            choice = input("Select save number: ")

            try:
                index = int(choice) - 1
                if index < 0 or index >= len(saves):
                    raise ValueError

                selected_name = saves[index]
                data = load_game(selected_name)

                player = Player.from_dict(data)
                player.save_slot = selected_name

                print("✅ Game loaded!")
                break
            except:
                print("❌ Invalid selection.")
                continue

        else:
            print("❌ Invalid choice. Please select 1 or 2.")
                   
    while player.is_alive():
        print("\n1. Explore")
        print("2. Save Game")
        print("3. Quit")

        choice = input("Choose: ")

        if choice == "1":
            if player.level % 5 == 0:
                print("\n🔥 BOSS ENCOUNTER 🔥")
                enemy = generate_enemy(player.level)
            else:
                enemy = generate_enemy(player.level)
            
            battle(player, enemy)

        elif choice == "2":
            save_game(player)

        elif choice == "3":
            print("Goodbye, hero!")
            break

        else:
            print("Invalid option!")

    print("\nGame Over.")

if __name__ == "__main__":
    main()
