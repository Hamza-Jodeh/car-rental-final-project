# Car Rental Database and Management System

## Project Overview

This project is a Car Rental Database and Management System created for CS4092 Database Design and Development and CS3003 Programming Languages.

The system allows staff members to manage customers, vehicles, rentals, payments, and maintenance records. It uses a relational database to store the data and a Python command-line interface to interact with the system.

## Instructor Approval

This project was approved as a combined final project for both CS4092 Database Design and Development and CS3003 Programming Languages.

## Courses

- CS4092 Database Design and Development
- CS3003 Programming Languages

## Main Features

- Initialize the database
- View available vehicles
- Search vehicles by make or model
- Add new customers
- Add new vehicles
- Rent vehicles
- Return vehicles
- View rental history
- View payment records
- Add maintenance records

## Database Tables

The project includes six main tables:

1. Customer
2. Staff
3. Vehicle
4. Rental
5. Payment
6. Maintenance

## Technologies Used

- Python
- SQLite
- SQL
- Git
- GitHub

## Project Structure

```text
car-rental-final-project/

- README.md
- requirements/
  - requirements-document.md
- design/
  - schema-design.md
  - er-diagram.png
- sql/
  - database.sql
  - queries.sql
- src/
  - main.py
  - database.py
  - models.py
- docs/
  - programming-languages-writeup.md
- video/
  - demo-video-link.txt
- screenshots/
```

## How to Run the Project

### 1. Clone the Repository

```bash
git clone https://github.com/Hamza-Jodeh/car-rental-final-project.git
```

### 2. Go Into the Project Folder

```bash
cd car-rental-final-project
```

### 3. Run the Program

```bash
python src/main.py
```

If `python` does not work, use:

```bash
python3 src/main.py
```

### 4. Initialize the Database

When the menu opens, choose option:

```text
1. Initialize database
```

This creates the SQLite database and inserts sample data.

## CLI Menu

The command-line program includes this menu:

```text
====================================
 Car Rental Management System
====================================
1. Initialize database
2. View available vehicles
3. Search vehicles
4. Add customer
5. Add vehicle
6. Rent vehicle
7. Return vehicle
8. View rental history
9. View payments
10. Add maintenance record
0. Exit
```

## SQL Files

The SQL database implementation is located in:

```text
sql/database.sql
```

This file includes:

- Table creation statements
- Primary keys
- Foreign keys
- Sample insert data

The required SQL queries are located in:

```text
sql/queries.sql
```

This file includes multiple SQL queries, including multi-table queries using joins.

## Database Design Connection

For CS4092, this project includes:

- Requirements gathering document
- ER diagram
- Relational schema design
- SQL database implementation
- Sample data
- SQL queries
- Python-based database interaction
- Video demonstration

The database portion focuses on designing a relational database with clear entities, attributes, primary keys, foreign keys, and relationships.

## Programming Languages Connection

For CS3003, this project uses Python to demonstrate:

- Object-oriented programming
- Classes and objects
- Methods
- Encapsulation
- Imperative programming
- Functions
- Control structures
- Error handling
- Database interaction using SQLite

The project includes model classes such as:

- Customer
- Staff
- Vehicle
- Rental
- Payment
- Maintenance

The command-line menu demonstrates step-by-step application logic and interaction with the database.

## Example Use Cases

The system supports these use cases:

1. A staff member views available vehicles.
2. A staff member searches vehicles by make or model.
3. A staff member adds a new customer.
4. A staff member adds a new vehicle.
5. A staff member rents a vehicle to a customer.
6. A staff member returns a rented vehicle.
7. A staff member views rental history.
8. A staff member views payment records.
9. A staff member adds a vehicle maintenance record.

## Author

Hamzah Jodeh