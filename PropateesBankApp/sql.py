import mysql.connector
from mysql.connector import errorcode



def setup_database():
    try:
        # Connect to MySQL server
        db = mysql.connector.connect(
            host="localhost",
            user="pamela",
            password="Bankmysql",
            database="new_data"
        )
        cursor = db.cursor()

        # Drop existing tables if they exist
        cursor.execute("DROP TABLE IF EXISTS transactions")
        cursor.execute("DROP TABLE IF EXISTS beneficiaries")
        cursor.execute("DROP TABLE IF EXISTS users")

        # Create 'users' table
        cursor.execute("""
        CREATE TABLE users (
            id INT AUTO_INCREMENT PRIMARY KEY,
            username VARCHAR(255) NOT NULL UNIQUE,
            password VARCHAR(255) NOT NULL,
            dob DATE NOT NULL,
            secret_question VARCHAR(255),
            secret_answer VARCHAR(255),
            transaction_pin VARCHAR(255),
            account_number VARCHAR(255) NOT NULL UNIQUE,
            account_balance DECIMAL(10, 2) NOT NULL,
            reference_code VARCHAR(255),
            bvn VARCHAR(255),
            account_name VARCHAR(255),
            email VARCHAR(255),
            INDEX (username)  -- Add index for username to support foreign key references
        )
        """)

        # Create 'transactions' table
        cursor.execute("""
        CREATE TABLE transactions (
            id INT AUTO_INCREMENT PRIMARY KEY,
            username VARCHAR(255) NOT NULL,
            date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
            trans_type VARCHAR(50) NOT NULL,
            amount DECIMAL(10, 2) NOT NULL,
            balance DECIMAL(10, 2) NOT NULL,
            recipient_account VARCHAR(255),
            recipient_name VARCHAR(255),
            FOREIGN KEY (username) REFERENCES users(username)
        )
        """)

        # Create 'beneficiaries' table
        cursor.execute("""
        CREATE TABLE beneficiaries (
            id INT AUTO_INCREMENT PRIMARY KEY,
            username VARCHAR(255) NOT NULL,
            name VARCHAR(255) NOT NULL,
            account_number VARCHAR(255) NOT NULL,
            FOREIGN KEY (username) REFERENCES users(username),
            UNIQUE (username, account_number)
        )
        """)

        # Insert a sample user (if needed)
        cursor.execute("""
        INSERT INTO users (username, password, dob, secret_question, secret_answer, transaction_pin, account_number, account_balance, reference_code, bvn, account_name, email)
        VALUES ('sample_user', 'sample_pass', '1990-01-01', 'Your favorite color?', 'Blue', '1234', 'ACC123', 1000.00, 'REF123', '12345678901', 'Sample Name', 'sample@example.com')
        ON DUPLICATE KEY UPDATE
            password = VALUES(password),
            dob = VALUES(dob),
            secret_question = VALUES(secret_question),
            secret_answer = VALUES(secret_answer),
            transaction_pin = VALUES(transaction_pin),
            account_balance = VALUES(account_balance),
            reference_code = VALUES(reference_code),
            bvn = VALUES(bvn),
            account_name = VALUES(account_name),
            email = VALUES(email)
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
    


    

