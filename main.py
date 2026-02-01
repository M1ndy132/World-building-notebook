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

def get_valid_input(prompt, error_message, transform=str.strip):
    while True:
        user_input = input(prompt).strip()
        if transform:
            user_input = transform(user_input)
        
        if not user_input:
            print(error_message)
            continue
        else:
            return user_input
        
def get_input(prompt, input_type=None, transform=None):
    user_input = input(prompt).strip()
    
    if input_type == list:
        # Split by comma and strip whitespace from each item
        return [item.strip() for item in user_input.split(",") if item.strip()]
    elif input_type == dict:
        # For simple key:value pairs separated by commas
        # Example: "key1:value1, key2:value2"
        result = {}
        for pair in user_input.split(","):
            if ":" in pair:
                key, value = pair.split(":", 1)
                result[key.strip()] = value.strip()
        return result
    else:
        # Default string handling
        if transform:
            user_input = transform(user_input)
        return user_input
    
def print_world_details(world):
    """Print formatted world details"""
    print(f"\n{'='*50}")
    print(f"📖 WORLD: {world.get('Name', 'Unnamed')}")
    print(f"{'='*50}")
    
    for key, value in world.items():
        if key == 'Name':
            continue  # Already printed in header
        print(f"\n🔹 {key}:")
        # Handle different value types
        if isinstance(value, list):
            for i, item in enumerate(value, 1):
                print(f"   {i}. {item}")
        else:
            print(f"   {value}")
    print(f"{'='*50}\n")
    
def save_worlds(worlds):
    """Save worlds to JSON file"""
    with open("Worlds.json", "w") as f:
        json.dump(worlds, f, indent=4)
        
