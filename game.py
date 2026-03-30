import gamefunctions as gf

def main():
    """
    The main driver for the game. Manages the high-level state 
    and the primary game loop.
    """
    hp = 30
    gold = 10
    
    hero_name = str(input("What is your name, brave hero? "))
    gf.print_welcome(hero_name, 20)

    # stay in town as long as you aren't passed out
    while hp > 0:
        print(f"\nYou are in town.")
        print(f"Current HP: {hp}, Current Gold: {gold}")
        print("What would you like to do?")
        print("1) Leave town (Fight Monster)")
        print("2) Sleep (Restore HP for 5 Gold)")
        print("3) Quit")

        # make sure input is correct
        choice = gf.get_valid_input("> ", ["1", "2", "3"])

        if choice == "1":
            # enter the combat logic
            hp, gold = gf.fight_monster(hp, gold)
        elif choice == "2":
            # attempt to heal
            hp, gold = gf.sleep(hp, gold)
        elif choice == "3":
            print("Goodbye, traveler!")
            break

    # check if the loop ended because of health
    if hp <= 0:
        print("\nYour character has passed out. Game Over.")

if __name__ == "__main__":
    main()
