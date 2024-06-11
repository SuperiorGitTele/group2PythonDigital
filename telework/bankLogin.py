import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import pyttsx3
from PIL import Image, ImageTk
import sqlite3
from gtts import gTTS
import pygame
import os
import subprocess
import time
from registerWindow import NewWindow
import threading
from mainBank import WelcomeWindow
import mysql.connector
import requests




class LoginWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("PROPATEES Bank log in") 
         # Get the screen's width and height
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        # Assuming the taskbar's height is 40 pixels (you may need to adjust this)
        taskbar_height = 70

        # Set the window's geometry to the screen's width and height, minus the taskbar's height
        self.geometry(f"{screen_width}x{screen_height - taskbar_height}")

        self.state('normal')  # Instead of 'zoomed', use 'normal' to allow the window to be resized
        self.resizable(0, 0)  # But then disable resizing
        self.window = self
        # state = self.state('zoomed')

        # background image
        # self.bg_image = Image.open('yellowSho2.png')
        # self.bg_photo = ImageTk.PhotoImage(self.bg_image)
        # self.bg_label = tk.Label(self, image=self.bg_photo)
        # self.bg_label.image = self.bg_photo
        # self.bg_label.pack(fill='both', expand='yes')

        self.configure(bg='#003262')

         # light frame at the center
        self.lgn_frame = tk.Frame(self, bg='#3B3C36', width='950', height="600")
        self.lgn_frame.place(x=300, y=100)
        
        # welcome text
        self.txt = """WELCOME TO PROPATEES BANK"""
        
        
        
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
        self.username_label = Label(self.lgn_frame, text="Username", bg="#003262", fg="white", font=("yu gothic ui", 13, "bold"))
        self.username_label.place(x=550, y=300)

        self.username_entry = Entry(self.lgn_frame, highlightthickness=0, relief=FLAT, bg="#3B3C36", fg="#6b6a69", font=("yu gothic ui ", 12, "bold"), insertbackground = '#6b6a69')
        self.username_entry.place(x=580, y=335, width=270)
        self.username_entry.focus()

        self.username_line = Canvas(self.lgn_frame, width=300, height=2.0, bg="#bdb9b1", highlightthickness=0)
        self.username_line.place(x=550, y=359)

        # Password Entry Section
        self.password_label = Label(self.lgn_frame, text="Password", bg="#003262", fg="white", font=("yu gothic ui", 13, "bold"))
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

        self.show_button = Button(self.lgn_frame, image=self.hide_image, command=self.show, relief=FLAT,activebackground="white", borderwidth=0, background="#3B3C36", cursor="hand2")
        self.show_button.place(x=860, y=420)

        
        # Forgot button
        self.forgot_button = Button(self.lgn_frame, text="Forgot Password ?",font=("yu gothic ui", 13, "bold underline"), fg="white", relief=FLAT,activebackground="pink", borderwidth=0, background="#3B3C36", cursor="hand2", command=self.submit_reset_password)
        self.forgot_button.place(x=630, y=510)

    
        
        

    def submit_reset_password(self):
        dialog = tk.Toplevel(self.window)
        dialog.title("Forgot Password")

        tk.Label(dialog, text="Enter your username:").pack()
        username_entry = tk.Entry(dialog)
        username_entry.pack()

        tk.Label(dialog, text="Enter your date of birth (DD/MM/YYYY):").pack()
        dob_entry = tk.Entry(dialog)
        dob_entry.pack()

        def ok_callback():
            username = username_entry.get()
            dob = dob_entry.get()
            if username and dob:
                try:
                    day, month, year = map(int, dob.split('/'))
                    dob_formatted = f"{year}-{month:02d}-{day:02d}"  # Convert to YYYY-MM-DD format
                    # Check credentials and call go_backLogin if valid
                    conn = sqlite3.connect("users.db")
                    c = conn.cursor()
                    c.execute("SELECT * FROM users WHERE username=? AND dob=?", (username, dob_formatted))
                    row = c.fetchone()
                    conn.close()
                    if row:
                        # Show a message box with a welcome message
                        messagebox.showinfo("Login Success", f"Welcome, {username}! Login successful!")

                        if self.check_wifi_connection():
                            # If there is an internet connection, use pygame
                            # self.play_audio(username)
                            self.open_welcome_window(username)
                            self.withdraw()
                            
                        else:
                            # If there is no internet connection, use pyttsx3
                            self.play_welcome_audio_pyttsx3(username)

                        # Open a new window
                        self.open_welcome_window(username)
                        self.withdraw()
                        dialog.destroy()
                    else:
                        messagebox.showerror("Error", "Invalid username or date of birth")
                except ValueError:
                    messagebox.showerror("Error", "Invalid date of birth format. Please use DD/MM/YYYY")
            else:
                messagebox.showerror("Error", "Please enter both username and date of birth")

        tk.Button(dialog, text="Retrieve Account", command=ok_callback).pack()
        dob_entry.bind("<Return>", ok_callback)

                   
    def show(self):
        self.hide_button = Button(self.lgn_frame, image=self.show_image, command=self.hide, relief=FLAT, activebackground="white", borderwidth=0, background="#3B3C36", cursor="hand2")
        self.hide_button.place(x=860, y=420)
        self.password_entry.config(show='')

    def hide(self):
        self.show_button = Button(self.lgn_frame, image=self.hide_image, command=self.show, relief=FLAT,activebackground="white", borderwidth=0, background="#3B3C36", cursor="hand2")
        self.show_button.place(x=860, y=420)
        self.password_entry.config(show='*')

    def open_welcome_window(master, username):
        welcome_window = WelcomeWindow(master, username)
        return welcome_window


    

    def login_function(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if not username or not password:
            messagebox.showerror("Error", "Please fill in all fields")
            return

        # Connect to MySQL database
        db = mysql.connector.connect(
            host="localhost",
            user="tele",
            password="telesql19",
            database="new_database"
        )
        cursor = db.cursor()

        try:
            # Check if username and password exist in the database
            cursor.execute("SELECT * FROM users WHERE username = %s AND password = %s", (username, password))
            row = cursor.fetchone()

            if row:
                # Show a message box with a welcome message
                messagebox.showinfo("Login Success", f"Welcome, {username}! Login successful!")

                # Play a welcome audio
                if self.check_wifi_and_internet_speed():
                    # If there is an internet connection, use pygame
                    self.play_audio(username)
                    self.open_welcome_window(username)
                    self.withdraw()
                    
                else:
                    # If there is no internet connection, use pyttsx3
                    self.play_welcome_audio_pyttsx3(username)

                    # Open a new window
                    self.open_welcome_window(username)
                    self.withdraw()
               
            else:
                messagebox.showerror("Login Error", "Invalid username or password")

        except mysql.connector.Error as err:
            messagebox.showerror("Database Error", f"Error: {err}")
        finally:
            # Close the connection
            cursor.close()
            db.close()

        

    
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

                        

    def check_wifi_and_internet_speed(self):
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
            response = requests.get("https://httpbin.org/bytes/1024", timeout=2)
            end_time = time.time()

            # Check if the response was successful and if the time taken is less than 2 seconds
            if response.status_code == 200 and (end_time - start_time) < 2:
                return True
            else:
                return False
        except (subprocess.CalledProcessError, requests.RequestException):
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
    app = LoginWindow()
    app.mainloop()


