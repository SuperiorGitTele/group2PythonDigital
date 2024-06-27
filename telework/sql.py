import mysql.connector
from mysql.connector import errorcode

def setup_database():
    try:
        # Connect to MySQL server
        db = mysql.connector.connect(
            host="localhost",
            user="tele",
            password="telesql19"
        )
        cursor = db.cursor()

        # Create database if it doesn't exist
        cursor.execute("CREATE DATABASE IF NOT EXISTS new_database")
        cursor.execute("USE new_database")

        # Create table if it doesn't exist
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INT AUTO_INCREMENT PRIMARY KEY,
            username VARCHAR(255) NOT NULL,
            password VARCHAR(255) NOT NULL,
            dob DATE NOT NULL,
            secret_question VARCHAR(255),
            secret_answer VARCHAR(255),
            transaction_pin VARCHAR(255),
            account_number VARCHAR(255) NOT NULL,
            account_balance DECIMAL(10, 2) NOT NULL,
            reference_code VARCHAR(255),
            bvn VARCHAR(255),
            account_name VARCHAR(255),
            email VARCHAR(255)
        )
        """)

        # Insert a sample user (if needed)
        cursor.execute("""
        INSERT INTO users (username, password, dob, secret_question, secret_answer, transaction_pin, account_number, account_balance, reference_code, bvn, account_name, email)
        VALUES ('sample_user', 'sample_pass', '1990-01-01', 'Your favorite color?', 'Blue', '1234', 'ACC123', 1000.00, 'REF123', '12345678901', 'Sample Name', 'sample@example.com')
        """)

        db.commit()

        print("Database setup complete. Sample user inserted.")

    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Error: Access denied. Check your username and password.")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Error: Database does not exist.")
        else:
            print(err)
    finally:
        cursor.close()
        db.close()

if __name__ == "__main__":
    setup_database()
