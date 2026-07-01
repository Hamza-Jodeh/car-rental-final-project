-- Query 1: Show all available vehicles
SELECT 
    vehicle_id,
    make,
    model,
    year,
    license_plate,
    daily_rate,
    status
FROM Vehicle
WHERE status = 'Available';


-- Query 2: Search vehicles by make or model
-- Example search: Toyota
SELECT 
    vehicle_id,
    make,
    model,
    year,
    license_plate,
    daily_rate,
    status
FROM Vehicle
WHERE make LIKE '%Toyota%' OR model LIKE '%Toyota%';


-- Query 3: Show all active rentals with customer and vehicle information
SELECT 
    Rental.rental_id,
    Customer.first_name || ' ' || Customer.last_name AS customer_name,
    Vehicle.make,
    Vehicle.model,
    Vehicle.license_plate,
    Rental.start_date,
    Rental.end_date,
    Rental.status
FROM Rental
JOIN Customer ON Rental.customer_id = Customer.customer_id
JOIN Vehicle ON Rental.vehicle_id = Vehicle.vehicle_id
WHERE Rental.status = 'Active';


-- Query 4: Show full rental history with customer, vehicle, and staff information
SELECT
    Rental.rental_id,
    Customer.first_name || ' ' || Customer.last_name AS customer_name,
    Vehicle.make || ' ' || Vehicle.model AS vehicle_name,
    Staff.first_name || ' ' || Staff.last_name AS staff_name,
    Rental.start_date,
    Rental.end_date,
    Rental.return_date,
    Rental.status
FROM Rental
JOIN Customer ON Rental.customer_id = Customer.customer_id
JOIN Vehicle ON Rental.vehicle_id = Vehicle.vehicle_id
JOIN Staff ON Rental.staff_id = Staff.staff_id
ORDER BY Rental.rental_id;


-- Query 5: Show payment history with customer and vehicle information
SELECT 
    Payment.payment_id,
    Rental.rental_id,
    Customer.first_name || ' ' || Customer.last_name AS customer_name,
    Vehicle.make || ' ' || Vehicle.model AS vehicle_name,
    Payment.amount,
    Payment.payment_date,
    Payment.payment_method
FROM Payment
JOIN Rental ON Payment.rental_id = Rental.rental_id
JOIN Customer ON Rental.customer_id = Customer.customer_id
JOIN Vehicle ON Rental.vehicle_id = Vehicle.vehicle_id
ORDER BY Payment.payment_id;


-- Query 6: Show vehicles with maintenance records
SELECT 
    Vehicle.vehicle_id,
    Vehicle.make,
    Vehicle.model,
    Vehicle.license_plate,
    Maintenance.maintenance_date,
    Maintenance.description,
    Maintenance.cost,
    Maintenance.status
FROM Maintenance
JOIN Vehicle ON Maintenance.vehicle_id = Vehicle.vehicle_id
ORDER BY Maintenance.maintenance_date;


-- Query 7: Show total payment amount for each rental
SELECT
    Rental.rental_id,
    Customer.first_name || ' ' || Customer.last_name AS customer_name,
    SUM(Payment.amount) AS total_paid
FROM Rental
JOIN Customer ON Rental.customer_id = Customer.customer_id
JOIN Payment ON Rental.rental_id = Payment.rental_id
GROUP BY Rental.rental_id, customer_name
ORDER BY Rental.rental_id;


-- Query 8: Show vehicles with daily rental rate greater than 60
SELECT
    vehicle_id,
    make,
    model,
    year,
    daily_rate,
    status
FROM Vehicle
WHERE daily_rate > 60
ORDER BY daily_rate DESC;
