class Customer:
    """
    Represents a customer in the car rental system.
    """

    def __init__(self, first_name, last_name, phone, email, drivers_license):
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone
        self.email = email
        self.drivers_license = drivers_license

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"


class Staff:
    """
    Represents a staff member who manages rentals.
    """

    def __init__(self, first_name, last_name, phone, email, role):
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone
        self.email = email
        self.role = role

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"


class Vehicle:
    """
    Represents a vehicle in the rental system.
    """

    def __init__(self, make, model, year, license_plate, daily_rate, status="Available"):
        self.make = make
        self.model = model
        self.year = year
        self.license_plate = license_plate
        self.daily_rate = daily_rate
        self.status = status

    def get_vehicle_name(self):
        return f"{self.year} {self.make} {self.model}"

    def is_available(self):
        return self.status == "Available"


class Rental:
    """
    Represents a rental transaction.
    """

    def __init__(self, customer_id, vehicle_id, staff_id, start_date, end_date, status="Active"):
        self.customer_id = customer_id
        self.vehicle_id = vehicle_id
        self.staff_id = staff_id
        self.start_date = start_date
        self.end_date = end_date
        self.status = status


class Payment:
    """
    Represents a payment for a rental.
    """

    def __init__(self, rental_id, amount, payment_date, payment_method):
        self.rental_id = rental_id
        self.amount = amount
        self.payment_date = payment_date
        self.payment_method = payment_method


class Maintenance:
    """
    Represents a vehicle maintenance record.
    """

    def __init__(self, vehicle_id, maintenance_date, description, cost, status):
        self.vehicle_id = vehicle_id
        self.maintenance_date = maintenance_date
        self.description = description
        self.cost = cost
        self.status = status

