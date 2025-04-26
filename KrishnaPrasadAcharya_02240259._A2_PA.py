# ========================
# Pokemon Binder Manager Data
# ========================
MAX_POKEDEX = 1025
CARDS_PER_PAGE = 64
CARDS_PER_ROW = 8
binder = {}

# ========================
# Helper Functions
# ========================
def calculate_position(pokedex_number):
    index = pokedex_number - 1
    page = index // CARDS_PER_PAGE + 1
    index_on_page = index % CARDS_PER_PAGE
    row = index_on_page // CARDS_PER_ROW + 1
    col = index_on_page % CARDS_PER_ROW + 1
    return page, row, col

# ========================
# Part B - Pokemon Card Binder Manager
# ========================
def pokemon_card_binder_manager():
    while True:
        print("\n--- Pokemon Card Binder Manager ---")
        print("1. Add Pokemon card")
        print("2. Reset binder")
        print("3. View current placements")
        print("4. Exit to main menu")
        choice = input("Select option: ")
        if choice == "1":
            try:
                num = int(input("Enter Pokedex number (1-1025): "))
                if not 1 <= num <= MAX_POKEDEX:
                    print("Invalid Pokedex number.")
                    continue
                if num in binder:
                    print("Card already exists in binder.")
                    page, row, col = binder[num]
                    print(f"Page: {page}, Row: {row}, Column: {col}, Status: Already exists")
                else:
                    page, row, col = calculate_position(num)
                    binder[num] = (page, row, col)
                    print(f"Page: {page}, Row: {row}, Column: {col}, Status: Added")
                    if len(binder) == MAX_POKEDEX:
                        print("You have caught them all!!")
            except ValueError:
                print("Please enter a valid number.")
        elif choice == "2":
            confirm = input("Type 'CONFIRM' to reset or 'EXIT' to cancel: ")
            if confirm == "CONFIRM":
                binder.clear()
                print("The binder reset was successful!")
            else:
                print("Reset cancelled.")
        elif choice == "3":
            if not binder:
                print("The binder is empty.")
            else:
                print("Current Binder Contents:")
                for num in sorted(binder):
                    page, row, col = binder[num]
                    print(f"Pokedex #{num}: Page {page}, Row {row}, Column {col}")
                total = len(binder)
                percent = (total / MAX_POKEDEX) * 100
                print(f"Total cards: {total}, Completion: {percent:.1f}%")
        elif choice == "4":
            print("Returning to main menu...")
            break
        else:
            print("Invalid option.")

def main():
    pokemon_card_binder_manager()

if __name__ == "__main__":
    main()
