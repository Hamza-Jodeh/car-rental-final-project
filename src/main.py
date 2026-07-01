from database import initialize_database, get_connection


def view_available_vehicles():
    """
    Displays all vehicles with status Available.
    """
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT vehicle_id, make, model, year, license_plate, daily_rate, status
        FROM Vehicle
        WHERE status = 'Available'
        ORDER BY vehicle_id
    """)

    vehicles = cursor.fetchall()

    print("\nAvailable Vehicles")
    print("------------------------------------")

    if len(vehicles) == 0:
        print("No vehicles are currently available.")
    else:
        for vehicle in vehicles:
            print(
                f"ID: {vehicle['vehicle_id']} | "
                f"{vehicle['year']} {vehicle['make']} {vehicle['model']} | "
                f"Plate: {vehicle['license_plate']} | "
                f"Rate: ${vehicle['daily_rate']:.2f}/day | "
                f"Status: {vehicle['status']}"
            )

    connection.close()


def search_vehicles():
    """
    Searches vehicles by make or model.
    """
    search_term = input("Enter vehicle make or model to search: ")

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT vehicle_id, make, model, year, license_plate, daily_rate, status
        FROM Vehicle
        WHERE make LIKE ? OR model LIKE ?
        ORDER BY vehicle_id
    """, (f"%{search_term}%", f"%{search_term}%"))

    vehicles = cursor.fetchall()

    print("\nSearch Results")
    print("------------------------------------")

    if len(vehicles) == 0:
        print("No vehicles matched your search.")
    else:
        for vehicle in vehicles:
            print(
                f"ID: {vehicle['vehicle_id']} | "
                f"{vehicle['year']} {vehicle['make']} {vehicle['model']} | "
                f"Plate: {vehicle['license_plate']} | "
                f"Rate: ${vehicle['daily_rate']:.2f}/day | "
                f"Status: {vehicle['status']}"
            )

    connection.close()


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

        elif choice == "2":
            view_available_vehicles()

        elif choice == "3":
            search_vehicles()

        elif choice == "0":
            print("Goodbye.")
            break

        else:
            print("This feature will be added soon.")


if __name__ == "__main__":
    main()