def add_world():
    name = get_valid_input(
        "Enter world name: ",
        "Name cannot be empty. :|\nEven a placeholder will do if you haven't found the one yet.",
        str.title
    )


    description = get_valid_input(
        "Enter description: ",
        "This is a CLI, you need a little something to help you remeber your world.\nTry at least one line."
    )

    tone = get_valid_input(
        "Enter the tone of your world: ",
        "What are we supposed to feel, give me a sneak peek pleaseeeeee."
    )

    genre = get_valid_input(
        "What's the genre? ",
        "It most fit somewhere.\nIt can even be a made up one",
        str.capitalize
    )

    rules = get_input("Enter your primary rules, those which will never change (comma separated): ", input_type=list)
    scope = get_input("Enter the scope of your world (planet, pocket-dimension, city-state, etc): ", input_type=str, transform=str.capitalize)
    timeframe = get_input("Enter timeframe: ", input_type=str, transform=str.capitalize)

    geo_features = get_input("Enter major geographic features (continents, mountain ranges, oceans), (key:value pairs): ", input_type=dict)
    climate = get_input("Enter climate: ")
    hazards = get_input("Enter natural hazards (comma separated): ", input_type=list)
    resources = get_input("Enter resources (comma separated): ", input_type=list)

    creation_myths = get_input("Enter creation myths: ")
    factual_history = get_input("Enter factual history: ")
    eras = get_input("Enter major eras (comma separated): ", input_type=list)
    events_log = get_input("Enter key events (comma separated): ", input_type=list)

    cultures = get_input("Enter major cultures (comma separated): ", input_type=list)
    norms = get_input("Enter cultural norms (comma separated): ", input_type=list)
    taboos = get_input("Enter taboos (comma separated): ", input_type=list)
    Rites = get_input("Enter holidays/rites/rituals (comma separated): ", input_type=list)

    government = get_input("Enter government types (comma separated): ", input_type=list)
    power_players = get_input("Enter power players (comma separated): ", input_type=list)
    justice = get_input("Enter law/enforcement/justice system: ")

    money_systems = get_input("Enter money systems (key:value pairs): ", input_type=dict)
    industries = get_input("Enter key industries (comma separated): ", input_type=list)
    trade_routes = get_input("Enter trade routes (comma separated): ", input_type=list)

    tech_lvl = get_input("Enter tech level: ")
    key_inventions = get_input("Enter key inventions (comma separated): ", input_type=list)
    built_env = get_input("Enter built environment details: ")
    maintenance = get_input("Enter maintenance/longevity details: ")

    mechanics = get_input("Enter magic mechanics: ")
    limits = get_input("Enter magic limits: ")
    practitioners = get_input("Enter practitioners/institutions: ")
    cultural_role = get_input("Enter cultural role of magic: ")

    basic_needs = get_input("Enter how basic needs are met: ")
    edu = get_input("Enter education system: ")
    entertainment = get_input("Enter entertainment: ")

    maj_philosophies = get_input("Enter major philosophies (comma separated): ", input_type=list)
    legends = get_input("Enter urban legends (comma separated): ", input_type=list)
    ethics = get_input("Enter morality systems: ")

    flora = get_input("Enter flora (comma separated): ", input_type=list)
    fauna = get_input("Enter fauna (comma separated): ", input_type=list)
    disease = get_input("Enter diseases: ")
    medicine = get_input("Enter medicine practices: ")
    env_interact = get_input("Enter environmental interactions: ")

    ext_threats = get_input("Enter external threats (comma separated): ", input_type=list)
    int_threats = get_input("Enter internal threats (comma separated): ", input_type=list)
    crisis_mechs = get_input("Enter crisis mechanics: ")

    archetypal_figures = get_input("Enter archetypal figures (comma separated): ", input_type=list)
    signature_bios = get_input("Enter signature character bios (key:value pairs): ", input_type=dict)
    relationships = get_input("Enter relationships & rivalries: ")

    naming_conventions = get_input("Enter naming conventions: ")
    common_phrases = get_input("Enter common phrases/idioms (comma separated): ", input_type=list)
    written_forms = get_input("Enter written forms & recordkeeping: ")

    iconography = get_input("Enter iconography & symbols: ")
    artifacts = get_input("Enter key artifacts & relics (comma separated): ", input_type=list)
    visual_refs = get_input("Enter visual references: ")

    player_systems = get_input("Enter player-facing systems: ")
    progression = get_input("Enter progression & consequences: ")
    event_triggers = get_input("Enter event triggers & scenes (comma separated): ", input_type=list)

    inspirations = get_input("Enter inspirations & references (comma separated): ", input_type=list)
    open_questions = get_input("Enter open questions & research tasks: ")
    plausibility_notes = get_input("Enter notes on plausibility: ")

    glossary = get_input("Enter glossary terms (key:value pairs): ", input_type=dict)
    cross_refs = get_input("Enter index of cross-references: ")
    what_if_sketches = get_input("Enter 'what if' sketches: ")
    deadlines = get_input("Enter deadlines & milestones: ")

    new_world = {
        'Name': name,
        'Core': {
            'Description': description,
            'Tone': tone,
            'Genre': genre,
        },
        'Foundations': {
            'Primary Rules': rules,
            'Scale/Scope': scope,
            'Timeframe': timeframe
        },
        'Geography': {
            'Maps/features': geo_features,
            'Climate': climate,
            'Natrual hazards': hazards,
            'Resources': resources
        },
        'History': {
            'Creation myths': creation_myths,
            'Factual History': factual_history,
            'Major eras': eras,
            'Key events log': events_log
        },
        'Cultures/Societies': {
            'Major Cultures': cultures,
            'Norms': norms,
            'Taboos': taboos,
            'Holidays/rites/rituals': Rites,
        },
        'Politics/Power': {
            'Governments': government,
            'Power players': power_players,
            'Law, enforcement, justics': justice
        },
        'Economy': {
            'Money systems': money_systems,
            'Key Industries': industries,
            'Trade Routes': trade_routes
        },
        'Technology': {
            'Tech level': tech_lvl,
            'Key inventions': key_inventions,
            'Built Environment': built_env,
            'Maintenance/Longevity': maintenance
        },
        'Magic': {
            'Mechanics': mechanics,
            'Limits': limits,
            'Practitioners/Institutions': practitioners,
            'Cultural Role': cultural_role
        },
        'Daily Life': {
            'Basic needs': basic_needs,
            'Education': edu,
            'Entertainment': entertainment
        },
        'Philosophy': {
            'Major Philosophies': maj_philosophies,
            'Urban Legends': legends,
            'Morality systems': ethics
        },
        'Ecology, Biology': {
            'Flora': flora,
            'Fauna': fauna,
            'Disease': disease,
            'Medicine': medicine,
            'Environmental Interactions': env_interact
        },
        'Conflict': {
            'External Threats': ext_threats,
            'Internal Threats': int_threats,
            'Crisis mechanics': crisis_mechs
        },
        'Notable Characters & NPCs': {
            'Archetypal figures': archetypal_figures,
            'Signature bios': signature_bios,
            'Relationships & rivalries': relationships
        },
        'Language, Names & Scripts': {
            'Naming conventions': naming_conventions,
            'Common phrases & idioms': common_phrases,
            'Written forms & recordkeeping': written_forms
        },
        'Maps, Visuals & Artifacts': {
            'Iconography & symbols': iconography,
            'Key artifacts & relics': artifacts,
            'Visual references': visual_refs
        },
        'Mechanics for Stories/Games': {
            'Player-facing systems': player_systems,
            'Progression & consequences': progression,
            'Event triggers & scenes': event_triggers
        },
        'Research & Sources': {
            'Inspirations & references': inspirations,
            'Open questions & research tasks': open_questions,
            'Notes on plausibility': plausibility_notes
        },
        'Appendices & Expandables': {
            'Glossary': glossary,
            'Index of cross-references': cross_refs,
            'What if sketches': what_if_sketches,
            'Deadlines & milestones': deadlines
        }
    }

    worlds = load_worlds()  # Get current list
    worlds.append(new_world)  # Add new world

    save_worlds(worlds)


