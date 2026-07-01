DROP TABLE IF EXISTS Maintenance;
DROP TABLE IF EXISTS Payment;
DROP TABLE IF EXISTS Rental;
DROP TABLE IF EXISTS Vehicle;
DROP TABLE IF EXISTS Staff;
DROP TABLE IF EXISTS Customer;

CREATE TABLE Customer (
    customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    phone TEXT,
    email TEXT UNIQUE,
    drivers_license TEXT UNIQUE NOT NULL
);

CREATE TABLE Staff (
    staff_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    phone TEXT,
    email TEXT UNIQUE,
    role TEXT NOT NULL
);

CREATE TABLE Vehicle (
    vehicle_id INTEGER PRIMARY KEY AUTOINCREMENT,
    make TEXT NOT NULL,
    model TEXT NOT NULL,
    year INTEGER NOT NULL,
    license_plate TEXT UNIQUE NOT NULL,
    daily_rate REAL NOT NULL,
    status TEXT NOT NULL DEFAULT 'Available'
);

CREATE TABLE Rental (
    rental_id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_id INTEGER NOT NULL,
    vehicle_id INTEGER NOT NULL,
    staff_id INTEGER NOT NULL,
    start_date TEXT NOT NULL,
    end_date TEXT NOT NULL,
    return_date TEXT,
    status TEXT NOT NULL DEFAULT 'Active',
    FOREIGN KEY (customer_id) REFERENCES Customer(customer_id),
    FOREIGN KEY (vehicle_id) REFERENCES Vehicle(vehicle_id),
    FOREIGN KEY (staff_id) REFERENCES Staff(staff_id)
);

CREATE TABLE Payment (
    payment_id INTEGER PRIMARY KEY AUTOINCREMENT,
    rental_id INTEGER NOT NULL,
    amount REAL NOT NULL,
    payment_date TEXT NOT NULL,
    payment_method TEXT NOT NULL,
    FOREIGN KEY (rental_id) REFERENCES Rental(rental_id)
);

CREATE TABLE Maintenance (
    maintenance_id INTEGER PRIMARY KEY AUTOINCREMENT,
    vehicle_id INTEGER NOT NULL,
    maintenance_date TEXT NOT NULL,
    description TEXT NOT NULL,
    cost REAL NOT NULL,
    status TEXT NOT NULL,
    FOREIGN KEY (vehicle_id) REFERENCES Vehicle(vehicle_id)
);


INSERT INTO Customer (first_name, last_name, phone, email, drivers_license)
VALUES
('Ali', 'Mansour', '513-111-2222', 'ali@example.com', 'DL1001'),
('Sarah', 'Smith', '513-333-4444', 'sarah@example.com', 'DL1002'),
('Omar', 'Khan', '513-555-6666', 'omar@example.com', 'DL1003'),
('Lina', 'Johnson', '513-777-1234', 'lina@example.com', 'DL1004'),
('David', 'Miller', '513-222-7890', 'david@example.com', 'DL1005'),
('Nora', 'Ahmed', '513-888-4321', 'nora@example.com', 'DL1006'),
('James', 'Wilson', '513-444-9999', 'james@example.com', 'DL1007'),
('Mariam', 'Hassan', '513-666-1010', 'mariam@example.com', 'DL1008');

INSERT INTO Staff (first_name, last_name, phone, email, role)
VALUES
('Hamzah', 'Jodeh', '513-777-8888', 'hamzah@example.com', 'Manager'),
('Maya', 'Brown', '513-999-0000', 'maya@example.com', 'Rental Agent'),
('Adam', 'Clark', '513-123-9876', 'adam@example.com', 'Rental Agent'),
('Sophia', 'Davis', '513-321-6540', 'sophia@example.com', 'Maintenance Coordinator');

INSERT INTO Vehicle (make, model, year, license_plate, daily_rate, status)
VALUES
('Toyota', 'Corolla', 2022, 'ABC123', 45.00, 'Available'),
('Honda', 'Civic', 2021, 'XYZ789', 50.00, 'Rented'),
('Hyundai', 'Tucson', 2023, 'HYB456', 65.00, 'Rented'),
('Kia', 'Niro', 2023, 'KIA321', 60.00, 'Maintenance'),
('Nissan', 'Altima', 2020, 'NIS555', 55.00, 'Available'),
('Ford', 'Escape', 2022, 'FOR222', 58.00, 'Available'),
('Chevrolet', 'Malibu', 2021, 'CHE789', 52.00, 'Available'),
('Toyota', 'Camry', 2023, 'CAM888', 62.00, 'Rented'),
('Jeep', 'Compass', 2022, 'JEP456', 70.00, 'Available'),
('Honda', 'CR-V', 2024, 'CRV202', 75.00, 'Maintenance');

INSERT INTO Rental (customer_id, vehicle_id, staff_id, start_date, end_date, return_date, status)
VALUES
(1, 1, 1, '2026-07-01', '2026-07-05', '2026-07-05', 'Returned'),
(2, 2, 2, '2026-07-10', '2026-07-15', NULL, 'Active'),
(3, 3, 1, '2026-07-12', '2026-07-16', NULL, 'Active'),
(4, 5, 3, '2026-07-03', '2026-07-06', '2026-07-06', 'Returned'),
(5, 6, 2, '2026-07-08', '2026-07-11', '2026-07-11', 'Returned'),
(6, 8, 3, '2026-07-14', '2026-07-20', NULL, 'Active'),
(7, 7, 1, '2026-07-02', '2026-07-04', '2026-07-04', 'Returned');

INSERT INTO Payment (rental_id, amount, payment_date, payment_method)
VALUES
(1, 225.00, '2026-07-01', 'Credit Card'),
(2, 250.00, '2026-07-10', 'Debit Card'),
(3, 260.00, '2026-07-12', 'Cash'),
(4, 165.00, '2026-07-03', 'Credit Card'),
(5, 174.00, '2026-07-08', 'Debit Card'),
(6, 372.00, '2026-07-14', 'Credit Card'),
(7, 104.00, '2026-07-02', 'Cash'),
(1, 25.00, '2026-07-05', 'Cash');

INSERT INTO Maintenance (vehicle_id, maintenance_date, description, cost, status)
VALUES
(4, '2026-07-03', 'Oil change and tire check', 120.00, 'Completed'),
(3, '2026-07-12', 'Brake inspection', 90.00, 'Scheduled'),
(10, '2026-07-15', 'Engine diagnostic check', 150.00, 'Scheduled'),
(9, '2026-07-09', 'Tire replacement', 400.00, 'Completed'),
(2, '2026-06-28', 'Interior cleaning and inspection', 75.00, 'Completed'),
(6, '2026-07-06', 'Battery replacement', 180.00, 'Completed');
