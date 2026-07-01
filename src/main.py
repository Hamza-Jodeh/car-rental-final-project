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


def add_customer():
    """
    Adds a new customer to the database.
    """
    print("\nAdd New Customer")
    print("------------------------------------")

    first_name = input("First name: ")
    last_name = input("Last name: ")
    phone = input("Phone number: ")
    email = input("Email address: ")
    drivers_license = input("Driver's license number: ")

    connection = get_connection()
    cursor = connection.cursor()

    try:
        cursor.execute("""
            INSERT INTO Customer (first_name, last_name, phone, email, drivers_license)
            VALUES (?, ?, ?, ?, ?)
        """, (first_name, last_name, phone, email, drivers_license))

        connection.commit()
        print("Customer added successfully.")

    except Exception as error:
        print("Error adding customer:", error)

    finally:
        connection.close()


def add_vehicle():
    """
    Adds a new vehicle to the database.
    """
    print("\nAdd New Vehicle")
    print("------------------------------------")

    make = input("Make: ")
    model = input("Model: ")

    try:
        year = int(input("Year: "))
        daily_rate = float(input("Daily rental rate: "))
    except ValueError:
        print("Invalid number. Year must be a whole number and daily rate must be a number.")
        return

    license_plate = input("License plate number: ")
    status = "Available"

    connection = get_connection()
    cursor = connection.cursor()

    try:
        cursor.execute("""
            INSERT INTO Vehicle (make, model, year, license_plate, daily_rate, status)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (make, model, year, license_plate, daily_rate, status))

        connection.commit()
        print("Vehicle added successfully.")

    except Exception as error:
        print("Error adding vehicle:", error)

    finally:
        connection.close()


def rent_vehicle():
    """
    Creates a rental record and marks the vehicle as Rented.
    """
    print("\nRent Vehicle")
    print("------------------------------------")

    try:
        customer_id = int(input("Customer ID: "))
        vehicle_id = int(input("Vehicle ID: "))
        staff_id = int(input("Staff ID: "))
    except ValueError:
        print("Invalid ID. Customer ID, Vehicle ID, and Staff ID must be numbers.")
        return

    start_date = input("Start date YYYY-MM-DD: ")
    end_date = input("End date YYYY-MM-DD: ")

    connection = get_connection()
    cursor = connection.cursor()

    try:
        cursor.execute("SELECT * FROM Customer WHERE customer_id = ?", (customer_id,))
        customer = cursor.fetchone()

        if customer is None:
            print("Customer not found.")
            return

        cursor.execute("SELECT * FROM Staff WHERE staff_id = ?", (staff_id,))
        staff = cursor.fetchone()

        if staff is None:
            print("Staff member not found.")
            return

        cursor.execute("SELECT * FROM Vehicle WHERE vehicle_id = ?", (vehicle_id,))
        vehicle = cursor.fetchone()

        if vehicle is None:
            print("Vehicle not found.")
            return

        if vehicle["status"] != "Available":
            print("Vehicle is not available for rent.")
            return

        cursor.execute("""
            INSERT INTO Rental (customer_id, vehicle_id, staff_id, start_date, end_date, return_date, status)
            VALUES (?, ?, ?, ?, ?, NULL, 'Active')
        """, (customer_id, vehicle_id, staff_id, start_date, end_date))

        cursor.execute("""
            UPDATE Vehicle
            SET status = 'Rented'
            WHERE vehicle_id = ?
        """, (vehicle_id,))

        connection.commit()
        print("Vehicle rented successfully.")

    except Exception as error:
        print("Error renting vehicle:", error)

    finally:
        connection.close()


def return_vehicle():
    """
    Returns an active rental and marks the vehicle as Available.
    """
    print("\nReturn Vehicle")
    print("------------------------------------")

    try:
        rental_id = int(input("Rental ID: "))
    except ValueError:
        print("Invalid rental ID. Rental ID must be a number.")
        return

    return_date = input("Return date YYYY-MM-DD: ")

    connection = get_connection()
    cursor = connection.cursor()

    try:
        cursor.execute("""
            SELECT rental_id, vehicle_id, status
            FROM Rental
            WHERE rental_id = ?
        """, (rental_id,))

        rental = cursor.fetchone()

        if rental is None:
            print("Rental not found.")
            return

        if rental["status"] != "Active":
            print("This rental is not active or has already been returned.")
            return

        vehicle_id = rental["vehicle_id"]

        cursor.execute("""
            UPDATE Rental
            SET return_date = ?, status = 'Returned'
            WHERE rental_id = ?
        """, (return_date, rental_id))

        cursor.execute("""
            UPDATE Vehicle
            SET status = 'Available'
            WHERE vehicle_id = ?
        """, (vehicle_id,))

        connection.commit()
        print("Vehicle returned successfully.")

    except Exception as error:
        print("Error returning vehicle:", error)

    finally:
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

        elif choice == "4":
            add_customer()

        elif choice == "5":
            add_vehicle()

        elif choice == "6":
            rent_vehicle()

        elif choice == "7":
            return_vehicle()

        elif choice == "0":
            print("Goodbye.")
            break

        else:
            print("This feature will be added soon.")


if __name__ == "__main__":
    main()