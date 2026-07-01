import sqlite3
import os

DB_NAME = "car_rental.db"


def get_connection():
    """
    Creates and returns a connection to the SQLite database.
    """
    connection = sqlite3.connect(DB_NAME)
    connection.row_factory = sqlite3.Row
    return connection


def initialize_database():
    """
    Creates the database tables and inserts sample data
    using the SQL script in sql/database.sql.
    """
    connection = get_connection()
    cursor = connection.cursor()

    sql_file_path = os.path.join("sql", "database.sql")

    with open(sql_file_path, "r") as file:
        sql_script = file.read()

    cursor.executescript(sql_script)

    connection.commit()
    connection.close()

    print("Database created and sample data inserted successfully.")
