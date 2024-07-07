import mysql.connector
from mysql.connector import errorcode

def create_mysql_user_and_database(new_username, new_password, new_database):
    try:
        # Connect to MySQL server as root
        db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="rootsql19"  # Replace with your root password
        )
        cursor = db.cursor()

        # Check if the user already exists
        cursor.execute(f"SELECT EXISTS(SELECT 1 FROM mysql.user WHERE user = '{new_username}')")
        user_exists = cursor.fetchone()[0]
        
        if user_exists:
            print(f"User '{new_username}' already exists. Skipping user creation.")
        else:
            # Create new user
            cursor.execute(f"CREATE USER '{new_username}'@'localhost' IDENTIFIED BY '{new_password}';")
            print(f"User '{new_username}' created.")

        # Check if the database already exists
        cursor.execute(f"SHOW DATABASES LIKE '{new_database}'")
        database_exists = cursor.fetchone()

        if database_exists:
            print(f"Database '{new_database}' already exists. Skipping database creation.")
        else:
            # Create new database
            cursor.execute(f"CREATE DATABASE {new_database}")
            print(f"Database '{new_database}' created.")

        # Grant privileges to the new user on the new database
        cursor.execute(f"GRANT ALL PRIVILEGES ON {new_database}.* TO '{new_username}'@'localhost';")
        cursor.execute("FLUSH PRIVILEGES;")
        cursor.execute(f"ALTER USER '{new_username}'@'localhost' IDENTIFIED WITH mysql_native_password BY '{new_password}';")
        cursor.execute("FLUSH PRIVILEGES;")
        

        cursor.execute("""
        CREATE TABLE Bank_data.users (
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
            last_login DATETIME,
            INDEX (username)
        )
        """)

        # Create 'transactions' table
        cursor.execute("""
        CREATE TABLE Bank_data.transactions (
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
        CREATE TABLE Bank_data.beneficiaries (
            id INT AUTO_INCREMENT PRIMARY KEY,
            username VARCHAR(255) NOT NULL,
            name VARCHAR(255) NOT NULL,
            account_number VARCHAR(255) NOT NULL,
            FOREIGN KEY (username) REFERENCES users(username),
            UNIQUE (username, account_number)
        )
        """)
        cursor.execute("""
        CREATE TABLE Bank_data.Admin (
            id INT AUTO_INCREMENT PRIMARY KEY,
            Admin VARCHAR(255) NOT NULL UNIQUE,
            password VARCHAR(255) NOT NULL,
        )
        """)
        print(f"Privileges granted to user '{new_username}' on database '{new_database}'.")

    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Error: Access denied. Check your username and password.")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Error: Database does not exist.")
        else:
            print(f"Error: {err}")
    finally:
        if cursor:
            cursor.close()
        if db:
            db.close()

# Example usage
if __name__ == "__main__":
    create_mysql_user_and_database("Bank", "Bankappsql", "Bank_data")
