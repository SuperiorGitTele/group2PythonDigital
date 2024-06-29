import mysql.connector
from mysql.connector import errorcode

def show_table_structure_and_contents():
    db = None  # Define db at the start to avoid unbound variable issues
    try:
        # Connect to the database
        db = mysql.connector.connect(
            host="localhost",
            user="Bank",
            password="Bankappsql",
            database="Bank_data",
            auth_plugin='mysql_native_password'  # Use if changing the user's plugin isn't possible
        )
        
        with db.cursor() as cursor:
            # Show table structure
            cursor.execute("DESCRIBE users")
            table_description = cursor.fetchall()
            print("Table Structure:")
            for row in table_description:
                print(row)
            
            # Show table contents
            cursor.execute("SELECT * FROM users")
            rows = cursor.fetchall()
            print("\nTable Contents:")
            for row in rows:
                print(row)
    
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Error: Access denied. Check your username and password.")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Error: Database does not exist.")
        elif err.errno == errorcode.CR_CONNECTION_ERROR:
            print("Error: Could not connect to MySQL server.")
        elif "caching_sha2_password" in str(err):
            print("Error: Authentication plugin 'caching_sha2_password' is not supported.")
        else:
            print(f"Error: {err}")
    finally:
        if db and db.is_connected():
            db.close()

# Example usage
if __name__ == "__main__":
    show_table_structure_and_contents()
