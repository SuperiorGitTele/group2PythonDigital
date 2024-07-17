import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk
import mysql.connector
from decimal import Decimal

class SubscripWindow:
    def __init__(self, master, username):
        self.master = master
        self.sub_window = tk.Toplevel(self.master)
        self.username = username
        self.sub_window.title("Subscription Service")
        self.sub_window.configure(bg='#003262')
        self.sub_window.grab_set()

        dialog_width = 400
        dialog_height = 250

        # Center the dialog relative to the parent window (self.new_window)
        parent_x = self.master.winfo_x()
        parent_y = self.master.winfo_y()
        parent_width = self.master.winfo_width()
        parent_height = self.master.winfo_height()

        # Calculate the position
        x = parent_x + (parent_width // 2) - (dialog_width // 2)
        y = parent_y + (parent_height // 2) - (dialog_height // 2)

        self.sub_window.geometry(f"{dialog_width}x{dialog_height}+{x}+{y}")

        # Adjust main window size
        self.sub_window.geometry("500x300")

        img = ImageTk.PhotoImage(file='logo.png')
        self.sub_window.iconphoto(False, img)

        # Frame for buttons to place them on the same line
        button_frame = tk.Frame(self.sub_window, bg='#003262')
        button_frame.pack(pady=50)

        # Subscription options with increased button size
        tk.Button(button_frame, text=f"Buy Airtime", command=lambda: self.new_window("Airtime"), width=20, height=2).grid(row=0, column=0, padx=10)
        tk.Button(button_frame, text="Buy Data", command=lambda: self.new_window("Data"), width=20, height=2).grid(row=0, column=1, padx=10)

    def new_window(self, subscription_type):
        new_win = tk.Toplevel(self.sub_window)
        new_win.title(f"Buy {subscription_type}")
        new_win.configure(bg='#003262')
        new_win.grab_set()
        img = ImageTk.PhotoImage(file='logo.png')
        new_win.iconphoto(False, img)

        dialog_width = 400
        dialog_height = 300

        # Center the dialog relative to the parent window (self.new_window)
        parent_x = self.master.winfo_x()
        parent_y = self.master.winfo_y()
        parent_width = self.master.winfo_width()
        parent_height = self.master.winfo_height()

        # Calculate the position
        x = parent_x + (parent_width // 2) - (dialog_width // 2)
        y = parent_y + (parent_height // 2) - (dialog_height // 2)

        new_win.geometry(f"{dialog_width}x{dialog_height}+{x}+{y}")

        tk.Label(new_win, text=f"Enter your phone number to buy {subscription_type}", bg='#003262', fg='white').pack(padx=10, pady=10)
        self.phone_var = tk.StringVar()
        tk.Entry(new_win, textvariable=self.phone_var).pack(padx=10, pady=10)

        tk.Label(new_win, text="Enter the amount", bg='#003262', fg='white').pack(padx=10, pady=10)
        self.amount_var = tk.StringVar()
        tk.Entry(new_win, textvariable=self.amount_var).pack(padx=10, pady=10)

        tk.Button(new_win, text="Submit", command=lambda: self.submit(new_win, subscription_type)).pack(pady=10)

    def submit(self, window, subscription_type):
        phone_number = self.phone_var.get()
        amount = self.amount_var.get()

        if not phone_number:
            messagebox.showwarning("Input Error", "Please enter your phone number.")
            return

        if not amount:
            messagebox.showwarning("Input Error", "Please enter the amount.")
            return

        try:
            amount = Decimal(amount)  # Convert to Decimal
        except ValueError:
            messagebox.showwarning("Input Error", "Please enter a valid amount.")
            return

        # Deduct amount from account balance
        if self.deduct_amount_from_balance(amount):
            messagebox.showinfo("Success", f"{amount}₦ has been deducted from your account for {subscription_type}.")
            window.destroy()
        else:
            messagebox.showerror("Error", "Failed to deduct the amount. Please try again.")

    def deduct_amount_from_balance(self, amount):
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
            # Get current balance
            cursor.execute("SELECT account_balance FROM users WHERE username = %s", (self.username,))
            row = cursor.fetchone()

            if row:
                current_balance = row[0]
                if current_balance >= amount:
                    new_balance = current_balance - amount

                    # Update balance in database
                    cursor.execute("UPDATE users SET account_balance = %s WHERE username = %s", (new_balance, self.username))
                    db.commit()
                    return True
                else:
                    messagebox.showwarning("Insufficient Funds", "You do not have enough funds for this transaction.")
                    return False
            else:
                messagebox.showerror("Error", "Failed to retrieve account balance.")
                return False
        except mysql.connector.Error as err:
            messagebox.showerror("Database Error", f"Error: {err}")
            return False
        finally:
            cursor.close()
            db.close()


        

    def show_receipt(self, subscription_type, phone_number, amount):
        receipt_win = tk.Toplevel(self.sub_window)
        receipt_win.title("Receipt")
        receipt_win.configure(bg='#003262')
        img = ImageTk.PhotoImage(file='logo.png')
        receipt_win.iconphoto(False, img)
        receipt_win.grab_set()

        dialog_width = 400
        dialog_height = 300

        # Center the dialog relative to the parent window (self.new_window)
        parent_x = self.master.winfo_x()
        parent_y = self.master.winfo_y()
        parent_width = self.master.winfo_width()
        parent_height = self.master.winfo_height()

        # Calculate the position
        x = parent_x + (parent_width // 2) - (dialog_width // 2)
        y = parent_y + (parent_height // 2) - (dialog_height // 2)

        receipt_win.geometry(f"{dialog_width}x{dialog_height}+{x}+{y}")

        # Adjust receipt window size
        receipt_win.geometry("400x300")

        receipt_text = (
            f"Receipt\n\n"
            f"Subscription Type: {subscription_type}\n"
            f"Phone Number: {phone_number}\n"
            f"Amount: {amount}\n"
        )

        tk.Label(receipt_win, text=receipt_text, font=("Helvetica", 12), bg='#003262', fg='white').pack(padx=20, pady=20)
        tk.Button(receipt_win, text="Close", command=receipt_win.destroy).pack(pady=10)
