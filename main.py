# Word-building Notebook
import json

def load_worlds():
    try:
        with open("Worlds.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []
    
Worlds = load_worlds()

def add_world():
    while True:
        name = input("Enter world name: ").strip().title()

        if not name:
            print("Name cannot be empty. :|")
            print("Even a placeholder will do if you haven't found the one yet.")
            continue
        else:
            break

    while True:
        description = input("Enter description: ").strip()

        if not description:
            print("This is a CLI, you need a little something to help you remeber your world.")
            print("Try at least one line.")
            continue
        else:
            break

    while True:
        key_feat_1 = input("Enter the first key feature of your world: ").strip()

        if not key_feat_1:
            print("Give me something please.")
            print("I'm starving here.")
            continue
        else:
            break

    key_feat_2 = input("Enter the second key feature of your world: ").strip()
    key_feat_3 = input("Enter the third key feature of your world: ").strip()

    new_world = {
        'Name': name,
        'Description': description,
        'Key_1': key_feat_1,
        'Key_2': key_feat_2,
        'Key_3': key_feat_3
    }

    worlds = load_worlds()  # Get current list
    worlds.append(new_world)  # Add new world

    with open("Worlds.json", "w") as f:
        json.dump(worlds, f, indent=4)  # Write ALL worlds


def view_worlds():    
    try:
        with open("Worlds.json", "r") as f:
            worlds = json.load(f)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []
    
    worlds_list = worlds
    
    for world in worlds_list:
        print(f"{world['Name']}, \n{world['Description']}, \n{world['Key_1']}, \n{world['Key_2']}, \n{world['Key_3']}")
    

def view_single_world():
    try:
        with open("Worlds.json", "r") as f:
            worlds = json.load(f)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []
    
    world_name = input("Enter the name of the world you like to view: ")

    for world in worlds:
        if world['Name'] == world_name:
            print(f"{world['Name']}, \n{world['Description']}, \n{world['Key_1']}, \n{world['Key_2']}, \n{world['Key_3']}")



print("Sometimes we dream up whole worlds.")
print("And sometimes we forget them because we never thought to write them down.")
print("So let's carve out a space for all the worlds that could have been, that are and that will be.")
print("Type 'add', 'view all', 'view one' or 'quit'.")
print("Pretty easy to start don't you think?\n")

while option := input("What would you like to do? ('add'/'view all'/'view one'/'quit/): ").strip().lower():
    match option:
        case 'add':
            add_world()
        case 'view all':
            view_worlds()
        case 'view one':
            view_single_world()
        case 'quit':
            print("I'll see you again when you dream up the next one.")
            print("DOn't take too long.")
            break