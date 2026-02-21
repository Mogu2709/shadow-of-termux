import random
from colorama import Fore, Style

def battle(player, enemy):
    print(Fore.RED + f"\n⚔️ A wild {enemy.name} appears!")
    print(Style.RESET_ALL)

    skill_cooldown = 0

    while player.is_alive() and enemy.is_alive():
        print(f"\n{player.name} HP: {player.hp}")
        print(f"{enemy.name} HP: {enemy.hp}")

        print("\nChoose action:")
        print("1. Attack")
        print("2. Power Strike (Skill)")
        print("3. Use Potion")
        print("4. Run")
        action = input(">> ")

        if action == "1":
            # Player attack
            damage = player.attack + random.randint(-2, 5)

            # Critical chance 20%
            if random.random() < 0.2:
                damage *= 2
                print(Fore.YELLOW + "💥 CRITICAL HIT!")
                print(Style.RESET_ALL)

            enemy.hp -= damage
            print(f"You dealt {damage} damage!")

        elif action == "2":
            if skill_cooldown == 0:
                damage = int(player.attack * 1.5)
                print("⚡ POWER STRIKE!")
                enemy.hp -= damage
                print(f"You deal {damage} damage!")
                skill_cooldown = 3 
            else:
                print(f"Skill on cooldown for {skill_cooldown} more turns!")
                continue
        
        elif action == "3":
                player.use_potion()
                continue

        elif action == "4":
            print("You ran away safely!")
            return

        else:
            print("Invalid choice!")
            continue

        # Enemy attack (if still alive)
        if enemy.is_alive():
            enemy_damage = enemy.attack + random.randint(-2, 3)
            player.hp -= enemy_damage
            print(Fore.MAGENTA + f"{enemy.name} attacks you for {enemy_damage} damage!")
            print(Style.RESET_ALL)
	
        if skill_cooldown > 0:
            skill_cooldown -= 1

    # End of battle
    if player.is_alive():
        print(Fore.GREEN + f"\n🎉 You defeated {enemy.name}!")
        print(Style.RESET_ALL)
        xp_gain = random.randint(20, 40)
        if "Warlord" in enemy.name or "King" in enemy.name or "Overlord" in enemy.name:
            print("🎁 Boss defeated! You found 2 extra potions!")
            player.potions += 2
        print(f"You gained {xp_gain} XP!")
        player.gain_xp(xp_gain)
    else:
        print(Fore.RED + "\n💀 You were defeated...")
        print(Style.RESET_ALL)
