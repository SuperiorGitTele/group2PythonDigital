import mysql.connector

# Connect to the database
db = mysql.connector.connect(
    host="localhost",
    user="tele2",
    password="tele2sql12",
    database="new_data"
)

cursor = db.cursor()

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

# Close the connection
cursor.close()
db.close()
