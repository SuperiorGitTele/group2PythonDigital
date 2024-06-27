import mysql.connector
from mysql.connector import errorcode


def create_mysql_user():
    try:
        db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root_password"  # Replace with your root password
        )
        cursor = db.cursor()

        # Create new user and grant privileges
        cursor.execute("CREATE USER 'bank'@'localhost' IDENTIFIED BY 'tele2sql12';")
        cursor.execute("GRANT ALL PRIVILEGES ON new_data.* TO 'bank'@'localhost';")
        cursor.execute("FLUSH PRIVILEGES;")
        print("User 'tele2' created and granted privileges.")
        
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



def setup_database():
    try:
        # Connect to MySQL server
        db = mysql.connector.connect(
            host="localhost",
            user="tele2",
            password="tele2sql12",
            database="new_data"
        )
        cursor = db.cursor()


        # Create database if it doesn't exist
        cursor.execute("CREATE DATABASE IF NOT EXISTS new_data")
        cursor.execute("USE new_data")

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
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS transactions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            date TIMESTAMP NOT NULL,
            trans_type TEXT NOT NULL,
            amount REAL NOT NULL,
            balance REAL NOT NULL,
            recipient_account TEXT NOT NULL,
            recipient_name TEXT NOT NULL
        );""")
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS beneficiaries (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            name TEXT NOT NULL,
            account_number TEXT NOT NULL,
            FOREIGN KEY (username) REFERENCES users(username),
            UNIQUE (username, name, account_number)
        );""")


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
    if create_mysql_user:
            setup_database
    setup_database()
    
