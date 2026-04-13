# gamefunctions.py
# Elizabeth Sweeney
# 4/12/26
# This program implements the two following functions:
# The first, purchase_item(), takes the cost of an item and the starting
# amount of money, and optionally the quantity to buy (default is 1). It
# returns the number of items purchased and the money leftover after.
# The second, new_random_monster(), picks a random monster from a
# list of three monsters with the name, description, health, money,
# and power level (with some variation) for each monster in a dictionary.
# The third, print_welcome(), prints a welcome message centered in a given width.
# The fourth, print_shop_menu(), prints an aligned menu with specified 
# items and prices.
# Part of a larger project.

"""A module for managing RPG game mechanics.

This module provides functions designed to handle common tasks in a text-based 
role-playing game. It includes logic for purchasing items with budget constraints, 
generating randomized monster encounters, and printing formatted menus and 
greetings to the console.

Typical usage example:

  monster = new_random_monster()
  print_welcome(monster["name"], width=30)
  items_bought, change = purchase_item(10.50, 50.00, quantityToPurchase=3)"""

import random
import os
import json

def new_random_monster():
    """
    Generates a dictionary representing a random monster with randomized stats.

    Returns:
        dict: A dictionary containing 'name', 'description', 'health', 'power', and 'money'.

    Example:
        >>> monster = new_random_monster()
        >>> print(monster['name'])
        'Goblin'
    """
    monster1 = {
    "name": "Goblin",
    "description": "A short, green, and scowling creature.",
    "health": random.randint(80, 100),
    "power": random.randint(30, 40),
    "money": random.randint(65, 85)
    }
    monster2 = {
    "name": "Ghost",
    "description": "A howling, transparent remnant of death.",
    "health": random.randint(15, 30),
    "power": random.randint(10, 20),
    "money": random.randint(0, 20)
    }
    monster3 = {
    "name": "Troll",
    "description": "A hulking, enraged beast.",
    "health": random.randint(150, 300),
    "power": random.randint(80, 100),
    "money": random.randint(100, 150)
    }
    # picks a random monster
    monsters = [monster1, monster2, monster3]
    random_monster = random.choice(monsters)
    return random_monster

def print_welcome(name, width=20):
    """
    Prints a centered greeting message within a specified width.

    Parameters:
        name (str): The name of the player to greet.
        width (int): The total width of the formatted string.

    Returns:
        None

    Example:
        >>> print_welcome("Hero", 14)
         Hello, Hero! 
    """
    width = int(width)
    greeting = f"Hello, {name}!"
    print(f"{greeting:^{width}}")


def print_shop_menu(item1Name, item1Price, item2Name, item2Price):
    r"""
    Displays a formatted shop menu with two items and their prices.

    Parameters:
        item1Name (str): The name of the first item.
        item1Price (float): The price of the first item.
        item2Name (str): The name of the second item.
        item2Price (float): The price of the second item.

    Returns:
        None or str: Returns an error message if inputs exceed formatting limits.

    Example:
        >>> print_shop_menu("Sword", 50, "Shield", 35)
        /----------------------\
        | Sword          $50.00 |
        | Shield         $35.00 |
        \----------------------/
    """
    item1Price = f"${item1Price:.2f}"
    item2Price = f"${item2Price:.2f}"
    # ensure menu will fit in width specifications
    if (len(item1Name) > 12) or (len(item1Price) > 8) or (len(item2Name) > 12) or (len(item2Price) > 8):
        return "An item name is longer than 12 or a price is longer than 8."
    print("/----------------------\\")
    print(f"| {item1Name:<12}{item1Price:>8} |")
    print(f"| {item2Name:<12}{item2Price:>8} |")
    print("\\----------------------/")

def get_valid_input(prompt, options):
    """
    Prompts the user for input until they provide a valid choice.

    Parameters:
        prompt (str): The text displayed to the user.
        options (list): A list of strings representing valid inputs.

    Returns:
        str: The valid input selected by the user.

    Example:
        >>> get_valid_input("Pick 1 or 2: ", ["1", "2"])
        '1'
    """
    while True:
        choice = input(prompt)
        if choice in options:
            return choice
        print(f"Invalid choice. Please enter one of: {', '.join(options)}")

def sleep(hp, gold):
    """
    Restores player HP to maximum for a cost of 5 gold.

    Parameters:
        hp (int): The player's current health points.
        gold (int): The player's current gold balance.

    Returns:
        tuple: A tuple containing the updated (hp, gold).

    Example:
        >>> sleep(10, 20)
        (30, 15)
    """
    if gold >= 5:
        print("\nYou feel refreshed! (HP restored to 30)")
        return 30, gold - 5
    else:
        print("\nYou don't have enough gold to sleep!")
        return hp, gold

