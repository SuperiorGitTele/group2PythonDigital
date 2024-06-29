import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
from PIL import Image, ImageTk
from tkinter import simpledialog
import random
import mysql.connector
import random
import re





class NewWindow(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("Register with PROPATEES")
        self.geometry("1450x760")
        self.master = master
        img = PhotoImage(file='logo.png')
        self.iconphoto(False, img)
         

        self.state('normal')  # Instead of 'zoomed', use 'normal' to allow the window to be resized
        self.resizable(True, True)  # But then disable resizing
        # self.new_window.update_idletasks()
        self.center_window()
        self.configure(bg='#0047AB')


        # red frame at the center
        self.lgn_frame = tk.Frame(self, bg='#343434', width='950', height="600")
        self.lgn_frame.place(x=300, y=100)

        # welcome text
        self.txt = """WELCOME TO PROPATEES BANK"""
        self.heading = Label(self.lgn_frame, text=self.txt, font=('Times New Roman', 25, 'bold'), bg='#343434', fg='white')
        self.heading.place(x=200, y=5, width=550, height=100)
        
        # login button pic and button function
        self.lgn_button = Image.open('btn1.png')
        photo = ImageTk.PhotoImage(self.lgn_button)
        self.lgn_button_label = Label(self.lgn_frame, image=photo, bg='#343434')
        self.lgn_button_label.image = photo
        self.lgn_button_label.place(x=330, y=540)
        self.login = Button(self.lgn_button_label, text='REGISTER', font=("yu gothic ui", 13, "bold"), width=25, bd=0, bg='#3047ff', cursor='hand2', activebackground='#3047ff', fg='white', command=self.register)
        self.login.place(x=20, y=10)
        self.login = Button(self, text='GO BACK TO LOGIN PAGE', font=("yu gothic ui", 13, "bold"), width=25, bd=0, bg='#6CB4EE', cursor='hand2', activebackground='#3047ff', fg='white', command=self.go_backLogin)
        self.login.place(x=20, y=30)

        
        
        # logo pic
        self.logoside = Image.open('logopng.png')
        self.logoside = self.logoside.resize((80, 80), resample=Image.LANCZOS)  # Resize the image to 50x50 pixels using Lanczos resampling
        logos = ImageTk.PhotoImage(self.logoside)
        self.logo_label = Label(self.lgn_frame, image=logos, width='80', height="80", bg='#343434')
        self.logo_label.image = logos
        self.logo_label.__reduce__()
        self.logo_label.place(x=750, y=5)
        
        # face login
        self.sign_in_image = Image.open('userdisplay.png')
        photo = ImageTk.PhotoImage(self.sign_in_image)
        self.sign_in_image_label = Label(self.lgn_frame, image=photo, bg='#343434')
        self.sign_in_image_label.image = photo
        self.sign_in_image_label.place(x=400, y=92)
        
        # Sign in text
        self.sign_in_label = Label(self.lgn_frame, text="Register and Join us😎!", bg="#011F5B", fg="white", font=("yu gothic ui", 17, "bold"))
        self.sign_in_label.place(x=350, y=201)

        # Username Section
        self.username_label = Label(self.lgn_frame, text="Username", bg="#4B3621", fg="white", font=("yu gothic ui", 13, "bold"))
        self.username_label.place(x=100, y=250)

        self.username_entry = Entry(self.lgn_frame, highlightthickness=0, relief=FLAT, bg="#414A4C", fg="#6082B6", font=("yu gothic ui ", 12, "bold"), insertbackground = '#6082B6')
        self.username_entry.place(x=127, y=280, width=200)
        
        
        self.username_line = Canvas(self.lgn_frame, width=200, height=2.0, bg="#bdb9b1", highlightthickness=0)
        self.username_line.place(x=127, y=304)

                # ===== Username icon =========
        self.username_icon = Image.open('username_icon.png')
        photo = ImageTk.PhotoImage(self.username_icon)

        self.username_icon_label = Label(self.lgn_frame, image=photo, bg='#343434')
        self.username_icon_label.image = photo
        self.username_icon_label.place(x=100, y=280)

        # Password Section
        self.password_label = Label(self.lgn_frame, text="Password", bg="#4B3621", fg="white", font=("yu gothic ui", 13, "bold"))
        self.password_label.place(x=100, y=340)

        self.password_entry = Entry(self.lgn_frame, highlightthickness=0, relief=FLAT, bg="#414A4C", fg="#6082B6", font=("yu gothic ui", 12, "bold"), show="*", insertbackground = '#6082B6')
        self.password_entry.place(x=127, y=366, width=200)

        self.password_line = Canvas(self.lgn_frame, width=200, height=2.0, bg="#bdb9b1", highlightthickness=0)
        self.password_line.place(x=127, y=388)

        # Date of Birth Section
        self.dob_label = Label(self.lgn_frame, text="""Date of Birth
(DD/MM/YYYY)""", bg="#4B3621", fg="white", font=("yu gothic ui", 13, "bold"))
        self.dob_label.place(x=340, y=250)

        self.dob_entry = Entry(self.lgn_frame, highlightthickness=0, relief=FLAT, bg="#414A4C", fg="#6082B6", font=("yu gothic ui ", 12, "bold"), insertbackground = '#6082B6')
        self.dob_entry.place(x=340, y=304, width=108)

        self.dob_line = Canvas(self.lgn_frame, width=108, height=2.0, bg="#bdb9b1", highlightthickness=0)
        self.dob_line.place(x=340, y=328)



        self.secret_question_label = Label(self.lgn_frame, text="""Secret Question(Windows + H, to quickly voice 
type the question if no one is around you)""", bg="#4B3621", fg="white", font=("yu gothic ui", 13, "bold"))
        self.secret_question_label.place(x=580, y=249)

        self.secret_question_entry = Entry(self.lgn_frame, highlightthickness=0, relief=FLAT, bg="#414A4C", fg="#6082B6", font=("yu gothic ui ", 12, "bold"), insertbackground = '#6082B6')
        self.secret_question_entry.place(x=600, y=304, width=240)

        self.secret_question_line = Canvas(self.lgn_frame, width=240, height=2.0, bg="#bdb9b1", highlightthickness=0)
        self.secret_question_line.place(x=600, y=328)

        self.secret_answer_label = Label(self.lgn_frame, text="Secret Answer", bg="#4B3621", fg="white", font=("yu gothic ui", 13, "bold"))
        self.secret_answer_label.place(x=600, y=340)

        self.secret_answer_entry = Entry(self.lgn_frame, highlightthickness=0, relief=FLAT, bg="#414A4C", fg="#6082B6", font=("yu gothic ui ", 12, "bold"), insertbackground = '#6082B6')
        self.secret_answer_entry.place(x=600, y=380, width=240)

        self.secret_answer_line = Canvas(self.lgn_frame, width=240, height=2.0, bg="#bdb9b1", highlightthickness=0)
        self.secret_answer_line.place(x=600, y=404)

        self.transaction_pin_label = Label(self.lgn_frame, text="Create transaction Pin", bg="#4B3621", fg="white", font=("yu gothic ui", 13, "bold"))
        self.transaction_pin_label.place(x=600, y=450)

        self.transaction_pin_entry = Entry(self.lgn_frame, highlightthickness=0, relief=FLAT, bg="#414A4C", fg="#6082B6", font=("yu gothic ui ", 12, "bold"), insertbackground = '#6082B6', show="*")
        self.transaction_pin_entry.place(x=600, y=490, width=100)

        self.transaction_pin_line = Canvas(self.lgn_frame, width=100, height=2.0, bg="#bdb9b1", highlightthickness=0)
        self.transaction_pin_line.place(x=600, y=515)

        self.email_label = Label(self.lgn_frame, text="Enter Email(Optional)", bg="#4B3621", fg="white", font=("yu gothic ui", 13, "bold"))
        self.email_label.place(x=340, y=340)

        self.email_entry = Entry(self.lgn_frame, highlightthickness=0, relief=FLAT, bg="#414A4C", fg="#6082B6", font=("yu gothic ui ", 12, "bold"), insertbackground = '#6082B6')
        self.email_entry.place(x=340, y=380, width=255)

        self.email_line = Canvas(self.lgn_frame, width=255, height=2.0, bg="#bdb9b1", highlightthickness=0)
        self.email_line.place(x=340, y=404)
        

        self.reference_code_label = Label(self.lgn_frame, text="""PROPATEES Reference Code
(To start with a Level 2 Account)""", bg="#4B3621", fg="white", font=("yu gothic ui", 13, "bold"))
        self.reference_code_label.place(x=105, y=450)

        self.reference_code_entry = Entry(self.lgn_frame, highlightthickness=0, relief=FLAT, bg="#414A4C", fg="#6082B6", font=("yu gothic ui ", 12, "bold"), insertbackground = '#6082B6')
        self.reference_code_entry.place(x=110, y=510, width=100)

        self.reference_code_line = Canvas(self.lgn_frame, width=100, height=2.0, bg="#bdb9b1", highlightthickness=0)
        self.reference_code_line.place(x=110, y=535)
        self.reference_code_entry.bind("<Return>", lambda event: self.register())

        self.username_entry.focus()

    

        def focus_password_entry(self, event=None):
            self.password_entry.focus()

        # Bind the Enter key to focus on the password entry field
        self.username_entry.bind("<Return>", lambda event: focus_password_entry(self))

        def focus_password_entry1(self, event=None):
            self.dob_entry.focus()

        # Bind the Enter key to focus on the password entry field
        self.password_entry.bind("<Return>", lambda event: focus_password_entry1(self))

        def focus_password_entry2(self, event=None):
            self.secret_question_entry.focus()

        # Bind the Enter key to focus on the password entry field
        self.dob_entry.bind("<Return>", lambda event: focus_password_entry2(self))

        def focus_password_entry3(self, event=None):
            self.secret_answer_entry.focus()

        # Bind the Enter key to focus on the password entry field
        self.secret_question_entry.bind("<Return>", lambda event: focus_password_entry3(self))

        def focus_password_entry4(self, event=None):
            self.transaction_pin_entry.focus()

        # Bind the Enter key to focus on the password entry field
        self.secret_answer_entry.bind("<Return>", lambda event: focus_password_entry4(self))

        def focus_password_entry5(self, event=None):
            self.email_entry.focus()

        # Bind the Enter key to focus on the password entry field
        self.transaction_pin_entry.bind("<Return>", lambda event: focus_password_entry5(self))

        def focus_password_entry6(self, event=None):
            self.reference_code_entry.focus()

        # Bind the Enter key to focus on the password entry field
        self.email_entry.bind("<Return>", lambda event: focus_password_entry6(self))

        

        
        # Password Icon
        self.password_icon = Image.open('password_icon.png')
        photo = ImageTk.PhotoImage(self.password_icon)
        self.password_icon_label = Label(self.lgn_frame, image=photo, bg='#414A4C')
        self.password_icon_label.image = photo
        self.password_icon_label.place(x=100, y=365)

        # ========= show/hide password ========
        self.show_image = ImageTk.PhotoImage \
            (file='hide.png')

        self.hide_image = ImageTk.PhotoImage \
            (file='show.png')

        self.show_button = Button(self.lgn_frame, image=self.show_image, command=self.show, relief=FLAT,activebackground='#414A4C', borderwidth=0, background="#414A4C", cursor="hand2")
        self.show_button.place(x=308, y=367)

    def show(self):
        self.hide_button = Button(self.lgn_frame, image=self.hide_image, command=self.hide, relief=FLAT, activebackground='#414A4C', borderwidth=0, background="#414A4C", cursor="hand2")
        self.hide_button.place(x=308, y=367)
        self.password_entry.config(show='')

    def hide(self):
        self.show_button = Button(self.lgn_frame, image=self.show_image, command=self.show, relief=FLAT,activebackground='#414A4C', borderwidth=0, background="#414A4C", cursor="hand2")
        self.show_button.place(x=308, y=367)
        self.password_entry.config(show='*')

    


    def center_window(self):
        # Update window size info
        self.update_idletasks()
        width = self.winfo_width()
        height = self.winfo_height()
        x = (self.winfo_screenwidth() // 2) - (width // 2)
        y = (self.winfo_screenheight() // 2) - (height // 2)
        self.geometry(f'{width}x{height}+{x}+{y}')
    
    def register(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        dob = self.dob_entry.get()
        secret_question = self.secret_question_entry.get()
        secret_answer = self.secret_answer_entry.get()
        transaction_pin = self.transaction_pin_entry.get()
        reference_code = self.reference_code_entry.get()
        email = self.email_entry.get()  # Assume you have an email entry field

        if not username or not password or not dob or not secret_question or not secret_answer or not transaction_pin:
            messagebox.showerror("Error", "Please fill in all mandatory fields")
            return

        # Username validation
        if len(username) < 3:
            messagebox.showerror("Error", "Username must be at least 3 characters long")
            return

        # Password validation
        if len(password) < 8 or not re.search(r"[A-Za-z]", password) or not re.search(r"[0-9]", password):
            messagebox.showerror("Error", "Password must be at least 8 characters long and contain both letters and numbers")
            return

        # Secret question validation
        if not secret_question.endswith('?'):
            messagebox.showerror("Error", "Secret question must end with a question mark")
            return

        # Transaction pin validation
        if len(transaction_pin) != 4 or not transaction_pin.isdigit():
            messagebox.showerror("Error", "Transaction PIN must be exactly 4 digits")
            return

        # Email validation
        if email and not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            messagebox.showerror("Error", "Invalid email format")
            return

        # Parse the date of birth
        try:
            day, month, year = map(int, dob.split('/'))
            dob = f"{year}-{month:02d}-{day:02d}"
        except ValueError:
            messagebox.showerror("Error", "Invalid date of birth format. Please use DD/MM/YYYY")
            return

        # Generate a random 10-digit account number
        account_number = str(random.randint(1000000000, 9999999999))

        # Generate a random 11-digit BVN
        bvn = str(random.randint(10000000000, 99999999999))

        # Use the username as the account name
        account_name = username

        

        # Initialize account balance
        if reference_code == "QRPTP":
            # Ask for initial deposit amount
            initial_deposit_dialog = tk.Toplevel(self)
            initial_deposit_dialog.title("Initial Deposit")
            initial_deposit_dialog.grab_set()

            initial_deposit_dialog.configure(bg='#003262')
            img = ImageTk.PhotoImage(file='logo.png')
            initial_deposit_dialog.iconphoto(False, img)

             # Set size of the fund account dialog
            dialog_width = 250
            dialog_height = 70

            # Center the dialog relative to the parent window (self.new_window)
            parent_x = self.winfo_x()
            parent_y = self.winfo_y()
            parent_width = self.winfo_width()
            parent_height = self.winfo_height()

            # Calculate the position
            x = parent_x + (parent_width // 2) - (dialog_width // 2)
            y = parent_y + (parent_height // 2) - (dialog_height // 2)

            initial_deposit_dialog.geometry(f"{dialog_width}x{dialog_height}+{x}+{y}")

            tk.Label(initial_deposit_dialog, text="The reference code has granted you ₦1500", bg='#6CB4EE').pack()

            account_balance = 1500

                
            # Register user
            self.register_user(username, password, dob, secret_question, secret_answer, transaction_pin, account_number, account_balance, reference_code, bvn, account_name, email)
            initial_deposit_dialog.after(4000, lambda: initial_deposit_dialog.destroy())

            
        elif reference_code == "":
            account_balance = 0
            self.register_user(username, password, dob, secret_question, secret_answer, transaction_pin, account_number, account_balance, bvn, account_name, email, None)

        else:
            messagebox.showerror("Invalid reference code!")
               

    def register_user(self, username, password, dob, secret_question, secret_answer, transaction_pin, account_number, account_balance, reference_code, bvn, account_name, email):
        db = mysql.connector.connect(
            host="localhost",
            user="Bank",
            password="Bankappsql",
            database="Bank_data"
        )
        cursor = db.cursor()

        # Insert user data into the database
        query = """
        INSERT INTO users (username, password, dob, secret_question, secret_answer, transaction_pin, account_number, account_balance, reference_code, bvn, account_name, email)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        values = (username, password, dob, secret_question, secret_answer, transaction_pin, account_number, account_balance, reference_code, bvn, account_name, email)
        cursor.execute(query, values)

        db.commit()
        cursor.close()
        db.close()

        self.username_entry.delete(0, tk.END)
        self.password_entry.delete(0, tk.END)
        self.dob_entry.delete(0, tk.END)
        self.secret_question_entry.delete(0, tk.END)
        self.secret_answer_entry.delete(0, tk.END)
        self.transaction_pin_entry.delete(0, tk.END)
        self.reference_code_entry.delete(0, tk.END)
        if self.master.state_string == 'zoomed':
            self.master.state('zoomed')
        else:
            self.master.state('normal')
        self.withdraw()
        messagebox.showinfo("Registration Successful", "Your account has been created successfully!")
        self.master.deiconify()


    

    def go_backLogin(self):
            self.username_entry.delete(0, tk.END)
            self.password_entry.delete(0, tk.END) 
            self.master.geometry(self.master.geometry_string)
            if self.master.state_string == 'zoomed':
                self.master.state('zoomed')
            else:
                self.master.state('normal')
            self.withdraw()
            self.master.deiconify()
            self.master.username_entry.focus()
            

    def clear_on_focus(self, event):
        if self.username_entry.get() == "Type your username here...":
            event.widget.delete(0, tk.END)

# new_window = NewWindow(master=None)
# new_window.mainloop()


