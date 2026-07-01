# Relational Schema Design

## Project Title

Car Rental Database and Management System

## Overview

This document converts the car rental system ER design into relational database schemas. Each relation includes attributes, primary keys, and foreign keys.

The database contains six main relations:

1. Customer
2. Staff
3. Vehicle
4. Rental
5. Payment
6. Maintenance

---

## 1. Customer Relation

Customer stores information about each customer who rents vehicles.

### Schema

Customer(
customer_id,
first_name,
last_name,
phone,
email,
drivers_license
)

### Primary Key

customer_id

### Candidate Keys

email
drivers_license

### Attributes

* customer_id: Unique ID for each customer
* first_name: Customer's first name
* last_name: Customer's last name
* phone: Customer's phone number
* email: Customer's email address
* drivers_license: Customer's driver's license number

---

## 2. Staff Relation

Staff stores information about employees who manage rentals and vehicles.

### Schema

Staff(
staff_id,
first_name,
last_name,
phone,
email,
role
)

### Primary Key

staff_id

### Candidate Key

email

### Attributes

* staff_id: Unique ID for each staff member
* first_name: Staff member's first name
* last_name: Staff member's last name
* phone: Staff member's phone number
* email: Staff member's email address
* role: Staff member's job role

---

## 3. Vehicle Relation

Vehicle stores information about cars available in the rental system.

### Schema

Vehicle(
vehicle_id,
make,
model,
year,
license_plate,
daily_rate,
status
)

### Primary Key

vehicle_id

### Candidate Key

license_plate

### Attributes

* vehicle_id: Unique ID for each vehicle
* make: Vehicle manufacturer
* model: Vehicle model
* year: Vehicle year
* license_plate: Vehicle license plate number
* daily_rate: Cost to rent the vehicle per day
* status: Vehicle status such as Available, Rented, or Maintenance

---

## 4. Rental Relation

Rental stores information about each vehicle rental transaction.

### Schema

Rental(
rental_id,
customer_id,
vehicle_id,
staff_id,
start_date,
end_date,
return_date,
status
)

### Primary Key

rental_id

### Foreign Keys

customer_id references Customer(customer_id)
vehicle_id references Vehicle(vehicle_id)
staff_id references Staff(staff_id)

### Attributes

* rental_id: Unique ID for each rental
* customer_id: Customer who rented the vehicle
* vehicle_id: Vehicle being rented
* staff_id: Staff member who handled the rental
* start_date: Rental start date
* end_date: Expected rental end date
* return_date: Actual return date
* status: Rental status such as Active or Returned

---

## 5. Payment Relation

Payment stores payment information for rental transactions.

### Schema

Payment(
payment_id,
rental_id,
amount,
payment_date,
payment_method
)

### Primary Key

payment_id

### Foreign Key

rental_id references Rental(rental_id)

### Attributes

* payment_id: Unique ID for each payment
* rental_id: Rental connected to the payment
* amount: Payment amount
* payment_date: Date of payment
* payment_method: Payment method such as Cash, Credit Card, or Debit Card

---

## 6. Maintenance Relation

Maintenance stores maintenance and repair records for vehicles.

### Schema

Maintenance(
maintenance_id,
vehicle_id,
maintenance_date,
description,
cost,
status
)

### Primary Key

maintenance_id

### Foreign Key

vehicle_id references Vehicle(vehicle_id)

### Attributes

* maintenance_id: Unique ID for each maintenance record
* vehicle_id: Vehicle that received maintenance
* maintenance_date: Date of maintenance
* description: Description of the maintenance work
* cost: Cost of the maintenance
* status: Maintenance status such as Scheduled or Completed

---

## Relationship Summary

### Customer and Rental

One customer can have many rentals.
Each rental belongs to one customer.

Relationship:

Customer 1-to-many Rental

---

### Vehicle and Rental

One vehicle can appear in many rental records over time.
Each rental is for one vehicle.

Relationship:

Vehicle 1-to-many Rental

---

### Staff and Rental

One staff member can manage many rentals.
Each rental is managed by one staff member.

Relationship:

Staff 1-to-many Rental

---

### Rental and Payment

One rental can have one or more payments.
Each payment belongs to one rental.

Relationship:

Rental 1-to-many Payment

---

### Vehicle and Maintenance

One vehicle can have many maintenance records.
Each maintenance record belongs to one vehicle.

Relationship:

Vehicle 1-to-many Maintenance

---

## Final List of Relations

Customer(customer_id PK, first_name, last_name, phone, email UNIQUE, drivers_license UNIQUE)

Staff(staff_id PK, first_name, last_name, phone, email UNIQUE, role)

Vehicle(vehicle_id PK, make, model, year, license_plate UNIQUE, daily_rate, status)

Rental(rental_id PK, customer_id FK, vehicle_id FK, staff_id FK, start_date, end_date, return_date, status)

Payment(payment_id PK, rental_id FK, amount, payment_date, payment_method)

Maintenance(maintenance_id PK, vehicle_id FK, maintenance_date, description, cost, status)

## Notes

The Rental table connects Customer, Vehicle, and Staff. This allows the database to track which customer rented which vehicle and which staff member handled the rental.

The Payment table is separate from Rental because a rental may have payment information connected to it, and separating payments makes the design more organized.

The Maintenance table is separate from Vehicle because each vehicle can have many maintenance records over time.
