import tkinter as tk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector

def create_toplevel():
    # Create a Toplevel window
    adminBank.withdraw()
    toplevel = tk.Toplevel(adminBank)
    toplevel.title("Admin Deposit")
    toplevel.geometry("350x250")
    toplevel.configure(bg='#003262')
    img = ImageTk.PhotoImage(file='logo.png')
    toplevel.iconphoto(False, img)

    # Load the image using Pillow
    image = Image.open("logopng.png")
    photo = ImageTk.PhotoImage(image)

    label = tk.Label(toplevel, image=photo, bg='#003262')
    label.image = photo 
    label.place(x=130, y=0)

    UserAcctLabel = tk.Label(toplevel, text=f"User Account Bvn", bg='#0095B6')
    UserAcctLabel.place(x=50, y=40)
    Userbvn_entry = tk.Entry(toplevel)
    Userbvn_entry.place(x=50, y=63)

    acctNumLabel = tk.Label(toplevel, text=f"Account Number", bg='#0095B6')
    acctNumLabel.place(x=50, y=85)
    acctNum_entry = tk.Entry(toplevel)
    acctNum_entry.place(x=50, y=108)

    ammountLabel = tk.Label(toplevel, text=f"Amount To Deposit ₦:", bg='#0095B6')
    ammountLabel.place(x=50, y=135)
    num_entry = tk.Entry(toplevel)
    num_entry.place(x=50, y=160)

    passwordLabel = tk.Label(toplevel, text=f"Password", bg='#0095B6')
    passwordLabel.place(x=50, y=180)
    password_entry = tk.Entry(toplevel)
    password_entry.config(show='*')
    password_entry.place(x=50, y=200)
    password_entry.bind("<Return>", lambda event: deposit())

    def deposit():
        userbvn = Userbvn_entry.get()
        recipient_account = acctNum_entry.get()
        password = password_entry.get()
        amount = int(num_entry.get())

        if not userbvn or not recipient_account or not amount:
            messagebox.showerror("Error", "Please fill in all fields")
            return

        db = mysql.connector.connect(
            host="localhost",
            user="Bank",
            password="Bankappsql",
            database="Bank_data",
            auth_plugin='mysql_native_password'
        )
        cursor = db.cursor()
        
        try:
            

            cursor.execute("SELECT * FROM admin WHERE password = %s", (password,))
            row = cursor.fetchone()
            db.commit()

            if row:
                cursor.execute("SELECT bvn, account_balance FROM users WHERE account_number = %s", (recipient_account,))
                recipient = cursor.fetchone()
                if not recipient:
                    messagebox.showerror("Error", "Recipient account not found.")
                    return

                username1, recipient_balance = recipient
                if username1 != userbvn:
                    messagebox.showerror("Error", "Recipient account not found.")
                    return
            
                if isinstance(recipient_balance, tuple):
                    recipient_balance = recipient_balance[0]

                new_recipient_balance = recipient_balance + amount

                
                cursor.execute("UPDATE users SET account_balance = %s WHERE account_number = %s", (new_recipient_balance, recipient_account))
                db.commit()
               


        except mysql.connector.Error as err:
            messagebox.showerror("Database Error", f"Error: {err}")
        finally:
            cursor.close()
            db.close()
        

    tk.Button(toplevel, text="Deposit", bg="Purple", command=deposit).place(x=50, y=220)
    num_entry.bind("<Return>", lambda event: deposit())
    
    def Admin_window():
        # Update window size info
        toplevel.update_idletasks()
        width = toplevel.winfo_width()
        height = toplevel.winfo_height()
        x = (toplevel.winfo_screenwidth() // 2) - (width // 2)
        y = (toplevel.winfo_screenheight() // 2) - (height // 2)
        toplevel.geometry(f'{width}x{height}+{x}+{y}')
    Admin_window()

    def backLogin():
        name_entry.delete(0, tk.END)
        password_entry.delete(0, tk.END)
        toplevel.withdraw()
        adminBank.deiconify()
    tk.Button(toplevel, text="Log Out", bg="#0095B6",command=backLogin).place(x=280, y=222)
    

def center_window():
    # Update window size info
    adminBank.update_idletasks()
    width = adminBank.winfo_width()
    height = adminBank.winfo_height()
    x = (adminBank.winfo_screenwidth() // 2) - (width // 2)
    y = (adminBank.winfo_screenheight() // 2) - (height // 2)
    adminBank.geometry(f'{width}x{height}+{x}+{y}')

def adminLogin():
    username = name_entry.get()
    password = password_entry.get()

    if not username or not password:
        messagebox.showerror("Error", "Please fill in all fields")
        return

    # Connect to MySQL database
    db = mysql.connector.connect(
        host="localhost",
        user="Bank",
        password="Bankappsql",
        database="Bank_data",
        auth_plugin='mysql_native_password'
    )
    cursor = db.cursor()

    try:
        # Check if username and password exist in the database
        cursor.execute("SELECT * FROM admin WHERE Admin = %s AND password = %s", (username, password))
        row = cursor.fetchone()

        if row:
                # Show a message box with a welcome message
                messagebox.showinfo("Login Success", f"Welcome Admin {username}! Login successful!")
                adminBank.withdraw()
                create_toplevel()


        else:
            messagebox.showerror("Login Error", "Invalid username or password")

    except mysql.connector.Error as err:
        messagebox.showerror("Database Error", f"Error: {err}")
    finally:
        # Close the connection
        cursor.close()
        db.close()

        
# Create the main Tk window
adminBank = tk.Tk()
adminBank.title("Main Window")
adminBank.geometry("350x250")
adminBank.configure(bg='#003262')
img = ImageTk.PhotoImage(file='logo.png')
adminBank.iconphoto(False, img)

center_window()

# Load the image using Pillow
image = Image.open("logopng.png")
photo = ImageTk.PhotoImage(image)

label = tk.Label(adminBank, image=photo, bg='#003262')
label.image = photo 
label.place(x=130, y=0)

label = tk.Label(adminBank, text=f"Welcome Admin, login in", bg='#0095B6')
label.place(x=10, y=10)

entryLabel = tk.Label(adminBank, text=f"Admin", bg='#0095B6')
entryLabel.place(x=50, y=40)
name_entry = tk.Entry(adminBank)
name_entry.place(x=50, y=63)

passwordLabel = tk.Label(adminBank, text=f"Password", bg='#0095B6')
passwordLabel.place(x=50, y=85)
password_entry = tk.Entry(adminBank)
password_entry.config(show='*')
password_entry.place(x=50, y=108)
password_entry.bind("<Return>", lambda event: adminLogin())

button = tk.Button(adminBank, text="Login", bg='#0095B6', command=adminLogin)
button.place(x=50, y=150)


# Run the Tkinter event loop
adminBank.mainloop()
