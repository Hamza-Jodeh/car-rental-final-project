from database import initialize_database


def show_menu():
    """
    Displays the main menu for the car rental system.
    """
    print("\n====================================")
    print(" Car Rental Management System")
    print("====================================")
    print("1. Initialize database")
    print("2. View available vehicles")
    print("3. Search vehicles")
    print("4. Add customer")
    print("5. Add vehicle")
    print("6. Rent vehicle")
    print("7. Return vehicle")
    print("8. View rental history")
    print("9. View payments")
    print("10. Add maintenance record")
    print("0. Exit")


def main():
    """
    Runs the main command-line application.
    """
    while True:
        show_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            initialize_database()

        elif choice == "0":
            print("Goodbye.")
            break

        else:
            print("This feature will be added soon.")


if __name__ == "__main__":
    main()
