import tkinter as tk
from PIL import Image, ImageTk
from tkinter import ttk, filedialog
import os
import mysql.connector
from tkinter import messagebox
import tkinter as tk


class Sidebar(tk.Frame):
    def __init__(self, master, username,**kwargs):
        tk.Frame.__init__(self, master, **kwargs)
        self.master = master
        self.username = username
        self.is_open = False
        self.image_path = None
        self.load_image_path()
        self.configure(bg="#555555")


        # Open the image file
        image = Image.open("barclose.png")
        image = image.resize((40, 40), resample=Image.LANCZOS)
        dropdown_image = ImageTk.PhotoImage(image)
        self.sidebar_button = tk.Button(self, image=dropdown_image, compound="top", font=("yu gothic ui", 4, "bold"), width=70, bd=0, bg='#3B3C36', cursor='hand2', activebackground='#3B3C36', fg='white', command=self.close_sidebar)
        self.sidebar_button.image = dropdown_image
        self.sidebar_button.place(x=10, y=0)

        self.logo_label3 = tk.Label(self, bg='#555555')
        self.logo_label3.place(x=70, y=85)

        self.load_image_from_path3()
        
        

        self.username_label = tk.Label(self, text=f"{username}: Signed in", bg='#555555', fg="white")
        self.username_label.place(x=70, y=180)


        # Buttons
        self.button1 = tk.Button(self, text="Dashboard", font=('yu gothic ui', 13, 'bold'), width=20, bd=0, bg='#0095B6', cursor='hand2', activebackground='#6CB4EE', fg='white', command=self.dashboard)
        self.button1.place(x=20, y=250)

        self.button2 = tk.Button(self, text="Account Details", font=('yu gothic ui', 13, 'bold'), width=20, bd=0, bg='#0095B6', cursor='hand2', activebackground='#6CB4EE', fg='white', command=self.AcctDetail)
        self.button2.place(x=20, y=350)

        self.button3 = tk.Button(self, text="Settings", font=('yu gothic ui', 11, 'bold'), width=22, bd=0, bg='#0095B6', cursor='hand2', activebackground='#6CB4EE', fg='white', command=self.setting)
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


        self.username_label = tk.Label(dashboard, text=f"{self.username}", font=('yu gothic ui', 35, 'bold'),bg='#003262', fg="white")
        self.username_label.place(x=135, y=70)

        account_balance = self.get_account_balance(self.username)  
        style = ttk.Style()
        style.configure("Big.TLabel", font=("Arial", 15), foreground="#003262", background="#0095B6")
        # Label to display the account balance
        self.balance_label = ttk.Label(dashboard, text=f"Account Balance ₦: {account_balance}", style="Big.TLabel", width="24")
        self.balance_label.place(x=130, y=160)

        tk.Label(dashboard, text="Activities", bg="#003262", fg="white", font=('Arial', 14, 'bold')).place(x=40, y=190)
        
        


        transfer = tk.Label(dashboard, text="Quick Actions", bg="#003262", fg="white", font=('Arial', 14, 'bold'))
        transfer.place(x=40, y=500)
        tk.Button(dashboard, text="Transfer(Soon!)", font=('Arial', 12), bg='#0095B6', fg='white', cursor='hand2').place(x=40, y=550)
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
        AcctDetail.title("Account Details")
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

        # Retrieve account details
        account_details = self.get_account_detail(self.username)

        if account_details:
            account_balance = account_details['account_balance']
            account_number = account_details['account_number']
            account_name = account_details['account_name']
            email = account_details['email']
            dob = account_details['dob']

            # Configure style
            style = ttk.Style()
            style.configure("Big.TLabel", font=("Arial", 15), foreground="#003262", background="#0095B6")

            # Display account details
            self.balance_label = ttk.Label(AcctDetail, text=f"Account Balance ₦: {account_balance}", style="Big.TLabel", width=40)
            self.balance_label.place(x=30, y=50)

            self.account_number_label = ttk.Label(AcctDetail, text=f"Account Number: {account_number}", style="Big.TLabel", width=40)
            self.account_number_label.place(x=30, y=100)

            self.account_name_label = ttk.Label(AcctDetail, text=f"Account Name: {account_name}", style="Big.TLabel", width=40)
            self.account_name_label.place(x=30, y=150)

            self.email_label = ttk.Label(AcctDetail, text=f"Email: {email}", style="Big.TLabel", width=40)
            self.email_label.place(x=30, y=200)

            self.dob_label = ttk.Label(AcctDetail, text=f"Date of Birth: {dob}", style="Big.TLabel", width=40)
            self.dob_label.place(x=30, y=250)

        

    def setting(self):
        setting = tk.Toplevel(self.master)
        setting.title("Settings")
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


    def get_account_detail(self, username):
        # Connect to MySQL database
        db = mysql.connector.connect(
            host="localhost",
            user="Bank",
            password="Bankappsql",
            database="Bank_data",
            auth_plugin='mysql_native_password'
        )
        cursor = db.cursor(dictionary=True)

        try:
            # Get account details from database
            cursor.execute("""
                SELECT account_balance, account_number, account_name, email, dob
                FROM users
                WHERE username = %s
            """, (username,))
            row = cursor.fetchone()

            if row:
                return row
            else:
                return None
        except mysql.connector.Error as err:
            messagebox.showerror("Database Error", f"Error: {err}")
            return None
        finally:
            cursor.close()
            db.close()

    

    


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

    sidebar = Sidebar(root, username=None,bg='#555555')
    sidebar.place(x=0, y=0, relwidth=0.2, relheight=1)  

    root.mainloop()
