import json
import os

SAVE_DIR = "saves"

if not os.path.exists(SAVE_DIR):
    os.makedirs(SAVE_DIR)


def save_game(player):
    if not player.save_slot:
        while True:
            save_name = input("Enter save name: ").strip().lower()

            if not save_name:
                print("❌ Save name cannot be empty.")
                continue

            filename = f"{save_name}.json"
            path = os.path.join(SAVE_DIR, filename)

            if os.path.exists(path):
                print("❌ Save name already exists! Choose another name.")
                continue

            player.save_slot = save_name
            break

    filename = f"{player.save_slot}.json"
    path = os.path.join(SAVE_DIR, filename)

    with open(path, "w") as f:
        json.dump(player.to_dict(), f)

    print(f"\n💾 Game saved in slot '{player.save_slot}'!") 
           
def list_saves():
    files = os.listdir(SAVE_DIR)
    saves = []

    for f in files:
        if f.endswith(".json"):
            saves.append(f.replace(".json", ""))  # hapus .json

    return saves

def load_game(save_name):
    filename = f"{save_name}.json"
    path = os.path.join(SAVE_DIR, filename)

    if not os.path.exists(path):
        return None

    with open(path, "r") as f:
        data = json.load(f)

    return data
