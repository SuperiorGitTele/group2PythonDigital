import tkinter as tk
from tkinter import ttk
import sqlite3
from sideBar import Sidebar
from tkinter import messagebox
import mysql.connector
from PIL import ImageTk, Image

class WelcomeWindow:
    def __init__(self, master, username):
        self.master = master
        self.username = username
        self.new_window = tk.Toplevel(self.master)
        self.new_window.title("PROPATEES Bank App")

        # Get the screen's width and height
        screen_width = self.new_window.winfo_screenwidth()
        screen_height = self.new_window.winfo_screenheight()

        # Assuming the taskbar's height is 40 pixels (you may need to adjust this)
        taskbar_height = 50

        # Set the window's geometry to the screen's width and height, minus the taskbar's height
        self.new_window.geometry(f"{screen_width}x{screen_height - taskbar_height}")

        self.new_window.state('normal')  # Instead of 'zoomed', use 'normal' to allow the window to be resized
        self.new_window.resizable(0, 0)  # But then disable resizing
        self.new_window.configure(bg='#F7E7CE')

        self.lgn_frame = tk.Frame(self.new_window, bg='#3B3C36', bd=5, height=220, width=1528)
        self.lgn_frame.place(x=0, y=0)

        # logo pic
        self.logoside = Image.open('ps2.png')
        self.logoside = self.logoside.resize((80, 80), resample=Image.LANCZOS)  # Resize the image to 50x50 pixels using Lanczos resampling
        logos = ImageTk.PhotoImage(self.logoside)
        self.logo_label = tk.Label(self.new_window, image=logos, width='80', height="80", bg='#3B3C36')
        self.logo_label.image = logos
        self.logo_label.__reduce__()
        self.logo_label.place(x=70, y=0)

        label = tk.Label(self.lgn_frame, text=f"Welcome {username}, to our simple and easy to use bank app!", font=('yu gothic ui', 16, 'bold'), bg='#FF4F00', fg='white')
        label.place(x=900, y=36)
        self.lgn_frame.after(5000, label.destroy)

        style = ttk.Style()
        style.configure("Big.TButton", font=("Arial", 17), foreground="red", background="black")

        # Create a Button to check the account balance
        self.check_balance_button = ttk.Button(self.lgn_frame, text="Check Balance", style="Big.TButton", command=lambda: self.toggle_balance(username))
        self.check_balance_button.place(x=320, y=120)

        # Create a Button to initiate money transfer
        self.transfer_button = ttk.Button(self.lgn_frame, text="Transfer", style="Big.TButton", command=self.show_transfer_dialog)
        self.transfer_button.place(x=580, y=120)

        # 
        self.fund_account_button = ttk.Button(self.lgn_frame, text="""Fund your account from 
your other PTP account""", style="Big.TButton", command=self.show_fund_account_dialog)
        self.fund_account_button.place(x=820, y=120)

        self.subscribe_button = ttk.Button(self.lgn_frame, text="Subscription", style="Big.TButton")
        self.subscribe_button.place(x=1150, y=120)

        # Create a Label to display the account balance
        self.balance_label = None

        loginpage = tk.Button(self.new_window, text='LOG OUT', font=("yu gothic ui", 13, "bold"), width=10, bd=0, bg='#3047ff', cursor='hand2', activebackground='#3047ff', fg='white', command=self.go_backLogin1)
        loginpage.place(x=1400, y=700)

        # self.sidebar_button = tk.Button(self.lgn_frame, text="------\n------\n-------", font=("yu gothic ui", 13, "bold"), width=15, bd=0, bg='#3047ff', cursor='hand2', activebackground='#3047ff', fg='white', command=self.toggle_sidebar)
        # self.sidebar_button.place(x=1000, y=10)

        # Open the image file
        image = Image.open("drop.png")

        # Resize the image
        image = image.resize((40, 40), resample=Image.LANCZOS)  # Replace (20, 20) with your desired size

        # Convert the image to a PhotoImage
        dropdown_image = ImageTk.PhotoImage(image)

        self.sidebar_button = tk.Button(self.lgn_frame, image=dropdown_image, compound="top", font=("yu gothic ui", 4, "bold"), width=70, bd=0, bg='red', cursor='hand2', activebackground='#3B3C36', fg='white', command=self.toggle_sidebar)
        self.sidebar_button.image = dropdown_image
        self.sidebar_button.place(x=10, y=0)

        self.settings = tk.StringVar()
        self.settings.set("Settings")  # default value

        self.sidebar_menu = ttk.OptionMenu(self.lgn_frame, self.settings, "Change UserName", "Edit Account Details", command=self.toggle_sidebar)
        self.sidebar_menu.place(x=1400, y=10)

        self.sidebar = None

        self.bankHistory = tk.Frame(self.new_window,bg='blue', width='700', height="350")
        self.bankHistory.place(x=310, y=300)

        self.txt = """History"""
        self.heading = tk.Label(self.bankHistory, text=self.txt, font=('yu gothic ui', 25, 'bold'), bg='#3B3C36', fg='white')
        self.heading.place(x=0, y=5, width=550, height=60)

        self.bene_frame = tk.Frame(self.new_window   , bg='PINK', width='400', height="350")
        self.bene_frame.place(x=1040, y=300)

    def toggle_sidebar(self):
        if self.sidebar is None:
            self.sidebar = Sidebar(self.new_window)
            self.sidebar.place(x=1528, y=0, relwidth=0.2, relheight=1)
        self.sidebar.toggle()

    def get_account_balance(self, username):
        # Connect to MySQL database
        db = mysql.connector.connect(
            host="localhost",
            user="tele",
            password="telesql19",
            database="new_database"
        )
        cursor = db.cursor()

        try:
            # Get account balance from database
            cursor.execute("SELECT account_balance FROM users WHERE username = %s", (username,))
            row = cursor.fetchone()

            if row:
                return row[0]
            else:
                return None
        except mysql.connector.Error as err:
            messagebox.showerror("Database Error", f"Error: {err}")
            return None
        finally:
            cursor.close()
            db.close()


    def toggle_balance(self, username):
        if self.balance_label is None:
            # Get the account balance from the database or wherever it's stored
            account_balance = self.get_account_balance(username)  # Replace with your own function
            style = ttk.Style()
            style.configure("Big.TLabel", font=("Arial", 15), foreground="red", background="brown")

            # Create a Label to display the account balance
            self.balance_label = ttk.Label(self.lgn_frame, text=f"Account Balance ₦: {account_balance}", style="Big.TLabel", width="23")
            self.balance_label.place(x=320, y=160)
        else:
            self.balance_label.place_forget()
            self.balance_label = None


    def show_transfer_dialog(self):
        transfer_dialog = tk.Toplevel(self.new_window)
        transfer_dialog.title("Transfer Money")

        tk.Label(transfer_dialog, text="Recipient Account Number:").pack()
        recipient_entry = tk.Entry(transfer_dialog)
        recipient_entry.pack()

        tk.Label(transfer_dialog, text="Amount to Transfer ₦ :").pack()
        amount_entry = tk.Entry(transfer_dialog)
        amount_entry.pack()

        tk.Label(transfer_dialog, text="Transaction PIN:").pack()
        pin_entry = tk.Entry(transfer_dialog, show="*")
        pin_entry.pack()

        def transfer_callback():
            recipient_account = recipient_entry.get()
            try:
                amount = int(amount_entry.get())
            except ValueError:
                messagebox.showerror("Error", "Invalid amount. Please enter a numeric value.")
                return
            transaction_pin = pin_entry.get()

            self.transfer_money(self.username, recipient_account, amount, transaction_pin)
            transfer_dialog.destroy()

        tk.Button(transfer_dialog, text="Transfer", command=transfer_callback).pack()

    def transfer_money(self, sender_username, recipient_account, amount, transaction_pin):
        # Connect to MySQL database
        db = mysql.connector.connect(
            host="localhost",
            user="tele",
            password="telesql19",
            database="new_database"
        )
        cursor = db.cursor()

        try:
            # Fetch sender's details
            cursor.execute("SELECT account_number, account_balance, transaction_pin FROM users WHERE username = %s", (sender_username,))
            sender = cursor.fetchone()
            if not sender:
                messagebox.showerror("Error", "Sender account not found.")
                return

            sender_account, sender_balance, stored_pin = sender

            # Validate transaction PIN
            if transaction_pin != stored_pin:
                messagebox.showerror("Error", "Invalid transaction PIN.")
                return

            # Ensure sufficient balance
            if sender_balance < amount:
                messagebox.showerror("Error", "Insufficient balance.")
                return

            # Fetch recipient's details
            cursor.execute("SELECT account_balance FROM users WHERE account_number = %s", (recipient_account,))
            recipient = cursor.fetchone()
            if not recipient:
                messagebox.showerror("Error", "Recipient account not found.")
                return

            recipient_balance = recipient[0]

            # Update balances
            new_sender_balance = sender_balance - amount
            new_recipient_balance = recipient_balance + amount

            cursor.execute("UPDATE users SET account_balance = %s WHERE account_number = %s", (new_sender_balance, sender_account))
            cursor.execute("UPDATE users SET account_balance = %s WHERE account_number = %s", (new_recipient_balance, recipient_account))
            db.commit()

            messagebox.showinfo("Success", "Transfer completed successfully!")

            # Update balance display if visible
            if self.balance_label:
                self.toggle_balance(sender_username)
                self.toggle_balance(sender_username)

        except mysql.connector.Error as err:
            messagebox.showerror("Database Error", f"Error: {err}")
        finally:
            cursor.close()
            db.close()

    def show_fund_account_dialog(self):
        fund_account_dialog = tk.Toplevel(self.new_window)
        fund_account_dialog.title("Fund Your Account")

        tk.Label(fund_account_dialog, text="Other Account Number:").pack()
        other_account_entry = tk.Entry(fund_account_dialog)
        other_account_entry.pack()

        tk.Label(fund_account_dialog, text="Other Username:").pack()
        other_username_entry = tk.Entry(fund_account_dialog)
        other_username_entry.pack()

        tk.Label(fund_account_dialog, text="Other BVN:").pack()
        other_bvn_entry = tk.Entry(fund_account_dialog)
        other_bvn_entry.pack()

        tk.Label(fund_account_dialog, text="Other Password:").pack()
        other_password_entry = tk.Entry(fund_account_dialog, show="*")
        other_password_entry.pack()

        tk.Label(fund_account_dialog, text="Amount to Withdraw:").pack()
        amount_entry = tk.Entry(fund_account_dialog)
        amount_entry.pack()

        def fund_callback():
            other_account_number = other_account_entry.get()
            other_username = other_username_entry.get()
            other_bvn = other_bvn_entry.get()
            other_password = other_password_entry.get()
            try:
                amount = int(amount_entry.get())
            except ValueError:
                messagebox.showerror("Error", "Invalid amount. Please enter a numeric value.")
                return

            self.fund_account_from_other(self.username, other_account_number, other_username, other_bvn, other_password, amount)
            fund_account_dialog.destroy()

        tk.Button(fund_account_dialog, text="Fund", command=fund_callback).pack()


    def fund_account_from_other(self, current_username, other_account_number, other_username, other_bvn, other_password, amount):
        # Connect to MySQL database
        db = mysql.connector.connect(
            host="localhost",
            user="tele",
            password="telesql19",
            database="new_database"
        )
        cursor = db.cursor()

        try:
            # Fetch other account's details
            cursor.execute("""
                SELECT username, bvn, password, account_balance 
                FROM users 
                WHERE account_number = %s
            """, (other_account_number,))
            other_account = cursor.fetchone()
            
            if not other_account:
                messagebox.showerror("Error", "Other account not found.")
                return

            other_db_username, other_db_bvn, other_db_password, other_balance = other_account

            # Validate other account's details
            if other_username != other_db_username or other_bvn != other_db_bvn or other_password != other_db_password:
                messagebox.showerror("Error", "Invalid other account details.")
                return

            # Ensure sufficient balance in other account
            if other_balance < amount:
                messagebox.showerror("Error", "Insufficient balance in the other account.")
                return

            # Fetch current account details
            cursor.execute("""
                SELECT account_number, account_balance 
                FROM users 
                WHERE username = %s
            """, (current_username,))
            current_account = cursor.fetchone()
            
            if not current_account:
                messagebox.showerror("Error", "Current account not found.")
                return

            current_account_number, current_balance = current_account

            # Update balances
            new_other_balance = other_balance - amount
            new_current_balance = current_balance + amount

            cursor.execute("UPDATE users SET account_balance = %s WHERE account_number = %s", (new_other_balance, other_account_number))
            cursor.execute("UPDATE users SET account_balance = %s WHERE account_number = %s", (new_current_balance, current_account_number))
            db.commit()

            messagebox.showinfo("Success", "Funds transferred successfully!")

            # Update balance display if visible
            if self.balance_label:
                self.toggle_balance(current_username)
                self.toggle_balance(current_username)

        except mysql.connector.Error as err:
            messagebox.showerror("Database Error", f"Error: {err}")
        finally:
            cursor.close()
            db.close()




    def go_backLogin1(self):
        self.new_window.withdraw()
        self.master.deiconify()


# root = tk.Tk()
# welcome_window = WelcomeWindow(root, "username")
# root.withdraw()  # Hide the root window
# welcome_window.new_window.mainloop()