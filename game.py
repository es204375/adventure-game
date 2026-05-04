import gamefunctions as gf

def main():
    # start with title animation!
    gf.print_title_animation()
    
    # defining items
    sword_item = {
        "name": "Iron Sword", 
        "type": "weapon", 
        "price": 50, 
        "damage_boost": 60, 
        "maxDurability": 10, 
        "currentDurability": 10, 
        "equipped": False
    }

    bait_item = {
        "name": "Monster Bait", 
        "type": "consumable", 
        "price": 30
    }

    print("1) New Game\n2) Load Game")
    start_choice = gf.get_valid_input("> ", ["1", "2"])
    
    state = gf.load_game() if start_choice == "2" else None
    if state is None:
        state = gf.initialize_game(input("What is your name? "))
    
    while state["player_hp"] > 0:
        print(f"\nLocation: Town | HP: {state['player_hp']} | Gold: {state['player_gold']}")
        choice = gf.get_valid_input("1) Explore\n2) Sleep\n3) Shop\n4) Inventory\n5) Save\n6) Quit\n> ", ["1", "2", "3", "4", "5", "6"])

        if choice == "1":
            result = gf.run_map_interface(state)
            if result == "dead": break

        elif choice == "2":
            state["player_hp"], state["player_gold"] = gf.sleep(state["player_hp"], state["player_gold"])

        elif choice == "3":
            gf.print_shop_menu(sword_item["name"], sword_item["price"], bait_item["name"], bait_item["price"])
            
            shop_choice = gf.get_valid_input("What would you like to buy? (1, 2, or 3 to leave): ", ["1", "2", "3"])
            if shop_choice == "1":
                gf.purchase_item(sword_item, state)
            elif shop_choice == "2":
                gf.purchase_item(bait_item, state)
            else:
                print("Leaving shop.")

        elif choice == "4":
            gf.equip_item(state, "weapon")

        elif choice == "5":
            gf.save_game(state)
            
        elif choice == "6":
            break

    if state["player_hp"] <= 0:
        print("\nYour journey has ended. Game Over.")

if __name__ == "__main__":
    main()