def fight_monster(hp, gold):
    """
    Executes a combat loop between the player and a random monster.

    Parameters:
        hp (int): The player's current health points.
        gold (int): The player's current gold balance.

    Returns:
        tuple: A tuple containing the updated (hp, gold) after the fight.

    Example:
        >>> fight_monster(30, 10)
        (20, 85)
    """
    monster = new_random_monster()
    print(f"\nA wild {monster['name']} appears! {monster['description']}")
    
    m_hp = monster['health']
    player_damage = 25 

    while hp > 0 and m_hp > 0:
        print(f"\n{monster['name']} HP: {m_hp} | Your HP: {hp}")
        choice = get_valid_input("1) Fight\n2) Run\n> ", ["1", "2"])

        if choice == "1":
            m_hp -= player_damage
            hp -= monster['power']
            print(f"You hit for {player_damage}! The monster hits you for {monster['power']}!")
        else:
            print("You escaped back to town!")
            return hp, gold

    if hp <= 0:
        print("\nYou have been defeated...")
        hp = 0 
    else:
        print(f"\nYou defeated the {monster['name']} and found {monster['money']} gold!")
        gold += monster['money']
    
    return hp, gold

def initialize_game(player_name):
    """
    Initializes the game state dictionary with starting stats and inventory.

    Parameters:
        player_name (str): The name of the player.

    Returns:
        dict: A dictionary containing player_name, player_hp, player_gold, and player_inventory.

    Example:
        >>> state = initialize_game("Jeff")
        >>> print(state["player_gold"])
        500
    """
    return {
        "player_name": player_name,
        "player_hp": 30,
        "player_gold": 500,
        "player_inventory": []
    }

def purchase_item(item_template, state):
    """
    Handles buying an item and updating the game state.

    Parameters:
        item_template (dict): A dictionary containing the item's stats and price.
        state (dict): The current game state dictionary.

    Returns:
        bool: True if the purchase was successful, False otherwise.

    Example:
        >>> purchase_item({"name": "Sword", "price": 50}, state)
        True
    """
    price = item_template["price"]
    if state["player_gold"] >= price:
        state["player_gold"] -= price
        new_item = item_template.copy()
        new_item.pop("price")
        state["player_inventory"].append(new_item)
        print(f"Purchased {new_item['name']}!")
        return True
    else:
        print("Not enough gold!")
        return False

def equip_item(state, item_type):
    """
    Displays a filtered list of items and allows the user to equip one.

    Parameters:
        state (dict): The current game state dictionary.
        item_type (str): The category of item to filter by (e.g., 'weapon').

    Returns:
        None

    Example:
        >>> equip_item(state, "weapon")
        0) None/Unequip
        1) Iron Sword (Equipped)
    """
    options = [item for item in state["player_inventory"] if item["type"] == item_type]
    
    if not options:
        print(f"You have no {item_type}s to equip.")
        return

    print(f"\n--- Select a {item_type} to equip ---")
    valid_indices = ["0"]
    print("0) None/Unequip")
    
    for i, item in enumerate(options, 1):
        status = "(Equipped)" if item.get("equipped") else ""
        print(f"{i}) {item['name']} {status}")
        valid_indices.append(str(i))

    choice = int(get_valid_input("> ", valid_indices))

    for item in state["player_inventory"]:
        if item["type"] == item_type:
            item["equipped"] = False

    if choice > 0:
        options[choice - 1]["equipped"] = True
        print(f"Equipped {options[choice - 1]['name']}.")

