# Word-building Notebook
"""- **WEEK 7: World-Building Notebook**
**Constraints:**
- Use ONLY: JSON, dictionaries, `open()`
- Store: name, description, 3 key features
- No images or maps
- No linking between worlds
- No categories or tags
- Single JSON file

**Requirements:**
- Add world with 3 features
- List all worlds
- View single world details
- Save automatically"""

import json

def load_worlds():
    try:
        with open("Worlds.json", "r") as f:
            json.load(f)
    except FileNotFoundError:
        Worlds = []
    
Worlds = load_worlds()

def add_world():
    name = input("Enter world name: ").strip().title()
    description = input("Enter description: ").strip()
    key_feat_1 = input("Enter the first key feature of your world: ").strip()
    key_feat_2 = input("Enter the second key feature of your world: ").strip()
    key_feat_3 = input("Enter the third key feature of your world: ").strip()

    new_world = {
        'Name': name,
        'Description': description,
        'Key_1': key_feat_1,
        'Key_2': key_feat_2,
        'Key_3': key_feat_3
    }

    if not Worlds:
        with open("Worlds.json", 'w') as f:
            json.dump(new_world, f, indent=4)

    else:
        with open("Worlds.json", "a") as f:
            json.dump(new_world, f, indent=4)


def view_worlds():    
    try:
        with open("Worlds.json", "r") as f:
            worlds = json.load(f)
    except FileNotFoundError:
        return "No worlds created yet"
    
    print(worlds)
    