def view_worlds():    
    worlds = load_worlds()

    if not worlds:
        print("No worlds to view. Go add one!")
    else:
        worlds_list = worlds
        
        for world in worlds_list:
            print(f"{world['Name']}, \n{world['Description']}, \n{world['Key_1']}, \n{world['Key_2']}, \n{world['Key_3']}")
    

def view_single_world():
    worlds = load_worlds()

    if not worlds:
        print("No worlds to view. Go add one!")
    else:
        print("Your list of worlds: ")
        for world in worlds:
            print(world['Name'])
            
        world_name = input("Enter the name of the world you like to view: ")

        for world in worlds:
            if world['Name'] == world_name:
                print(f"{world['Name']}, \n{world['Description']}, \n{world['Key_1']}, \n{world['Key_2']}, \n{world['Key_3']}")

def edit_world():
    worlds = load_worlds()

    if not worlds:
        print("\nNo worlds to edit. Create one first!")
    else:

        # 1. SELECT WORLD
        print("\nEDIT WORLD")
        print("="*50)
        print("\nAVAILABLE WORLDS:")
        for i, world in enumerate(worlds, 1):
            print(f"{i}. {world.get('Name', 'Unnamed')}")
        
        while True:
            try:
                choice = input("\nEnter world number to edit: ").strip()
                if choice.isdigit():
                    idx = int(choice) - 1
                    if 0 <= idx < len(worlds):
                        world = worlds[idx]
                        break
                    print(f"Please enter 1-{len(worlds)}")
                else:
                    print("Please enter a number.")
            except ValueError:
                print("Invalid input.")
        
        original_name = world.get('Name', 'Unnamed')
        print(f"\nEDITING: {original_name}")
        
    # 2. SHOW CURRENT VALUES
        print("\nCURRENT VALUES:")
        print("-"*30)
        
        keys = list(world.keys())
        for i, key in enumerate(keys, 1):
            value = world[key]
            if isinstance(value, list):
                display = f"[List with {len(value)} items]"
            elif isinstance(value, str) and len(value) > 50:
                display = value[:50] + "..."
            else:
                display = value
            print(f"{i}. {key}: {display}")

        # 3. EDITING MENU
        while True:
            print("\nEDIT OPTIONS:")
            print("1. Edit existing field")
            print("2. Add new field")
            print("3. Add to list (Features/Categories)")
            print("4. Remove from list (Features/Categories)")
            print("5. Remove field entirely")
            print("6. Finish editing")
            
            option = input("\nChoose option (1-6): ").strip()
            
            if option == '1':  # Edit existing field
                print("\nEDIT EXISTING FIELD")
                print("Available fields:", ", ".join(keys))
                
                while True:
                    field = input("Field to edit: ").strip()
                    if field in world:
                        break
                    print(f"'{field}' not found. Try: {', '.join(keys)}")
                
                current = world[field]
                print(f"\nCurrent value: {current}")
                
                if isinstance(current, list):
                    print("\nCurrent items:")
                    for i, item in enumerate(current, 1):
                        print(f"  {i}. {item}")
                    
                    sub_opt = input("\nEdit (r)eplace entire list or (m)odify items? [r/m]: ").strip().lower()
                    
                    if sub_opt == 'r':
                        new_list = []
                        print("\nEnter new items (one per line, 'done' when finished):")
                        i = 1
                        while True:
                            item = input(f"Item {i}: ").strip()
                            if item.lower() == 'done':
                                break
                            if item:
                                new_list.append(item)
                                i += 1
                        world[field] = new_list
                        print(f"{field} updated!")
                    
                    elif sub_opt == 'm':
                        print("\nWhich item to modify?")
                        for i, item in enumerate(current, 1):
                            print(f"{i}. {item}")
                        
                        try:
                            item_idx = int(input("Item number: ")) - 1
                            if 0 <= item_idx < len(current):
                                new_value = input(f"New value for '{current[item_idx]}': ").strip()
                                if new_value:
                                    current[item_idx] = new_value
                                    print("Item updated!")
                                else:
                                    print("Item cannot be empty.")
                            else:
                                print("Invalid number.")
                        except ValueError:
                            print("Please enter a number.")
                
                else:  # String field
                    new_value = input(f"New value for {field}: ").strip()
                    if new_value:
                        world[field] = new_value
                        print(f"{field} updated!")
                    else:
                        print("Field cannot be empty.")
            
            elif option == '2':  # Add new field
                print("\nADD NEW FIELD")
                new_key = input("New field name: ").strip()
                if new_key:
                    if new_key in world:
                        print(f"'{new_key}' already exists. Use 'Edit existing field' instead.")
                    else:
                        value_type = input("Value type: (s)tring or (l)ist? [s/l]: ").strip().lower()
                        if value_type == 's':
                            value = input(f"Value for {new_key}: ").strip()
                            world[new_key] = value
                        elif value_type == 'l':
                            world[new_key] = []
                            print(f"Created empty list for {new_key}. Use 'Add to list' to populate.")
                        else:
                            print("Invalid type. Field not created.")
                else:
                    print("Field name cannot be empty.")
            
            elif option == '3':  # Add to list
                print("\nADD TO LIST")
                list_fields = [k for k, v in world.items() if isinstance(v, list)]
                if not list_fields:
                    print("No list fields found. Create one with 'Add new field' first.")
                    continue
                
                print("Available lists:", ", ".join(list_fields))
                field = input("List to add to: ").strip()
                
                if field in list_fields:
                    new_item = input("Item to add: ").strip()
                    if new_item:
                        world[field].append(new_item)
                        print(f"Added to {field}. Total items: {len(world[field])}")
                    else:
                        print("Item cannot be empty.")
                else:
                    print(f"'{field}' is not a list field.")
            
            elif option == '4':  # Remove from list
                print("\nREMOVE FROM LIST")
                list_fields = [k for k, v in world.items() if isinstance(v, list) and v]
                if not list_fields:
                    print("No populated lists found.")
                    continue
                
                print("Available lists:", ", ".join(list_fields))
                field = input("List to remove from: ").strip()
                
                if field in list_fields and world[field]:
                    print(f"\nItems in {field}:")
                    for i, item in enumerate(world[field], 1):
                        print(f"{i}. {item}")
                    
                    try:
                        item_num = int(input("Item number to remove: ")) - 1
                        if 0 <= item_num < len(world[field]):
                            removed = world[field].pop(item_num)
                            print(f"Removed: {removed}")
                        else:
                            print("Invalid number.")
                    except ValueError:
                        print("Please enter a number.")
                else:
                    print(f"'{field}' is empty or not a list.")
            
            elif option == '5':  # Remove field
                print("\nREMOVE FIELD")
                removable = [k for k in world.keys() if k not in ['Name']]  # Don't remove Name
                print("Removable fields:", ", ".join(removable))
                
                field = input("Field to remove: ").strip()
                if field in removable:
                    confirm = input(f"Remove '{field}'? This cannot be undone. (yes/no): ").strip().lower()
                    if confirm.startswith('y'):
                        del world[field]
                        print(f"Removed {field}")
                else:
                    print(f"Cannot remove '{field}' or field not found.")
            
            elif option == '6':  # Finish
                break
            
            else:
                print("Invalid option. Choose 1-6.")
            
            # Update keys list for next iteration
            keys = list(world.keys())
        
        # 4. SAVE CHANGES
        save_worlds(worlds)
        print(f"\n World '{original_name}' updated successfully!")
        print_world_details(world)

print("Sometimes we dream up whole worlds.")
print("And sometimes we forget them because we never thought to write them down.")
print("So let's carve out a space for all the worlds that could have been, that are and that will be.")
print("Type 'add', 'view all', 'view one', 'edit' or 'quit'.")
print("Pretty easy to start don't you think?\n")

while option := input("What would you like to do? ('add'/'view all'/'view one'/'edit/'quit'): ").strip().lower():
    match option:
        case 'add':
            add_world()
        case 'view all':
            view_worlds()
        case 'view one':
            view_single_world()
        case 'edit':
            edit_world()
        case 'quit':
            print("I'll see you again when you dream up the next one.")
            print("Don't take too long.")
            break