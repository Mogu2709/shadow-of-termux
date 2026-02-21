import os
import json

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
            path = os.path.join(SAVE_DIR, f"{save_name}.json")
            if os.path.exists(path):
                print("❌ Save name already exists!")
                continue
            player.save_slot = save_name
            break

    path = os.path.join(SAVE_DIR, f"{player.save_slot}.json")
    with open(path, "w") as f:
        json.dump(player.to_dict(), f)
    print(f"💾 Game saved in slot '{player.save_slot}'!")

def load_game(save_name):
    path = os.path.join(SAVE_DIR, f"{save_name}.json")
    if not os.path.exists(path):
        return None
    with open(path, "r") as f:
        return json.load(f)

def list_saves():
    return [f.replace(".json","") for f in os.listdir(SAVE_DIR) if f.endswith(".json")]

def get_save_preview(save_name):
    path = os.path.join(SAVE_DIR, f"{save_name}.json")
    with open(path, "r") as f:
        data = json.load(f)
    return data.get("level",1), data.get("hp",100)

def delete_save(save_name):
    path = os.path.join(SAVE_DIR, f"{save_name}.json")
    if os.path.exists(path):
        os.remove(path)
        return True
    return False
