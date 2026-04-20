import gamefunctions as gf
import random

def main():
    print("1) New Game\n2) Load Game")
    start_choice = gf.get_valid_input("> ", ["1", "2"])
    
    state = gf.load_game() if start_choice == "2" else None
    if state is None:
        state = gf.initialize_game(input("What is your name, brave hero? "))
    
    gf.print_welcome(state["player_name"], 20)

    while state["player_hp"] > 0:
        print(f"\nTown | HP: {state['player_hp']} | Gold: {state['player_gold']}")
        print("1) Explore (Open Map)\n2) Sleep (5 Gold)\n3) Save\n4) Quit")
        choice = gf.get_valid_input("> ", ["1", "2", "3", "4"])

        if choice == "1":
            # map Loop
            while True:
                map_result = gf.run_map_interface(state)
                
                if map_result == "monster":
                    gf.fight_monster(state)
                    # after fight, move monster to a new random spot
                    state["map_state"]["monster_pos"] = [random.randint(0,9), random.randint(0,9)]
                    # make sure the monster doesn't land on town
                    if state["map_state"]["monster_pos"] == state["map_state"]["town_pos"]:
                        state["map_state"]["monster_pos"] = [5, 5]
                    
                    if state["player_hp"] <= 0: break # exit map if dead
                else:
                    break # back to town menu

        elif choice == "2":
            state["player_hp"], state["player_gold"] = gf.sleep(state["player_hp"], state["player_gold"])
        elif choice == "3":
            gf.save_game(state)
        elif choice == "4":
            break

    if state["player_hp"] <= 0:
        print("\nGame Over.")

if __name__ == "__main__":
    main()
