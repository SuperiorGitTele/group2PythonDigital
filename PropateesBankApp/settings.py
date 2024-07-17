import tkinter as tk
from tkinter import messagebox
import mysql.connector
from PIL import Image, ImageTk

class Settingfunction:
    def __init__(self, master, username):
        self.master = master
        self.username = username
        self.settings = tk.Toplevel(self.master)
        self.settings.title("Settings")
        img = ImageTk.PhotoImage(file='logo.png')
        self.settings.iconphoto(False, img)
        self.settings.configure(bg="#003362")  

        dialog_width = 400
        dialog_height = 400

        # Center the dialog relative to the parent window (self.new_window)
        parent_x = self.master.winfo_x()
        parent_y = self.master.winfo_y()
        parent_width = self.master.winfo_width()
        parent_height = self.master.winfo_height()

        # Calculate the position
        x = parent_x + (parent_width // 2) - (dialog_width // 2)
        y = parent_y + (parent_height // 2) - (dialog_height // 2)

        self.settings.geometry(f"{dialog_width}x{dialog_height}+{x}+{y}")

        self.settings.geometry("400x400")
        self.settings.grab_set()

        
        tk.Label(self.settings, text="Username:", bg="#003362", fg="white").grid(row=0, column=0, padx=10, pady=10)
        entry_username = tk.Label(self.settings, text=f"{username}", bg="#003362", fg="white")
        entry_username.grid(row=0, column=1, padx=10, pady=10)

        tk.Button(self.settings, text="Delete Transaction History", bg='#0095B6',command=lambda: self.delete_transaction_history(entry_username.get())).grid(row=1, column=0, columnspan=2, pady=10)

        tk.Label(self.settings, text="Beneficiary Account Number:", bg="#003362", fg="white").grid(row=2, column=0, padx=10, pady=10)
        entry_account_number = tk.Entry(self.settings)
        entry_account_number.grid(row=2, column=1, padx=10, pady=10)
        tk.Button(self.settings, text="Delete Beneficiary", bg='#0095B6',command=lambda: self.delete_beneficiary(entry_username.get(), entry_account_number.get())).grid(row=3, column=0, columnspan=2, pady=10)

        tk.Label(self.settings, text="New Security Question:", bg="#003362", fg="white").grid(row=4, column=0, padx=10, pady=10)
        entry_new_question = tk.Entry(self.settings)
        entry_new_question.grid(row=4, column=1, padx=10, pady=10)

        tk.Label(self.settings, text="New Answer:", bg="#003362", fg="white").grid(row=5, column=0, padx=10, pady=10)
        entry_new_answer = tk.Entry(self.settings)
        entry_new_answer.grid(row=5, column=1, padx=10, pady=10)

        tk.Button(self.settings, text="Change Security Question", bg='#0095B6',command=lambda: self.change_security_question(entry_username.get(), entry_new_question.get(), entry_new_answer.get())).grid(row=6, column=0, columnspan=2, pady=10)



        # Database connection
        try:
            self.connection = mysql.connector.connect(
                host='127.0.0.1',  
                user='Bank', 
                password='Bankappsql', 
                database='Bank_data' 
            )
            self.cursor = self.connection.cursor()
            print("Database connection successful.")
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            messagebox.showerror("Database Connection Error", f"Error: {err}")
            self.settings.destroy()
            return

        

    def delete_transaction_history(self, username):
        try:
            print(f"Deleting transaction history for {username}")
            self.cursor.execute("DELETE FROM Bank_data.transactions WHERE username = %s", (username,))
            self.connection.commit()
            messagebox.showinfo("Success", "Transaction history deleted successfully.")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

    def delete_beneficiary(self, username, account_number):
        try:
            print(f"Deleting beneficiary {account_number} for {username}")
            self.cursor.execute("DELETE FROM Bank_data.beneficiaries WHERE username = %s AND account_number = %s", (username, account_number))
            self.connection.commit()
            messagebox.showinfo("Success", "Beneficiary deleted successfully.")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

    def change_security_question(self, username, new_question, new_answer):
        try:
            print(f"Changing security question for {username}")
            self.cursor.execute("UPDATE Bank_data.users SET secret_question = %s, secret_answer = %s WHERE username = %s", (new_question, new_answer, username))
            self.connection.commit()
            messagebox.showinfo("Success", "Security question changed successfully.")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

    