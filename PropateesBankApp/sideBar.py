import tkinter as tk
from PIL import Image, ImageTk
from tkinter import ttk, filedialog
import os
import mysql.connector
from tkinter import messagebox
import tkinter as tk
import smtplib
import subprocess
import time
import re
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import datetime
import requests

class Sidebar(tk.Frame):
    def __init__(self, master, username,**kwargs):
        tk.Frame.__init__(self, master, **kwargs)
        self.master = master
        self.username = username
        self.is_open = False
        self.image_path = None
        self.load_image_path()
        self.configure(bg="#3B3C36")


        # Open the image file
        image = Image.open("bar12.png")
        image = image.resize((40, 40), resample=Image.LANCZOS)
        dropdown_image = ImageTk.PhotoImage(image)
        self.sidebar_button = tk.Button(self, image=dropdown_image, compound="top", font=("yu gothic ui", 4, "bold"), width=70, bd=0, bg='#3B3C36', cursor='hand2', activebackground='#3B3C36', fg='white', command=self.close_sidebar)
        self.sidebar_button.image = dropdown_image
        self.sidebar_button.place(x=10, y=0)

        self.logo_label3 = tk.Label(self, bg='#3B3C36')
        self.logo_label3.place(x=70, y=85)

        self.load_image_from_path3()
        
        

        self.username_label = tk.Label(self, text=f"{username}: Signed in", bg='#3B3C36', fg="white")
        self.username_label.place(x=70, y=180)


        # Buttons
        self.button1 = tk.Button(self, text="Dashboard", font=('yu gothic ui', 13, 'bold'), width=20, bd=0, bg='#0095B6', cursor='hand2', activebackground='#3047ff', fg='white', command=self.dashboard)
        self.button1.place(x=20, y=250)

        self.button2 = tk.Button(self, text="Account Details", font=('yu gothic ui', 13, 'bold'), width=20, bd=0, bg='#0095B6', cursor='hand2', activebackground='#3047ff', fg='white', command=self.AcctDetail)
        self.button2.place(x=20, y=350)

        self.button3 = tk.Button(self, text="Settings", font=('yu gothic ui', 11, 'bold'), width=22, bd=0, bg='#0095B6', cursor='hand2', activebackground='#3047ff', fg='white', command=self.setting)
        self.button3.place(x=20, y=450)
    
    def load_image_from_path3(self):
            if self.image_path and os.path.exists(self.image_path):
                try:
                    image = Image.open(self.image_path)
                    image = image.resize((80, 80), resample=Image.LANCZOS)
                    self.logo = ImageTk.PhotoImage(image)
                    self.logo_label3.config(image=self.logo)
                except Exception as e:
                    print(f"Error loading image1: {e}")

    def load_image_path(self):
        # Load the image path from a file
        if os.path.exists('image_path.txt'):
            with open('image_path.txt', 'r') as f:
                self.image_path = f.read().strip()
        else:
            self.image_path = None

    def dashboard(self):
        dashboard = tk.Toplevel(self.master)
        dashboard.title("Dashboard")
        dashboard.configure(bg='#003262')
        img = ImageTk.PhotoImage(file='logo.png')
        dashboard.iconphoto(False, img)
        dashboard.grab_set()

        # Set size of the dashboard dialog
        dialog_width = 600
        dialog_height = 600

        # Center the dialog relative to the parent window (self.master)
        parent_x = self.master.winfo_x()
        parent_y = self.master.winfo_y()
        parent_width = self.master.winfo_width()
        parent_height = self.master.winfo_height()

        # Calculate the position
        x = parent_x + (parent_width // 2) - (dialog_width // 2)
        y = parent_y + (parent_height // 2) - (dialog_height // 2)

        dashboard.geometry(f"{dialog_width}x{dialog_height}+{x}+{y}")

        # Add welcome message
        tk.Label(dashboard, text="Welcome to Your Dashboard", bg="#003262", fg="white", font=('Arial', 20, 'bold')).place(x=110, y=20)

        

        # tk.Label(quick_actions_frame, text="Quick Actions", bg="#003262", fg="white", font=('Arial', 14, 'bold')).pack(anchor='w')
        # tk.Button(quick_actions_frame, text="Transfer Funds", font=('Arial', 12), bg='#0095B6', fg='white', cursor='hand2').pack(anchor='w', pady=5)
        # tk.Button(quick_actions_frame, text="Pay Bills", font=('Arial', 12), bg='#0095B6', fg='white', cursor='hand2').pack(anchor='w', pady=5)
        # tk.Button(quick_actions_frame, text="Deposit Checks", font=('Arial', 12), bg='#0095B6', fg='white', cursor='hand2').pack(anchor='w', pady=5)


        # label = tk.Label(activities, text="Text", bg="#0095B6", font=('Arial', 12))
        # label.place(x=50, y=50)
        self.username_label = tk.Label(dashboard, text=f"{self.username}", font=('yu gothic ui', 35, 'bold'),bg='#003262', fg="white")
        self.username_label.place(x=135, y=70)

        account_balance = self.get_account_balance(self.username)  
        style = ttk.Style()
        style.configure("Big.TLabel", font=("Arial", 15), foreground="#003262", background="#0095B6")
        # Label to display the account balance
        self.balance_label = ttk.Label(dashboard, text=f"Account Balance ₦: {account_balance}", style="Big.TLabel", width="24")
        self.balance_label.place(x=130, y=160)

        tk.Label(dashboard, text="Activities", bg="#003262", fg="white", font=('Arial', 14, 'bold')).place(x=40, y=190)
        
        


        tk.Label(dashboard, text="Quick Actions", bg="#003262", fg="white", font=('Arial', 14, 'bold')).place(x=40, y=500)
        tk.Button(dashboard, text="Transfer Funds", font=('Arial', 12), bg='#0095B6', fg='white', cursor='hand2').place(x=40, y=550)
        tk.Button(dashboard, text="Pay Bills(Soon!)", font=('Arial', 12), bg='#0095B6', fg='white', cursor='hand2').place(x=220, y=550)
        tk.Button(dashboard, text="Deposit Checks(Soon!)", font=('Arial', 12), bg='#0095B6', fg='white', cursor='hand2').place(x=400, y=550)

        self.logo_label = tk.Label(dashboard, bg='#003262')
        self.logo_label.place(x=40, y=70)

        def load_image_from_path():
            if self.image_path and os.path.exists(self.image_path):
                try:
                    image = Image.open(self.image_path)
                    image = image.resize((80, 80), resample=Image.LANCZOS)
                    self.logos = ImageTk.PhotoImage(image)
                    self.logo_label.config(image=self.logos)
                except Exception as e:
                    print(f"Error loading image: {e}")

        
            
        
        def upload_photo():
            file_path = filedialog.askopenfilename()
            if file_path:
                self.image_path = file_path
                # Save image path to a configuration file or database for persistence
                with open('image_path.txt', 'w') as f:
                    f.write(self.image_path)
                load_image_from_path()
                messagebox.showinfo("Photo change Successful", "Photo Change Successful!, full changes will take place when the app is reopened")

        def load_transaction_history():
            # Connect to MySQL database to fetch transactions
            db = mysql.connector.connect(
                host="localhost",
                user="Bank",
                password="Bankappsql",
                database="Bank_data",
                auth_plugin='mysql_native_password'
            )
            cursor = db.cursor()

            try:
                cursor.execute("SELECT amount FROM transactions WHERE username = %s", (self.username,))
                transactions = cursor.fetchall()

                # amount = transactions

                if not transactions:
                    recieved = tk.Label(dashboard, text="No Money Recieved", bg="#003262", fg="white", font=('Arial', 12))
                    recieved.place(x=40, y=260)

                    trans = tk.Label(dashboard, text="No Transactions", bg="#003262", fg="white", font=('Arial', 12))
                    trans.place(x=40, y=230)
                    return
                else:
                    trans = tk.Label(dashboard, text=f"Update coming soon", bg="#003262", fg="white", font=('Arial', 20))
                    trans.place(x=40, y=230)

            except mysql.connector.Error as err:
                messagebox.showerror("Database Error", f"Error: {err}")
            finally:
                cursor.close()
                db.close()
            
        upload_button = tk.Button(dashboard, text="Change Photo", command=upload_photo)
        upload_button.place(x=40, y=160)

        load_image_from_path()
        load_transaction_history()

 


    def AcctDetail(self):
        AcctDetail = tk.Toplevel(self.master)
        AcctDetail.title("Activities")
        AcctDetail.configure(bg='#0095B6')
        img = ImageTk.PhotoImage(file='logo.png')
        AcctDetail.iconphoto(False, img)
        AcctDetail.grab_set()

        # Set size of the fund account dialog
        dialog_width = 600
        dialog_height = 600

        # Center the dialog relative to the parent window (self.master)
        parent_x = self.master.winfo_x()
        parent_y = self.master.winfo_y()
        parent_width = self.master.winfo_width()
        parent_height = self.master.winfo_height()

        # Calculate the position
        x = parent_x + (parent_width // 2) - (dialog_width // 2)
        y = parent_y + (parent_height // 2) - (dialog_height // 2)

        AcctDetail.geometry(f"{dialog_width}x{dialog_height}+{x}+{y}")

    def setting(self):
        setting = tk.Toplevel(self.master)
        setting.title("Activities")
        setting.configure(bg='#003262')
        img = ImageTk.PhotoImage(file='logo.png')
        setting.iconphoto(False, img)
        setting.grab_set()

        # Set size of the fund account dialog
        dialog_width = 600
        dialog_height = 600

        # Center the dialog relative to the parent window (self.master)
        parent_x = self.master.winfo_x()
        parent_y = self.master.winfo_y()
        parent_width = self.master.winfo_width()
        parent_height = self.master.winfo_height()

        # Calculate the position
        x = parent_x + (parent_width // 2) - (dialog_width // 2)
        y = parent_y + (parent_height // 2) - (dialog_height // 2)

        setting.geometry(f"{dialog_width}x{dialog_height}+{x}+{y}")

    def get_account_balance(self, username):
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

    

    def transfer_money(self, sender_username, recipient_account, amount, transaction_pin):
        # Check Wi-Fi and Internet Speed
        def check_wifi_and_internet_speed():
            try:
                # Check Wi-Fi connection
                output = subprocess.check_output(["netsh", "wlan", "show", "interfaces"])
                output = output.decode("utf-8")
                ssid = None
                for line in output.split("\n"):
                    if "SSID" in line and "BSSID" not in line:
                        ssid = line.split(":")[1].strip()
                        break

                if not ssid:
                    return False

                # Perform a simple internet speed test
                start_time = time.time()
                response = requests.get("https://httpbin.org/bytes/1024", timeout=3)
                end_time = time.time()

                # Check if the response was successful and if the time taken is less than 3 seconds
                if response.status_code == 200 and (end_time - start_time) < 3:
                    return True
                else:
                    return False
            except (subprocess.CalledProcessError, requests.RequestException):
                return False

        # Verify Email Format
        def verify_email(email):
            # Basic regex for email validation
            email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
            return re.match(email_regex, email) is not None

        # Send Email Notification
        def send_email(to_email, subject, body):
            smtp_server = "smtp.gmail.com"
            smtp_port = 587
            from_email = "propateesbank@gmail.com"  # Replace with your email
            password = "proban24!"  # Replace with your app-specific password

            message = MIMEMultipart()
            message["From"] = from_email
            message["To"] = to_email
            message["Subject"] = subject
            message.attach(MIMEText(body, "plain"))

            try:
                server = smtplib.SMTP(smtp_server, smtp_port)
                server.starttls()
                server.login(from_email, password)
                server.sendmail(from_email, to_email, message.as_string())
                server.quit()
                print(f"Email sent to {to_email}")
            except Exception as e:
                print(f"Failed to send email to {to_email}: {e}")


        # Connect to the database
        db = mysql.connector.connect(
            host="localhost",
            user="Bank",
            password="Bankappsql",
            database="Bank_data",
            auth_plugin='mysql_native_password'
        )
        cursor = db.cursor()

        try:
            # Fetch sender's details
            cursor.execute("SELECT account_number, account_balance, transaction_pin, email FROM users WHERE username = %s", (sender_username,))
            sender = cursor.fetchone()
            if not sender:
                messagebox.showerror("Error", "Sender account not found.")
                return

            sender_account, sender_balance, stored_pin, sender_email = sender

            # Validate transaction PIN
            if transaction_pin != stored_pin:
                messagebox.showerror("Error", "Invalid transaction PIN.")
                return

            # Prevent transferring to own account
            if sender_account == recipient_account:
                messagebox.showerror("Error", "You cannot transfer money to your own account.")
                return

            # Fetch recipient's details
            cursor.execute("SELECT account_balance, account_name, email FROM users WHERE account_number = %s", (recipient_account,))
            recipient = cursor.fetchone()
            if not recipient:
                messagebox.showerror("Error", "Recipient account not found.")
                return

            recipient_balance, recipient_name, recipient_email = recipient

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

            # Log the transaction
            now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            cursor.execute(
                "INSERT INTO transactions (username, date, trans_type, amount, balance, recipient_account, recipient_name) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                (sender_username, now, 'Transfer', amount, new_sender_balance, recipient_account, recipient_name)
            )
            db.commit()

            # Get the transaction ID
            transaction_id = cursor.lastrowid

            # Fetch the transaction details
            cursor.execute("SELECT date, trans_type, amount, balance, recipient_account, recipient_name FROM transactions WHERE id = %s", (transaction_id,))
            transaction = cursor.fetchone()

            # Print the receipt
            self.print_receipt(transaction)

            # Update transaction history
            self.load_transaction_history()
            self.load_beneficiaries()

            # Send debit email notification
            if check_wifi_and_internet_speed() and sender_email and verify_email(sender_email):
                subject = "Debit Alert: Funds Transfer"
                body = f"""
                Dear {sender_username},

                You have successfully transferred ₦{amount:.2f} to account {recipient_account} ({recipient_name}).

                Transaction ID: {transaction_id}
                Date: {now}
                Remaining Balance: ₦{new_sender_balance:.2f}

                Thank you for using our service.

                Best regards,
                Your Bank Team
                """
                send_email(sender_email, subject, body)

            # Verify and send credit email notification
            if check_wifi_and_internet_speed() and recipient_email and verify_email(recipient_email):
                subject = "Credit Alert: Funds Received"
                body = f"""
                Dear {recipient_name},

                You have received ₦{amount:.2f} from {sender_username}.

                Transaction ID: {transaction_id}
                Date: {now}
                New Balance: ₦{new_recipient_balance:.2f}

                Thank you for using our service.

                Best regards,
                Your Bank Team
                """
                send_email(recipient_email, subject, body)

        except mysql.connector.Error as err:
            messagebox.showerror("Database Error", f"Error: {err}")
        finally:
            cursor.close()
            db.close()

    def show_transfer_dialog(self):
        transfer_dialog = tk.Toplevel(self.new_window)
        transfer_dialog.title("Transfer Money")
        transfer_dialog.configure(bg='#003262')
        img = ImageTk.PhotoImage(file='logo.png')
        transfer_dialog.iconphoto(False, img)
        transfer_dialog.grab_set()

        # Set size of the fund account dialog
        dialog_width = 400
        dialog_height = 250

        # Center the dialog relative to the parent window (self.new_window)
        parent_x = self.new_window.winfo_x()
        parent_y = self.new_window.winfo_y()
        parent_width = self.new_window.winfo_width()
        parent_height = self.new_window.winfo_height()

        # Calculate the position
        x = parent_x + (parent_width // 2) - (dialog_width // 2)
        y = parent_y + (parent_height // 2) - (dialog_height // 2)

        transfer_dialog.geometry(f"{dialog_width}x{dialog_height}+{x}+{y}")


        tk.Label(transfer_dialog, text="Recipient Account Number:", bg='#6CB4EE').pack()
        recipient_entry = tk.Entry(transfer_dialog)
        recipient_entry.pack()

        name_label = tk.Label(transfer_dialog, text="Account Name: ", bg='#6CB4EE')
        name_label.pack()

        

        # This update the name label dynamically as the user enters the account number
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

        

        tk.Label(transfer_dialog, text="Amount to Transfer ₦ :", bg='#6CB4EE').pack()
        amount_entry = tk.Entry(transfer_dialog)
        amount_entry.pack()

        tk.Label(transfer_dialog, text="Transaction PIN:", bg='#6CB4EE').pack()
        pin_entry = tk.Entry(transfer_dialog, show="*")
        pin_entry.pack()
        
        # Checkbox for adding recipient to beneficiaries
        add_beneficiary_var = tk.BooleanVar()
        add_beneficiary_checkbox = tk.Checkbutton(
            transfer_dialog, text="Add Recipient to Beneficiaries", bg='#6CB4EE', variable=add_beneficiary_var
        )
        add_beneficiary_checkbox.pack()

        def transfer_callback():
            recipient_account = recipient_entry.get()
            try:
                amount = int(amount_entry.get())
            except ValueError:
                messagebox.showerror("Error", "Invalid amount. Please enter a numeric value.")
                return
            transaction_pin = pin_entry.get()

            self.transfer_money(self.username, recipient_account, amount, transaction_pin)
            self.get_account_balance(self.username)

            if add_beneficiary_var.get():
                self.add_beneficiary(self.username, recipient_account)

            transfer_dialog.destroy()
        transfer_button = tk.Button(transfer_dialog, text="Transfer", bg='#0095B6', command=transfer_callback)
        transfer_button.pack()

        if amount_entry.focus() is True:
            on_recipient_change()

        def focus_password_entry6(self, event=None):
            amount_entry.focus()
            on_recipient_change()

        # Bind the Enter key to focus on the password entry field
        recipient_entry.bind("<Return>", lambda event: focus_password_entry6(self))

        def focus_password_entry3(self, event=None):
            pin_entry.focus()

        # Bind the Enter key to focus on the password entry field
        amount_entry.bind("<Return>", lambda event: focus_password_entry3(self))

        # Bind Enter key to simulate clicking the Transfer button
        pin_entry.bind("<Return>", lambda event: transfer_button.invoke())


    def toggle(self):
            self.animate_open()
            if self.is_open:
                self.is_open = True

    def close_sidebar(self):
        self.animate_close()

    def animate_open(self):
        # Animate the opening of the sidebar
        if self.winfo_x() > -self.winfo_width():
            self.place(x=self.winfo_x() - 20, y=0, relwidth=0.2, relheight=1)
            self.after(10, self.animate_open)
        else:
            self.place(x=0, y=0, relwidth=0.2, relheight=1)
            self.is_open = True

    def animate_close(self):
        # Animate the closing of the sidebar
        if self.winfo_x() < 0:
            self.place(x=self.winfo_x() + 20, y=0, relwidth=0.2, relheight=1)
            self.after(10, self.animate_close)
        else:
            self.place_forget()
            self.is_open = False

    

# Example usage
if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("1200x600")  # Set window size

    sidebar = Sidebar(root, username=None,bg='#3B3C36')
    sidebar.place(x=0, y=0, relwidth=0.2, relheight=1)  

    root.mainloop()
