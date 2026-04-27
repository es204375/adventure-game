import gamefunctions as gf

def main():
    print("1) New Game\n2) Load Game")
    start_choice = gf.get_valid_input("> ", ["1", "2"])
    
    state = gf.load_game() if start_choice == "2" else None
    if state is None:
        state = gf.initialize_game(input("What is your name? "))
    
    while state["player_hp"] > 0:
        print(f"\nLocation: Town | HP: {state['player_hp']} | Gold: {state['player_gold']}")
        choice = gf.get_valid_input("1) Explore\n2) Sleep\n3) Save\n4) Quit\n> ", ["1", "2", "3", "4"])

        if choice == "1":
            result = gf.run_map_interface(state)
            if result == "dead": break
        elif choice == "2":
            state["player_hp"], state["player_gold"] = gf.sleep(state["player_hp"], state["player_gold"])
        elif choice == "3":
            gf.save_game(state)
        elif choice == "4":
            break

    if state["player_hp"] <= 0:
        print("\nYour journey has ended. Game Over.")

if __name__ == "__main__":
    main()