def fight_monster(state):
    """
    Combat logic, including durability loss and consumable item usage.

    Parameters:
        state (dict): The current game state dictionary.

    Returns:
        None

    Example:
        >>> fight_monster(state)
        A wild Goblin appears!
        Use 'Monster Bait' to skip fight? (y/n): 
    """
    monster = new_random_monster()
    print(f"\nA wild {monster['name']} appears!")

    for i, item in enumerate(state["player_inventory"]):
        if item["type"] == "consumable" and item["name"] == "Monster Bait":
            choice = get_valid_input("Use 'Monster Bait' to skip fight? (y/n): ", ["y", "n"])
            if choice == "y":
                state["player_inventory"].pop(i)
                print(f"The {monster['name']} chased the bait away! You win!")
                state["player_gold"] += monster['money']
                return

    m_hp = monster['health']
    
    while state["player_hp"] > 0 and m_hp > 0:
        base_damage = 5
        equipped_weapon = next((i for i in state["player_inventory"] if i.get("equipped") and i["type"] == "weapon"), None)
        
        current_damage = base_damage
        if equipped_weapon:
            current_damage += equipped_weapon["damage_boost"]

        print(f"\n{monster['name']} HP: {m_hp} | Your HP: {state['player_hp']}")
        choice = get_valid_input("1) Fight\n2) Run\n> ", ["1", "2"])

        if choice == "1":
            m_hp -= current_damage
            state["player_hp"] -= monster['power']
            print(f"You hit for {current_damage}!")
            
            if equipped_weapon:
                equipped_weapon["currentDurability"] -= 1
                if equipped_weapon["currentDurability"] <= 0:
                    print(f"Your {equipped_weapon['name']} broke!")
                    state["player_inventory"].remove(equipped_weapon)
        else:
            print("Escaped!")
            return

    if state["player_hp"] <= 0:
        print("\nYou died.")
    else:
        print(f"Victory! Gained {monster['money']} gold.")
        state["player_gold"] += monster['money']

# savin and loadin
def save_game(state, filename="savegame.json"):
    """
    Saves the state dictionary to a JSON file.
    Parameters:
        state (dict): The current game state dictionary containing player stats and inventory.
        filename (str): The name of the file to create or overwrite.

    Returns:
        None

    Example:
        >>> save_game(state, "hero_save.json")
        Game saved successfully to hero_save.json!
    """
    try:
        with open(filename, 'w') as f:
            json.dump(state, f, indent=4)
        print(f"Game saved successfully to {filename}!")
    except Exception as e:
        print(f"Error saving game: {e}")

def load_game(filename="savegame.json"):
    """
    Reads the JSON file and returns the state dictionary.
    Parameters:
        filename (str): The name of the save file to read.

    Returns:
        dict or None: The restored state dictionary if successful, None otherwise.

    Example:
        >>> loaded_state = load_game("hero_save.json")
        Game loaded successfully!
    """
    if not os.path.exists(filename):
        print("No save file found.")
        return None
    try:
        with open(filename, 'r') as f:
            state = json.load(f)
        print("Game loaded successfully!")
        return state
    except Exception as e:
        print(f"Error loading game: {e}")
        return None


# function tests
if __name__ == "__main__":
    """ Initialize game function """
    # Saving and loading test
    choice = get_valid_input("1) New Game\n2) Load Game\n> ", ["1", "2"])
    
    if choice == "2":
        state = load_game()
        if not state:
            print("Starting new game instead...")
            name = input("Enter your name: ")
            state = initialize_game(name)
    else:
        name = input("Enter your name: ")
        state = initialize_game(name)

    print_welcome(state["player_name"], 30)
    print(f"Inventory Count: {len(test_state['player_inventory'])}")

    """ New purchase item function """
    # Define for testing
    sword_template = {
        "name": "Iron Sword", 
        "type": "weapon", 
        "price": 50, 
        "damage_boost": 20, 
        "maxDurability": 5, 
        "currentDurability": 5, 
        "equipped": False
    }
    bait_template = {
        "name": "Monster Bait", 
        "type": "consumable", 
        "price": 30
    }

    # Test successful purchase
    success = purchase_item(sword_template, test_state)
    print(f"Purchase Sword (Success): {success}")
    print(f"Remaining Gold: {test_state['player_gold']}")
    print(f"First Item in Inventory: {test_state['player_inventory'][0]['name']}")

    # Test purchase with insufficient funds
    poor_state = {"player_gold": 5, "player_inventory": []}
    success_fail = purchase_item(sword_template, poor_state)
    print(f"Purchase expensive item with 5 gold (Success): {success_fail}")   

    """ New random monster function """
    my_monster = new_random_monster()
    print(my_monster['name'])
    print(my_monster['description'])
    print(my_monster['health'])
    print(my_monster['power'])
    print(my_monster['money'])

    my_monster = new_random_monster()
    print(my_monster['name'])
    print(my_monster['description'])
    print(my_monster['health'])
    print(my_monster['power'])
    print(my_monster['money'])

    my_monster = new_random_monster()
    print(my_monster['name'])
    print(my_monster['description'])
    print(my_monster['health'])
    print(my_monster['power'])
    print(my_monster['money'])

    """ Print welcome function """
    print_welcome("Audrey", 30)
    print_welcome("Tom", 40)
    print_welcome("Jane", 11)

    """ Print shop menu function """
    print_shop_menu("Apple", 31, "Pear", 1.234)
    print_shop_menu("Egg", .23, "Bag of Oats", 12.34)
    print_shop_menu("Cheese", 17.48, "Cream", 5)




