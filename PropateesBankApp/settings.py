import tkinter as tk
from tkinter import messagebox
import mysql.connector

class Settingfunction:
    def __init__(self, master, username):
        settings = settings
        self.master = master
        self.username = username
        self.settings = tk.Toplevel(self.master)
        self.settings.title("Bank App")
        self.settings.configure(bg="#003362")  
        self.settings.geometry("200x200")
        self.settings.grab_set()



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

        # Button to open settings window
        tk.Button(self.settings, text="Settings", command=self.create_settings_window).pack(pady=20)

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

    def create_settings_window(self):
        settings_window = tk.Toplevel(self.settings)
        settings_window.title("Settings")
        settings_window.configure(bg="#003362") 
        settings_window.geometry("400x350")

        tk.Label(settings_window, text="Username:", bg="#003362", fg="white").grid(row=0, column=0, padx=10, pady=10)
        entry_username = tk.Entry(settings_window)
        entry_username.grid(row=0, column=1, padx=10, pady=10)

        tk.Button(settings_window, text="Delete Transaction History", command=lambda: self.delete_transaction_history(entry_username.get())).grid(row=1, column=0, columnspan=2, pady=10)

        tk.Label(settings_window, text="Beneficiary Account Number:", bg="#003362", fg="white").grid(row=2, column=0, padx=10, pady=10)
        entry_account_number = tk.Entry(settings_window)
        entry_account_number.grid(row=2, column=1, padx=10, pady=10)
        tk.Button(settings_window, text="Delete Beneficiary", command=lambda: self.delete_beneficiary(entry_username.get(), entry_account_number.get())).grid(row=3, column=0, columnspan=2, pady=10)

        tk.Label(settings_window, text="New Security Question:", bg="#003362", fg="white").grid(row=4, column=0, padx=10, pady=10)
        entry_new_question = tk.Entry(settings_window)
        entry_new_question.grid(row=4, column=1, padx=10, pady=10)

        tk.Label(settings_window, text="New Answer:", bg="#003362", fg="white").grid(row=5, column=0, padx=10, pady=10)
        entry_new_answer = tk.Entry(settings_window)
        entry_new_answer.grid(row=5, column=1, padx=10, pady=10)

        tk.Button(settings_window, text="Change Security Question", command=lambda: self.change_security_question(entry_username.get(), entry_new_question.get(), entry_new_answer.get())).grid(row=6, column=0, columnspan=2, pady=10)

if __name__ == "__main__":
    settings = tk.Tk()
    app = Settingfunction(settings)
    settings.mainloop()
