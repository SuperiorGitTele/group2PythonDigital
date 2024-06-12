import mysql.connector

def create_database_and_table():
    db = mysql.connector.connect(
        host="localhost",
        user="tele",
        password="telesql19"
    )
    cursor = db.cursor()

    # Create the database
    cursor.execute("CREATE DATABASE IF NOT EXISTS new_database;")

    # Select the database
    cursor.execute("USE new_database;")

    # Create the users table with added constraints
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            username VARCHAR(150) NOT NULL CHECK (LENGTH(username) >= 3),
            password VARCHAR(150) NOT NULL CHECK (LENGTH(password) >= 8),
            dob DATE NOT NULL,
            secret_question VARCHAR(150) NOT NULL,
            secret_answer VARCHAR(255) NOT NULL,
            transaction_pin CHAR(4) NOT NULL,
            account_number VARCHAR(150) NOT NULL,
            account_balance INT NOT NULL,
            reference_code VARCHAR(150) DEFAULT NULL,
            bvn VARCHAR(150) NOT NULL,
            account_name VARCHAR(150) NOT NULL,
            email VARCHAR(150) DEFAULT NULL,  -- Email is optional
            PRIMARY KEY (username)
        );
    """)

    db.commit()
    cursor.close()
    db.close()

    print("Database 'new_database' and table 'users' created successfully.")

# Create the database and table when the script is run directly
if __name__ == "__main__":
    create_database_and_table()
