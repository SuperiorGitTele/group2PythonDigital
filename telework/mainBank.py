import tkinter as tk
from tkinter import ttk
import sqlite3
from sideBar import Sidebar
from tkinter import messagebox
import mysql.connector
from PIL import ImageTk, Image
from datetime import datetime

class WelcomeWindow:
    def __init__(self, master, username):
        self.master = master
        self.username = username
        self.new_window = tk.Toplevel(self.master)
        self.new_window.title("PROPATEES Bank App")

        # img = ImageTk.PhotoImage(file='logo.png')
        # self.iconphoto(False, img)
        

        # Get the screen's width and height
        screen_width = self.new_window.winfo_screenwidth()
        screen_height = self.new_window.winfo_screenheight()

        # Assuming the taskbar's height is 40 pixels (you may need to adjust this)
        taskbar_height = 50

        # Set the window's geometry to the screen's width and height, minus the taskbar's height
        self.new_window.geometry(f"{screen_width}x{screen_height - taskbar_height}")

        self.new_window.state('normal')  # Instead of 'zoomed', use 'normal' to allow the window to be resized
        self.new_window.resizable(0, 0)  # But then disable resizing
        self.new_window.update_idletasks()
        self.new_window.configure(bg='#003262')

        

        self.lgn_frame = tk.Frame(self.new_window, bg='#3B3C36', bd=5, height=220, width=1535)
        self.lgn_frame.place(x=0, y=0)

        # logo pic
        self.logoside = Image.open('ps2.png')
        self.logoside = self.logoside.resize((80, 80), resample=Image.LANCZOS)  # Resize the image to 50x50 pixels using Lanczos resampling
        logos = ImageTk.PhotoImage(self.logoside)
        self.logo_label = tk.Label(self.new_window, image=logos, width='80', height="80", bg='#3B3C36')
        self.logo_label.image = logos
        self.logo_label.__reduce__()
        self.logo_label.place(x=70, y=0)

        self.username_label = tk.Label(self.new_window, text=f"{username}: Signed in", bg='#3B3C36', fg="white")
        self.username_label.place(x=180, y=6)

        # logo pic
        self.logoside = Image.open('ChangeCurve2.png')
        # self.logoside = self.logoside.resize((80, 80), resample=Image.LANCZOS)  # Resize the image to 50x50 pixels using Lanczos resampling
        logos = ImageTk.PhotoImage(self.logoside)
        self.logo_label = tk.Label(self.new_window, image=logos, width='300', height="300", bg='#003262')
        self.logo_label.image = logos
        self.logo_label.__reduce__()
        self.logo_label.place(x=10, y=220)

        self.logoside = Image.open('ChangeCurve2.png')
        # self.logoside = self.logoside.resize((80, 80), resample=Image.LANCZOS)  # Resize the image to 50x50 pixels using Lanczos resampling
        logos = ImageTk.PhotoImage(self.logoside)
        self.logo_label = tk.Label(self.new_window, image=logos, width='300', height="300", bg='#003262')
        self.logo_label.image = logos
        self.logo_label.__reduce__()
        self.logo_label.place(x=1050, y=550)

        self.logoside = Image.open('images2.png')
        self.logoside = self.logoside.resize((80, 80), resample=Image.LANCZOS)  # Resize the image to 50x50 pixels using Lanczos resampling
        logos = ImageTk.PhotoImage(self.logoside)
        self.logo_label = tk.Label(self.lgn_frame, image=logos, width='300', height="300", bg='#3B3C36')
        self.logo_label.image = logos
        self.logo_label.__reduce__()
        self.logo_label.place(x=0, y=15)

        self.logoside = Image.open('images3.png')
        self.logoside = self.logoside.resize((80, 80), resample=Image.LANCZOS)  # Resize the image to 50x50 pixels using Lanczos resampling
        logos = ImageTk.PhotoImage(self.logoside)
        self.logo_label = tk.Label(self.lgn_frame, image=logos, width='300', height="300", bg='#3B3C36')
        self.logo_label.image = logos
        self.logo_label.__reduce__()
        self.logo_label.place(x=1200, y=15)

    



        label1 = tk.Label(self.lgn_frame, text=f"Welcome {username}, to our simple and easy to use bank app!", font=('yu gothic ui', 16, 'bold'), bg='#6CB4EE', fg='white')
        label = tk.Label(self.lgn_frame, text=f"Welcome {username}, to our simple and easy to use bank app!", font=('yu gothic ui', 16, 'bold'), bg='#0095B6', fg='white')
        label1.place(x=900, y=36)
        self.lgn_frame.after(2000, label1.place_forget)
        self.lgn_frame.after(2000, lambda: label.place(x=900, y=36))
        self.lgn_frame.after(3000, label.place_forget)
        self.lgn_frame.after(3000, lambda: label1.place(x=900, y=36))
        self.lgn_frame.after(4000, label1.place_forget)
        self.lgn_frame.after(4000, lambda: label.place(x=900, y=36))
        self.lgn_frame.after(5000, label.place_forget)
        self.lgn_frame.after(5000, lambda: label1.place(x=900, y=36))
        self.lgn_frame.after(6000, label1.place_forget)

        

        style = ttk.Style()
        style.configure("Big.TButton", font=("Arial", 17), foreground="#013220", background="black")

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

        # Open the image file
        image = Image.open("drop.png")
        # Resize the image
        image = image.resize((40, 40), resample=Image.LANCZOS)  # Replace (20, 20) with your desired size
        # Convert the image to a PhotoImage
        dropdown_image = ImageTk.PhotoImage(image)
        self.sidebar_button = tk.Button(self.lgn_frame, image=dropdown_image, compound="top", font=("yu gothic ui", 4, "bold"), width=70, bd=0, bg='#003262', cursor='hand2', activebackground='#3B3C36', fg='white', command=self.toggle_sidebar)
        self.sidebar_button.image = dropdown_image
        self.sidebar_button.place(x=10, y=0)

        # logo pic
        self.logoside = Image.open('vector.png')
        self.logoside = self.logoside.resize((350, 350), resample=Image.LANCZOS)  # Resize the image to 50x50 pixels using Lanczos resampling
        logos = ImageTk.PhotoImage(self.logoside)
        self.logo_label = tk.Label(self.new_window, image=logos, bg='#003262')
        self.logo_label.image = logos
        self.logo_label.__reduce__()
        self.logo_label.place(x=25, y=520)

        self.settings = tk.StringVar()
        self.settings.set("Settings")  # default value

        self.sidebar_menu = ttk.OptionMenu(self.lgn_frame, self.settings, "Settings", "Edit Account Details", command=self.toggle_sidebar)
        self.sidebar_menu.place(x=1400, y=10)

        self.sidebar = None

        # self.username = self.username  # Dummy username; replace with the actual logged-in user's username.
        self.session_transactions = []  # Initialize to track transactions during the session

        self.setup_ui()
        self.bankHistory.place_forget()
        self.bankHistory1 = tk.Frame(self.new_window, bg='#6CB4EE', width='700', height="350")
        self.bankHistory1.place(x=310, y=300)

        self.txt = "Transaction history"
        self.heading = tk.Label(self.bankHistory1, text=self.txt, font=('yu gothic ui', 35, 'bold'), bg='#6CB4EE', fg='white')
        self.heading.place(x="0", y="7")


    def center_window(self):
        # Center the window on the screen
        self.update_idletasks()
        width = self.winfo_width()
        height = self.winfo_height()
        x = (self.winfo_screenwidth() // 2) - (width // 2)
        y = (self.winfo_screenheight() // 2) - (height // 2)
        self.geometry(f'{width}x{height}+{x}+{y}')




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
            style.configure("Big.TLabel", font=("Arial", 15), foreground="#0095B6", background="brown")

            # Create a Label to display the account balance
            self.balance_label = ttk.Label(self.lgn_frame, text=f"Account Balance ₦: {account_balance}", style="Big.TLabel", width="23")
            self.balance_label.place(x=320, y=160)
        else:
            self.balance_label.place_forget()
            self.balance_label = None

    def toggle_balance1(self):
        if self.bankHistory is None:
            self.setup_ui()
            self.load_transaction_history()
            # self.bankHistory.place_forget()

            
            
        else:
            self.bankHistory.place_forget()
            
            self.bankHistory = None
            # self.lgn_frame.after(5000, label.destroy)





    def setup_ui(self):
        # Bank History Frame
        self.bankHistory = tk.Frame(self.new_window, bg='#6CB4EE', width='700', height="350")
        self.bankHistory.place(x=310, y=300)
        

        self.txt = "Transaction History"
        self.heading = tk.Label(self.bankHistory, text=self.txt, font=('yu gothic ui', 35, 'bold'), bg='#6CB4EE', fg='white')
        self.heading.pack(anchor="w", pady=10)

        # Treeview for displaying transaction history
        self.history_tree = ttk.Treeview(self.bankHistory, columns=("Date", "Type", "Amount", "Balance", "Recipient Account", "Recipient Name"), show="headings", height=10)
        self.history_tree.heading("Date", text="Date")
        self.history_tree.heading("Type", text="Type")
        self.history_tree.heading("Amount", text="Amount (₦)")
        self.history_tree.heading("Balance", text="Balance (₦)")
        self.history_tree.heading("Recipient Account", text="Recipient Account")
        self.history_tree.heading("Recipient Name", text="Recipient Name")

        self.history_tree.column("Date", width=120)
        self.history_tree.column("Type", width=100)
        self.history_tree.column("Amount", width=100)
        self.history_tree.column("Balance", width=100)
        self.history_tree.column("Recipient Account", width=120)
        self.history_tree.column("Recipient Name", width=130)

        self.history_tree.pack(fill="both", expand=True)

        self.buttonHistory = tk.Button(self.new_window, text="Show history",bg='#0095B6', width="15", command=self.toggle_balance1)
        self.buttonHistory.place(x=895, y=670)
        

        # # Beneficiaries Frame
        # self.beneficiaries_frame = tk.Frame(self.new_window, bg='#0095B6', width='300', height="350")
        # self.beneficiaries_frame.place(x=1040, y=300)

        # # Label for Beneficiaries
        # self.bene_label = tk.Label(self.beneficiaries_frame, text="Beneficiaries", font=('yu gothic ui', 20, 'bold'), bg='#0095B6', fg='white')
        # self.bene_label.pack(anchor='w', pady=10)

        # # Treeview for displaying beneficiaries
        # self.bene_tree = ttk.Treeview(self.beneficiaries_frame, columns=("Name", "Account"), show="headings", height=10)
        # self.bene_tree.heading("Name", text="Name")
        # self.bene_tree.heading("Account", text="Account Number")

        # self.bene_tree.column("Name", width=150)
        # self.bene_tree.column("Account", width=150)

        # self.bene_tree.pack(fill="both", expand=True)

        self.load_transaction_history()

        # Load initial beneficiaries
        # self.load_beneficiaries()

    

    def load_beneficiaries(self):
        # Clear existing entries
        for item in self.bene_tree.get_children():
            self.bene_tree.delete(item)

        # Connect to MySQL database to fetch beneficiaries
        db = mysql.connector.connect(
            host="localhost",
            user="tele",
            password="telesql19",
            database="new_database"
        )
        cursor = db.cursor()

        try:
            cursor.execute("SELECT name, account_number FROM beneficiaries WHERE username = %s", (self.username,))
            beneficiaries = cursor.fetchall()

            if not beneficiaries:
                self.bene_tree.insert("", tk.END, values=("No beneficiaries found.", ""))
                return

            for beneficiary in beneficiaries:
                self.bene_tree.insert("", tk.END, values=beneficiary)

                # Add quick transfer button
                self.bene_tree.bind("<Double-1>", lambda event, item=beneficiary: self.quick_transfer_dialog(item))

        except mysql.connector.Error as err:
            messagebox.showerror("Database Error", f"Error: {err}")
        finally:
            cursor.close()
            db.close()

    def quick_transfer_dialog(self, beneficiary):
        name, account_number = beneficiary
        quick_transfer_dialog = tk.Toplevel(self.new_window)
        quick_transfer_dialog.title(f"Quick Transfer to {name}")

        tk.Label(quick_transfer_dialog, text=f"Account: {account_number}").pack()

        tk.Label(quick_transfer_dialog, text="Amount to Transfer ₦ :").pack()
        amount_entry = tk.Entry(quick_transfer_dialog)
        amount_entry.pack()

        tk.Label(quick_transfer_dialog, text="Transaction PIN:").pack()
        pin_entry = tk.Entry(quick_transfer_dialog, show="*")
        pin_entry.pack()

        def quick_transfer_callback():
            try:
                amount = int(amount_entry.get())
            except ValueError:
                messagebox.showerror("Error", "Invalid amount. Please enter a numeric value.")
                return
            transaction_pin = pin_entry.get()

            self.transfer_money(self.username, account_number, amount, transaction_pin)
            quick_transfer_dialog.destroy()

        quick_transfer_button = tk.Button(quick_transfer_dialog, text="Transfer", command=quick_transfer_callback)
        quick_transfer_button.pack()

        # Bind Enter key to simulate clicking the Transfer button
        pin_entry.bind("<Return>", lambda event: quick_transfer_button.invoke())

    






    

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

            # Prevent transferring to own account
            if sender_account == recipient_account:
                messagebox.showerror("Error", "You cannot transfer money to your own account.")
                return

            # Fetch recipient's details
            cursor.execute("SELECT account_balance, account_name FROM users WHERE account_number = %s", (recipient_account,))
            recipient = cursor.fetchone()
            if not recipient:
                messagebox.showerror("Error", "Recipient account not found.")
                return

            recipient_balance, recipient_name = recipient

            # Ensure sufficient balance
            if sender_balance < amount:
                messagebox.showerror("Error", "Insufficient balance.")
                return

            # Update balances
            new_sender_balance = sender_balance - amount
            new_recipient_balance = recipient_balance + amount

            cursor.execute("UPDATE users SET account_balance = %s WHERE account_number = %s", (new_sender_balance, sender_account))
            cursor.execute("UPDATE users SET account_balance = %s WHERE account_number = %s", (new_recipient_balance, recipient_account))
            db.commit()

            

            messagebox.showinfo("Success", "Transfer completed successfully!")

            # Log the transaction
            now = datetime.now()
            cursor.execute(
                "INSERT INTO transactions (username, date, trans_type, amount, balance, recipient_account, recipient_name) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                (sender_username, now, 'Transfer', amount, new_sender_balance, recipient_account, recipient_name)
            )
            db.commit()

            # Update transaction history
            self.load_transaction_history()

        except mysql.connector.Error as err:
            messagebox.showerror("Database Error", f"Error: {err}")
        finally:
            cursor.close()
            db.close()


    def update_transaction_history(self):
        # Clear the existing content
        # for item in self.history_tree.get_children():
        #     self.history_tree.delete(item)

        # Display session transactions
        for transaction in self.session_transactions:
            self.history_tree.insert("", tk.END, values=transaction)

    def load_transaction_history(self):
        # Clear existing entries
        # self.history_tree.insert("", tk.END, values=transaction)
        for item in self.history_tree.get_children():
            self.history_tree.delete(item)

        # Connect to MySQL database to fetch transactions
        db = mysql.connector.connect(
            host="localhost",
            user="tele",
            password="telesql19",
            database="new_database"
        )
        cursor = db.cursor()

        try:
            cursor.execute("SELECT date, trans_type, amount, balance, recipient_account, recipient_name FROM transactions WHERE username = %s ORDER BY date DESC", (self.username,))
            transactions = cursor.fetchall()

            if not transactions:
                self.history_tree.insert("", tk.END, values=("No transaction history found.", "", "", "", "", ""))
                return

            for transaction in transactions:
                self.history_tree.insert("", tk.END, values=transaction)

        except mysql.connector.Error as err:
            messagebox.showerror("Database Error", f"Error: {err}")
        finally:
            cursor.close()
            db.close()


    
    

    def print_receipt(self, transaction):
        receipt_dialog = tk.Toplevel(self.new_window)
        receipt_dialog.title("Transaction Receipt")

        date, trans_type, amount, balance, recipient_account, recipient_name = transaction

        receipt_text = f"""
        Transaction Receipt
        ===============================
        Date           : {date}
        Type           : {trans_type}
        Amount         : ₦ {amount}
        Balance        : ₦ {balance}
        Recipient Acc. : {recipient_account}
        Recipient Name : {recipient_name}
        ===============================
        """
        tk.Label(receipt_dialog, text=receipt_text, justify="left", font=("Arial", 12)).pack(padx=10, pady=10)

        tk.Button(receipt_dialog, text="Close", command=receipt_dialog.destroy).pack(pady=5)




    def show_transfer_dialog(self):
        transfer_dialog = tk.Toplevel(self.new_window)
        transfer_dialog.title("Transfer Money")
        transfer_dialog.grab_set()

        # Set size of the fund account dialog
        dialog_width = 400
        dialog_height = 300

        # Center the dialog relative to the parent window (self.new_window)
        parent_x = self.new_window.winfo_x()
        parent_y = self.new_window.winfo_y()
        parent_width = self.new_window.winfo_width()
        parent_height = self.new_window.winfo_height()

        # Calculate the position
        x = parent_x + (parent_width // 2) - (dialog_width // 2)
        y = parent_y + (parent_height // 2) - (dialog_height // 2)

        transfer_dialog.geometry(f"{dialog_width}x{dialog_height}+{x}+{y}")


        tk.Label(transfer_dialog, text="Recipient Account Number:").pack()
        recipient_entry = tk.Entry(transfer_dialog)
        recipient_entry.pack()

        name_label = tk.Label(transfer_dialog, text="Account Name: ")
        name_label.pack()
        

        # Update the name label dynamically as the user enters the account number
        def on_recipient_change(*args):
            recipient_account = recipient_entry.get()
            if recipient_account:
                account_name = self.get_account_name_by_account_number(recipient_account)
                if account_name:
                    name_label.config(text=f"Account Name: {account_name}")
                else:
                    name_label.config(text="Account Name: Not Found")
            else:
                name_label.config(text="Account Name: ")

        recipient_entry.bind("<KeyRelease>", on_recipient_change)

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

            transaction = self.transfer_money(self.username, recipient_account, amount, transaction_pin)
            
            transfer_dialog.destroy()

            
            self.print_receipt(transaction)
                


        transfer_button = tk.Button(transfer_dialog, text="Transfer", command=transfer_callback)
        transfer_button.pack()

        def focus_password_entry6(self, event=None):
            amount_entry.focus()

        # Bind the Enter key to focus on the password entry field
        recipient_entry.bind("<Return>", lambda event: focus_password_entry6(self))

        def focus_password_entry3(self, event=None):
            pin_entry.focus()

        # Bind the Enter key to focus on the password entry field
        amount_entry.bind("<Return>", lambda event: focus_password_entry3(self))

        # Bind Enter key to simulate clicking the Transfer button
        pin_entry.bind("<Return>", lambda event: transfer_button.invoke())
    

    def get_account_name_by_account_number(self, account_number):
        db = mysql.connector.connect(
            host="localhost",
            user="tele",
            password="telesql19",
            database="new_database"
        )
        cursor = db.cursor()

        try:
            cursor.execute("SELECT account_name FROM users WHERE account_number = %s", (account_number,))
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








    def show_add_beneficiary_dialog(self):
        add_beneficiary_dialog = tk.Toplevel(self.new_window)
        add_beneficiary_dialog.title("Add Beneficiary")

        tk.Label(add_beneficiary_dialog, text="Beneficiary Name:").pack()
        name_entry = tk.Entry(add_beneficiary_dialog)
        name_entry.pack()

        tk.Label(add_beneficiary_dialog, text="Beneficiary Account Number:").pack()
        account_entry = tk.Entry(add_beneficiary_dialog)
        account_entry.pack()

        def add_beneficiary_callback():
            name = name_entry.get()
            account_number = account_entry.get()

            if not name or not account_number:
                messagebox.showerror("Error", "Both name and account number are required.")
                return

            # Connect to MySQL database to add beneficiary
            db = mysql.connector.connect(
                host="localhost",
                user="tele",
                password="telesql19",
                database="new_database"
            )
            cursor = db.cursor()

            try:
                cursor.execute("INSERT INTO beneficiaries (username, name, account_number) VALUES (%s, %s, %s)",
                               (self.username, name, account_number))
                db.commit()
                messagebox.showinfo("Success", "Beneficiary added successfully!")
                self.load_beneficiaries()
                add_beneficiary_dialog.destroy()

            except mysql.connector.Error as err:
                messagebox.showerror("Database Error", f"Error: {err}")
            finally:
                cursor.close()
                db.close()

        add_button = tk.Button(add_beneficiary_dialog, text="Add", command=add_beneficiary_callback)
        add_button.pack()

        # Bind Enter key to simulate clicking the Add button
        account_entry.bind("<Return>", lambda event: add_button.invoke())





    



    







    def show_fund_account_dialog(self):
        fund_account_dialog = tk.Toplevel(self.new_window)
        fund_account_dialog.title("Fund Your Account")
        fund_account_dialog.grab_set()

        # Set size of the fund account dialog
        dialog_width = 400
        dialog_height = 300

        # Center the dialog relative to the parent window (self.new_window)
        parent_x = self.new_window.winfo_x()
        parent_y = self.new_window.winfo_y()
        parent_width = self.new_window.winfo_width()
        parent_height = self.new_window.winfo_height()

        # Calculate the position
        x = parent_x + (parent_width // 2) - (dialog_width // 2)
        y = parent_y + (parent_height // 2) - (dialog_height // 2)

        fund_account_dialog.geometry(f"{dialog_width}x{dialog_height}+{x}+{y}")

        tk.Label(fund_account_dialog, text="Other Account Number:").pack()
        other_account_entry = tk.Entry(fund_account_dialog)
        other_account_entry.pack()

        tk.Label(fund_account_dialog, text="Other Username:").pack()
        other_username_entry = tk.Entry(fund_account_dialog)
        other_username_entry.pack()

        tk.Label(fund_account_dialog, text="Account BVN:").pack()
        other_bvn_entry = tk.Entry(fund_account_dialog)
        other_bvn_entry.pack()

        tk.Label(fund_account_dialog, text="Account Password:").pack()
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

            # Prevent transferring to own account if desired
            if other_account_number == current_account_number:
                messagebox.showerror("Error", "You cannot transfer money to your own account.")
                return

            # Update balances
            new_other_balance = other_balance - amount
            new_current_balance = current_balance + amount

            cursor.execute("UPDATE users SET account_balance = %s WHERE account_number = %s", (new_other_balance, other_account_number))
            cursor.execute("UPDATE users SET account_balance = %s WHERE account_number = %s", (new_current_balance, current_account_number))
            db.commit()

            messagebox.showinfo("Success", "Funds transferred successfully!")

            # Update balance display if visible
            if hasattr(self, 'balance_label') and self.balance_label:
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
        self.master.username_entry.delete(0, tk.END)
        self.master.username_entry.insert(0, "Enter your username here...")
        self.master.password_entry.delete(0, tk.END)
        self.master.password_entry.insert(0, "Enter your password here...")
        self.master.username_entry.bind("<FocusIn>", self.clear_on_focus)
        self.master.password_entry.bind("<FocusIn>", self.clear_on_focus)


    def clear_on_focus(self, event):
        event.widget.delete(0, tk.END)

# root = tk.Tk()
# welcome_window = WelcomeWindow(root, "username")
# root.withdraw()  # Hide the root window
# welcome_window.new_window.mainloop()