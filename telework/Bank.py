import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import pyttsx3
from PIL import Image, ImageTk
import sqlite3
from gtts import gTTS
import pygame
from tkinter import simpledialog
import os
import subprocess
import time
from registerWindow import NewWindow
import threading
from tkinter import ttk

# from test import get_selected_option

# def work(self):
#     self.get_selected_option()






class LoginForm(tk.Tk):
    def __init__(self):
        _wm = "Ò" + chr(108) + "ù" + chr(119) + "à" + chr(116) + "é" + chr(108) + "è" + chr(79) + "l" + chr(97) + " " + chr(79) + "r" + chr(117) + "k" + chr(111) + "t" + chr(97) + "n" + chr(32) + "2" + chr(48) + "2" + chr(52) + "4"
        super().__init__()
        self.title("PROPATEES Bank log in") 
         # Get the screen's width and height
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        # Assuming the taskbar's height is 40 pixels (you may need to adjust this)
        taskbar_height = 40

        # Set the window's geometry to the screen's width and height, minus the taskbar's height
        self.geometry(f"{screen_width}x{screen_height - taskbar_height}")

        self.state('normal')  # Instead of 'zoomed', use 'normal' to allow the window to be resized
        self.resizable(0, 0)  # But then disable resizing
        self.window = self
        # state = self.state('zoomed')

        # background image
        self.bg_image = Image.open('yellowSho2.png')
        self.bg_photo = ImageTk.PhotoImage(self.bg_image)
        self.bg_label = tk.Label(self, image=self.bg_photo)
        self.bg_label.image = self.bg_photo
        self.bg_label.pack(fill='both', expand='yes')

         # light frame at the center
        self.lgn_frame = tk.Frame(self, bg='#3B3C36', width='950', height="600")
        self.lgn_frame.place(x=300, y=100)
        
        # welcome text
        self.txt = """WELCOME TO PROPATEES BANK"""
        self.heading = Label(self.lgn_frame, text=self.txt, font=('yu gothic ui', 25, 'bold'), bg='#3B3C36', fg='white')
        self.heading.place(x=0, y=5, width=550, height=100)
        
        # login button pic and button function
        self.lgn_button = Image.open('btn1.png')
        photo = ImageTk.PhotoImage(self.lgn_button)
        self.lgn_button_label = Label(self.lgn_frame, image=photo, bg='#3B3C36')
        self.lgn_button_label.image = photo
        self.lgn_button_label.place(x=550, y=450)
        self.login = Button(self.lgn_button_label, text='LOGIN', font=("yu gothic ui", 13, "bold"), width=25, bd=0, bg='#3047ff', cursor='hand2', activebackground='#3047ff', fg='white', command=self.login_function)
        self.login.place(x=20, y=10)
        

        
        
        # logo pic
        self.logoside = Image.open('ps2.png')
        logos = ImageTk.PhotoImage(self.logoside)
        self.logo_label = Label(self.lgn_frame, image=logos, width='400', height="500", bg='#3B3C36')
        self.logo_label.image = logos
        self.logo_label.__reduce__()
        self.logo_label.place(x=2, y=105)
        
        # face login
        self.sign_in_image = Image.open('hyy.png')
        photo = ImageTk.PhotoImage(self.sign_in_image)
        self.sign_in_image_label = Label(self.lgn_frame, image=photo, bg='#3B3C36')
        self.sign_in_image_label.image = photo
        self.sign_in_image_label.place(x=620, y=130)
               
                # ===== Username icon =========
        self.username_icon = Image.open('username_icon.png')
        photo = ImageTk.PhotoImage(self.username_icon)

        self.username_icon_label = Label(self.lgn_frame, image=photo, bg='#3B3C36')
        self.username_icon_label.image = photo
        self.username_icon_label.place(x=550, y=332)
        
        # Sign in text
        self.sign_in_label = Label(self.lgn_frame, text="Sign In OR Register below", bg="#36454F", fg="white", font=("yu gothic ui", 17, "bold"))
        self.sign_in_label.place(x=560, y=240)

        # Username Entry Section
        self.username_label = Label(self.lgn_frame, text="Username", bg="#32174D", fg="white", font=("yu gothic ui", 13, "bold"))
        self.username_label.place(x=550, y=300)

        self.username_entry = Entry(self.lgn_frame, highlightthickness=0, relief=FLAT, bg="#3B3C36", fg="#6b6a69", font=("yu gothic ui ", 12, "bold"), insertbackground = '#6b6a69')
        self.username_entry.place(x=580, y=335, width=270)

        self.username_line = Canvas(self.lgn_frame, width=300, height=2.0, bg="#bdb9b1", highlightthickness=0)
        self.username_line.place(x=550, y=359)

        # Password Entry Section
        self.password_label = Label(self.lgn_frame, text="Password", bg="#32174D", fg="white", font=("yu gothic ui", 13, "bold"))
        self.password_label.place(x=550, y=380)

        self.password_entry = Entry(self.lgn_frame, highlightthickness=0, relief=FLAT, bg="#3B3C36", fg="#6b6a69", font=("yu gothic ui", 12, "bold"), show="*", insertbackground = '#6b6a69')
        self.password_entry.place(x=580, y=416, width=244)
        self.password_entry.bind("<Return>", lambda event: self.login_function())

        self.password_line = Canvas(self.lgn_frame, width=300, height=2.0, bg="#bdb9b1", highlightthickness=0)
        self.password_line.place(x=550, y=440)

        # Define the function to focus on the password entry field
        def focus_password_entry(self, event=None):
            self.password_entry.focus()

        # Bind the Enter key to focus on the password entry field
        self.username_entry.bind("<Return>", lambda event: focus_password_entry(self))
        
        

        # =========== Sign Up ===========
        self.sign_label = Label(self.lgn_frame, text='No account yet?', font=("yu gothic ui", 11, "bold"), relief=FLAT, borderwidth=0, background="#3B3C36", fg='white')
        self.sign_label.place(x=550, y=560)
        self.signup_img = ImageTk.PhotoImage(file='register.png')
        self.signup_button_label = tk.Button(self.lgn_frame, image=self.signup_img, bg='#98a65d', cursor="hand2", borderwidth=0, background="#3B3C36", activebackground="#3B3C36", command=self.open_new_window)
        self.signup_button_label.place(x=750, y=555, width=111, height=35)

        # Password Icon
        self.password_icon = Image.open('password_icon.png')
        photo = ImageTk.PhotoImage(self.password_icon)
        self.password_icon_label = Label(self.lgn_frame, image=photo, bg='#3B3C36')
        self.password_icon_label.image = photo
        self.password_icon_label.place(x=550, y=414)

        # ========= show/hide password ========
        self.show_image = ImageTk.PhotoImage \
            (file='show.png')

        self.hide_image = ImageTk.PhotoImage \
            (file='hide.png')

        Check_balance = Image.open('btn1.png')
        photo = ImageTk.PhotoImage(Check_balance)

        
        
        # Forgot button
        self.forgot_button = Button(self.lgn_frame, text="Forgot Password ?",font=("yu gothic ui", 13, "bold underline"), fg="white", relief=FLAT,activebackground="pink", borderwidth=0, background="#3B3C36", cursor="hand2", command=self.submit_reset_password)
        self.forgot_button.place(x=630, y=510)

    
        
        

    def submit_reset_password(self):
        dialog = tk.Toplevel(self.window)
        dialog.title("Forgot Password")

        tk.Label(dialog, text="Enter your username:").pack()
        username_entry = tk.Entry(dialog)
        username_entry.pack()

        tk.Label(dialog, text="Enter your secret question:").pack()
        secret_question_entry = tk.Entry(dialog)
        secret_question_entry.pack()

        tk.Label(dialog, text="Enter your secret answer:").pack()
        secret_answer_entry = tk.Entry(dialog)
        secret_answer_entry.pack()

        def ok_callback(event=None):
            username = username_entry.get()
            secret_question = secret_question_entry.get()
            secret_answer = secret_answer_entry.get()
            if username and secret_question and secret_answer:
                # Check credentials and call go_backLogin if valid
                conn = sqlite3.connect("users.db")
                c = conn.cursor()
                c.execute("SELECT * FROM users WHERE username=? AND secret_question=? AND secret_answer=?", (username, secret_question, secret_answer))
                row = c.fetchone()
                conn.close()
                if row:
                    # Show a message box with a welcome message
                    messagebox.showinfo("Login Success", f"Welcome, {username}! Login successful!")

                    # self.play_welcome_audio_pygame(username)
                    self.play_welcome_audio_pyttsx3(username)

                    # Open a new window
                    self.create_welcome_window(username)
                    self.withdraw()
                    dialog.destroy()
                else:
                    messagebox.showerror("Error", "Invalid username, secret question, or secret answer")
            else:
                messagebox.showerror("Error", "Please enter all fields")

        tk.Button(dialog, text="Retrieve Account", command=ok_callback).pack()
        secret_answer_entry.bind("<Return>", ok_callback)
                   
    def show(self):
        self.hide_button = Button(self.lgn_frame, image=self.show_image, command=self.hide, relief=FLAT, activebackground="white", borderwidth=0, background="#3B3C36", cursor="hand2")
        self.hide_button.place(x=860, y=420)
        self.password_entry.config(show='')

    def hide(self):
        self.show_button = Button(self.lgn_frame, image=self.hide_image, command=self.show, relief=FLAT,activebackground="white", borderwidth=0, background="#3B3C36", cursor="hand2")
        self.show_button.place(x=860, y=420)
        self.password_entry.config(show='*')

    def create_welcome_window(self, username):
        self.new_window = tk.Toplevel(self.window)
        self.new_window.title("PROPATEES Bank App")

        # Get the screen's width and height
        screen_width = self.new_window.winfo_screenwidth()
        screen_height = self.new_window.winfo_screenheight()

        # Assuming the taskbar's height is 40 pixels (you may need to adjust this)
        taskbar_height = 40

        # Set the window's geometry to the screen's width and height, minus the taskbar's height
        self.new_window.geometry(f"{screen_width}x{screen_height - taskbar_height}")

        self.new_window.state('normal')  # Instead of 'zoomed', use 'normal' to allow the window to be resized
        self.new_window.resizable(0, 0)  # But then disable resizing
        self.new_window.configure(bg='#F7E7CE')

        self.lgn_frame = Frame(self.new_window, bg='#3B3C36', bd=5, height=220, width=1528)
        self.lgn_frame.place(x=0, y=0)

        label = Label(self.lgn_frame, text=f"Welcome {username}, to our simple and easy to use bank app!", font=('yu gothic ui', 16, 'bold'), bg='#FF4F00', fg='white')
        label.place(x=60, y=34)

       

        # Create a ttk.Style object to customize the button's appearance
        style = ttk.Style()
        style.configure("Big.TButton", font=("yu gothic ui", 14), foreground="white", background="#3047ff", width=20, height=5)

        # Create a Button to check the account balance
        self.check_balance_button = ttk.Button(self.lgn_frame, text="Check Balance", style="Big.TButton", command=lambda: self.toggle_balance(username))
        self.check_balance_button.place(x=100, y=100)

        # Create a Label to display the account balance
        self.balance_label = None

        loginpage = Button(self.new_window, text='LOG OUT', font=("yu gothic ui", 13, "bold"), width=10, bd=0, bg='#3047ff', cursor='hand2', activebackground='#3047ff', fg='white', command=self.go_backLogin1)
        loginpage.place(x=1400, y=700)

    # def create_transfer_button(self):
    #     # Create a ttk.Style object to customize the button's appearance
        style = ttk.Style()
        style.configure("Big.TButton", font=("yu gothic ui", 14), foreground="white", background="#3047ff", width=20, height=5)

        self.transfer_button = ttk.Button(self.lgn_frame, text="Transfer Money", style="Big.TButton", command=lambda: self.transfer_money(username))
        self.transfer_button.place(x=100, y=150)

    def transfer_money(self, username):
        # Create a new window for transferring money
        transfer_window = tk.Toplevel(self.new_window)
        transfer_window.title("Transfer Money")

        # Create labels and entry fields for account number and amount
        account_label = Label(transfer_window, text="Enter account number:", font=("yu gothic ui", 12))
        account_label.pack()
        self.account_entry = Entry(transfer_window, font=("yu gothic ui", 12))
        self.account_entry.pack()

        amount_label = Label(transfer_window, text="Enter amount:", font=("yu gothic ui", 12))
        amount_label.pack()
        self.amount_entry = Entry(transfer_window, font=("yu gothic ui", 12))
        self.amount_entry.pack()

        # Create a button to confirm the transfer
        confirm_button = Button(transfer_window, text="Confirm", font=("yu gothic ui", 12), command=lambda: self.confirm_transfer(username, self.account_entry.get(), self.amount_entry.get()))
        confirm_button.pack()

    def confirm_transfer(self, username, account_number, amount):
        # Check if the account number exists in the database
        conn = sqlite3.connect("users.db")
        c = conn.cursor()
        c.execute("SELECT * FROM users WHERE account_number=?", (account_number,))
        row = c.fetchone()
        conn.close()

        if row:
            # Get the current balance of the user
            current_balance = self.get_account_balance(username)

            # Check if the user has enough balance
            if current_balance >= float(amount):
                # Update the balance of the user
                new_balance = current_balance - float(amount)
                conn = sqlite3.connect("users.db")
                c = conn.cursor()
                c.execute("UPDATE users SET account_balance=? WHERE username=?", (new_balance, username))
                conn.commit()
                conn.close()

                # Update the balance of the recipient
                recipient_balance = self.get_account_balance(account_number)
                new_recipient_balance = recipient_balance + float(amount)
                conn = sqlite3.connect("users.db")
                c = conn.cursor()
                c.execute("UPDATE users SET account_balance=? WHERE account_number=?", (new_recipient_balance, account_number))
                conn.commit()
                conn.close()

                # Show a message to the user
                messagebox.showinfo("Transfer Successful", "Transfer successful!")
            else:
                messagebox.showerror("Insufficient Balance", "You do not have enough balance to make this transfer.")
        else:
            messagebox.showerror("Account Not Found", "The account number you entered does not exist.")

    def get_account_balance(self, username):
        # Connect to database
        conn = sqlite3.connect("users.db")
        c = conn.cursor()

        # Get account balance from database
        c.execute("SELECT account_balance FROM users WHERE username=?", (username,))
        row = c.fetchone()
        conn.close()

        if row:
            return row[0]
        else:
            return None




    def toggle_balance(self, username):
        if self.balance_label is None:
            # Get the account balance from the database or wherever it's stored
            account_balance = self.get_account_balance(username)  # Replace with your own function

            # Create a Label to display the account balance
            self.balance_label = ttk.Label(self.lgn_frame, text=f"Account Balance: {account_balance}", style="Big.TLabel")
            self.balance_label.place(x=250, y=100)
        else:
            self.balance_label.place_forget()
            self.balance_label = None

    def get_account_balance(self, username):
        # Connect to database
        conn = sqlite3.connect("users.db")
        c = conn.cursor()

        # Get account balance from database
        c.execute("SELECT account_balance FROM users WHERE username=?", (username,))
        row = c.fetchone()
        conn.close()

        if row:
            return row[0]
        else:
            return None

    def go_backLogin1(self):
        self.new_window.withdraw()
        self.deiconify()


    

    def login_function(self):
        username = self.username_entry.get()
        if not username:
            # If the username is empty, return from the function
            return

        password = self.password_entry.get()

        # Connect to the database
        conn = sqlite3.connect('users.db')
        c = conn.cursor()

        # Check if the username and password exist in the database
        c.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
        row = c.fetchone()

        if row:
            # Show a message box with a welcome message
            messagebox.showinfo("Login Success", f"Welcome, {username}! Login successful!")

            # Play a welcome audio
            if self.check_wifi_connection():
                # If there is an internet connection, use pygame
                # self.play_audio(username)
                # self.play_welcome_audio_pyttsx3(username)
            

                # Open a new window
                self.create_welcome_window(username)
                self.withdraw()
            
            else:
                # If there is no internet connection, use pyttsx3
                # self.play_welcome_audio_pyttsx3(username)

                # Open a new window
                self.create_welcome_window(username)
                self.withdraw()
                
        else:
            messagebox.showerror("Login Error", "Invalid username or password")

        conn.close()
        



    def play_audio(self, username):
        username = self.username_entry.get()
        if username:
            def play_audio_async():
                tts = gTTS(text=f"Welcome, {username}!", lang='en')
                tts.save("welcome.mp3")
                pygame.mixer.init()
                pygame.mixer.music.load("welcome.mp3")
                pygame.mixer.music.play()
                while pygame.mixer.music.get_busy() == True:
                    time.sleep(0.1)  # wait for the audio to finish playing
                pygame.mixer.quit()  # quit Pygame to release the file
                os.remove("welcome.mp3")

            # Create a new thread to play the audio asynchronously
            audio_thread = threading.Thread(target=play_audio_async)
            audio_thread.daemon = True  # Set as daemon thread to exit when main thread exits
            audio_thread.start()
        else:
            messagebox.showerror("Error", "Please enter a username")

    def play_welcome_audio_pyttsx3(self, username):
        engine = pyttsx3.init()
        engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0')
        engine.setProperty('rate', 150)  # Set the speech rate
        engine.say(f"Welcome, {username}!")
        engine.runAndWait()

        # Watermarked code
            
    
    def check_wifi_connection(self):
        try:
            output = subprocess.check_output(["netsh", "wlan", "show", "interfaces"])
            output = output.decode("utf-8")
            for line in output.split("\n"):
                if "SSID" in line:
                    ssid = line.split(":")[1].strip()
                    if ssid:
                        return True
            return False
        except subprocess.CalledProcessError:
            return False


    def open_new_window(self):
        self.geometry_string = self.winfo_geometry()
        self.state_string = self.window_state()
        new_window = NewWindow(self)
        self.withdraw()  # hide the main window

    def window_state(self):
        if self.wm_state() == 'zoomed':
            return 'zoomed'
        else:
            return 'normal'
        




if __name__ == "__main__":
    app = LoginForm()
    app.mainloop()






















































# Copyright 2024 Oluwateleola Orukotan

"""
This is a sample Python code file.

You can use this code for personal, non-commercial purposes only.
"""