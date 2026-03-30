import gamefunctions

def main():
    player_name = input("Enter your character's name: ")
    print("\n--- Game Start ---")
    gamefunctions.print_welcome(player_name, width=24)
    
    print("\nYou venture into the dark forest...")
    monster = gamefunctions.new_random_monster()
    print(f"A wild {monster['name']} appears!")
    print(f"Description: {monster['description']}")
    print(f"Stats: HP {monster['health']}, Power {monster['power']}")

    print("\nYou find a mysterious traveling merchant.")
    shop_error = gamefunctions.print_shop_menu("Health Pot", 15.00, "Iron Sword", 45.50)
    
    if isinstance(shop_error, str):
        print(f"Merchant Error: {shop_error}")

    player_gold = 100.00
    item_cost = 15.00
    quantity_desired = 3
    
    print(f"\nYou have ${player_gold:.2f}. You try to buy {quantity_desired} Health Pots.")
    
    bought, remaining_gold = gamefunctions.purchase_item(item_cost, player_gold, quantity_desired)
    
    print(f"Transaction complete!")
    print(f"Items bought: {bought}")
    print(f"Gold remaining: ${remaining_gold:.2f}")

if __name__ == "__main__":
    main()
