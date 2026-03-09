# gamefunctions.py
# Elizabeth Sweeney
# 3/1/26
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

import random

def purchase_item(itemPrice, startingMoney, quantityToPurchase=1):
    money = startingMoney
    num_purchased = 0
    # loop continues while money is left and more are required to be purchased
    while (money >= itemPrice) and (quantityToPurchase > 0):
        money -= itemPrice # cost is subtracted and quantity is ticked down while the number bought ticks up
        quantityToPurchase -= 1
        num_purchased += 1
    leftover_money = startingMoney - (itemPrice * num_purchased)
    return num_purchased, leftover_money

def new_random_monster():
    # some random variety within stat levels
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
    # formatting greeting
    width = int(width)
    greeting = f"Hello, {name}!"
    print(f"{greeting:^{width}}")


def print_shop_menu(item1Name, item1Price, item2Name, item2Price):
    item1Price = f"${item1Price:.2f}"
    item2Price = f"${item2Price:.2f}"
    # ensure menu will fit in width specifications
    if (len(item1Name) > 12) or (len(item1Price) > 8) or (len(item2Name) > 12) or (len(item2Price) > 8):
        return "An item name is longer than 12 or a price is longer than 8."
    print("/----------------------\\")
    print(f"| {item1Name:<12}{item1Price:>8} |")
    print(f"| {item2Name:<12}{item2Price:>8} |")
    print("\\----------------------/")


# function tests
if __name__ == "__main__":
    """ Purchase item function """
    num_purchased, leftover_money = purchase_item(123, 1000, 3)
    print(num_purchased)
    print(leftover_money)

    num_purchased, leftover_money = purchase_item(123, 201, 3)
    print(num_purchased)
    print(leftover_money)

    num_purchased, leftover_money = purchase_item(3141, 2112)
    print(num_purchased)
    print(leftover_money)

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


