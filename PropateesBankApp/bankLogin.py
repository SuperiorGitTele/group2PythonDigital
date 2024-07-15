import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import pyttsx3
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



# Run to install dependencies
# (python -m venv myenv to avoid conflicts)not necessary
# (myenv\Scripts\activate)not necessary
# pip install -r requirements.txt
# run sql.py with your root password


class LoginWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("PROPATEES Bank Log in") 
        self.geometry("1450x760")
        
        img = PhotoImage(file='logo.png')
        self.iconphoto(False, img)

    
        self.resizable(True, True) 
        self.window = self
        self.configure(bg='#003262')
        self.center_window()
        

        # Change Curve
        self.logoside = Image.open('ChangeCurve2.png')
        logos = ImageTk.PhotoImage(self.logoside)
        self.logo_label = tk.Label(self, image=logos, width='300', height="300", bg='#003262')
        self.logo_label.image = logos
        self.logo_label.__reduce__()
        self.logo_label.place(x=10, y=10)
        self.logoside = Image.open('ChangeCurve2.png')
        logos = ImageTk.PhotoImage(self.logoside)
        self.logo_label = tk.Label(self, image=logos, width='300', height="300", bg='#003262')
        self.logo_label.image = logos
        self.logo_label.__reduce__()
        self.logo_label.place(x=1210, y=550)

        # light frame at the center
        self.lgn_frame = tk.Frame(self, bg='#3B3C36', width='950', height="600")
        self.lgn_frame.place(x=300, y=100) 

        

        self.logoside = Image.open('images2.png')
        self.logoside = self.logoside.resize((80, 80), resample=Image.LANCZOS)
        logos = ImageTk.PhotoImage(self.logoside)
        self.logo_label = tk.Label(self.lgn_frame, image=logos, bg='#3B3C36')
        self.logo_label.image = logos
        self.logo_label.__reduce__()
        self.logo_label.place(x=60, y=350)

        self.logoside = Image.open('images3.png')
        self.logoside = self.logoside.resize((80, 80), resample=Image.LANCZOS)  # Resize the image to 50x50 pixels using Lanczos resampling
        logos = ImageTk.PhotoImage(self.logoside)
        self.logo_label = tk.Label(self.lgn_frame, image=logos, bg='#3B3C36')
        self.logo_label.image = logos
        self.logo_label.__reduce__()
        self.logo_label.place(x=380, y=350) 

        #=================================================

        # welcome text
        self.txt = """WELCOME TO PROPATEES BANK"""
        self.heading = Label(self.lgn_frame, text=self.txt, font=('Times New Roman', 25, 'bold'), bg='#3B3C36', fg='white')
        self.heading.place(x=0, y=5, width=550, height=100)

        self.txt = """Financial Solution Tailored For Your Properties"""
        self.heading = Label(self.lgn_frame, text=self.txt, font=('Times New Roman', 12, 'bold'), bg='#3B3C36', fg='white')
        self.heading.place(x=100, y=400, width=320, height=55)

        
        
        # Sign in text
        self.sign_in_label = Label(self.lgn_frame, text="Sign In Or Sign Up Below!", bg="#36454F", fg="white", font=("Georgia", 17, "bold"))
        self.sign_in_label.place(x=545, y=220)
        
        
        # login button pic and button function
        self.lgn_button = Image.open('btn1.png')
        photo = ImageTk.PhotoImage(self.lgn_button)
        self.lgn_button_label = Label(self.lgn_frame, image=photo, bg='#3B3C36')
        self.lgn_button_label.image = photo
        self.lgn_button_label.place(x=550, y=450)
        self.login = Button(self.lgn_button_label, text='LOGIN', font=("yu gothic ui", 13, "bold"), width=25, bd=0, bg='#3047ff', cursor='hand2', activebackground='#3047ff', fg='white', command=self.login_function)
        self.login.place(x=20, y=10)
        

        
        
        # logo pic
        self.logoside = Image.open('logopng.png')
        logos = ImageTk.PhotoImage(self.logoside)
        self.logo_label = Label(self.lgn_frame, image=logos, bg='#3B3C36')
        self.logo_label.image = logos
        self.logo_label.__reduce__()
        self.logo_label.place(x=120, y=70)
        
        # face login
        self.sign_in_image = Image.open('userdisplay.png')
        photo = ImageTk.PhotoImage(self.sign_in_image)
        self.sign_in_image_label = Label(self.lgn_frame, image=photo, bg='#3B3C36')
        self.sign_in_image_label.image = photo
        self.sign_in_image_label.place(x=620, y=110)
               
                # ===== Username icon =========
        self.username_icon = Image.open('username_icon.png')
        photo = ImageTk.PhotoImage(self.username_icon)
        self.username_icon_label = Label(self.lgn_frame, image=photo, bg='#3B3C36')
        self.username_icon_label.image = photo
        self.username_icon_label.place(x=550, y=332)
        

        # Username Entry Section
        self.username_label = Label(self.lgn_frame, text="Username", bg="#003262", fg="white", font=("yu gothic ui", 13, "bold"))
        self.username_label.place(x=550, y=300)

        self.username_entry = Entry(self.lgn_frame, highlightthickness=0, relief=FLAT, bg="#353839", fg="#6082B6", font=("yu gothic ui ", 12, "bold"), insertbackground = '#6082B6')
        self.username_entry.place(x=580, y=335, width=270)
        self.username_entry.insert(0, "Type your username here...")
        self.username_entry.bind("<FocusIn>", self.clear_on_focus)

        self.username_line = Canvas(self.lgn_frame, width=300, height=2.0, bg="#bdb9b1", highlightthickness=0)
        self.username_line.place(x=550, y=359)

        # Password Icon
        self.password_icon = Image.open('password_icon.png')
        photo = ImageTk.PhotoImage(self.password_icon)
        self.password_icon_label = Label(self.lgn_frame, image=photo, bg='#3B3C36')
        self.password_icon_label.image = photo
        self.password_icon_label.place(x=550, y=414)

        # Password Entry Section
        self.password_label = Label(self.lgn_frame, text="Password", bg="#003262", fg="white", font=("yu gothic ui", 13, "bold"))
        self.password_label.place(x=550, y=380)

        self.password_entry = Entry(self.lgn_frame, highlightthickness=0, relief=FLAT, bg="#353839", fg="#6082B6", font=("yu gothic ui", 12, "bold"), show="*", insertbackground = '#6082B6')
        self.password_entry.place(x=580, y=416, width=300)
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


        # ========= show/hide password ========
        self.show_image = ImageTk.PhotoImage \
            (file='show.png')

        self.hide_image = ImageTk.PhotoImage \
            (file='hide.png')

        self.show_button = Button(self.lgn_frame, image=self.hide_image, command=self.show, relief=FLAT,activebackground="white", borderwidth=0, background="#353839", cursor="hand2")
        self.show_button.place(x=860, y=420)

        
        # Forgot button
        self.forgot_button = Button(self.lgn_frame, text="Forgot Password ?",font=("yu gothic ui", 13, "bold underline"), fg="white", relief=FLAT,activebackground="pink", borderwidth=0, background="#3B3C36", cursor="hand2", command=self.submit_reset_password)
        self.forgot_button.place(x=630, y=510)


    def clear_on_focus(self, event):
        if self.username_entry.get() == "Type your username here...":
            event.widget.delete(0, tk.END)
        
    
    def on_configure(self, event):
        # Store the current geometry and state
        if self.state() == 'normal':
            self.geometry_string = self.geometry()
        self.state_string = self.state()

    def center_window(self):
        # Update window size info
        self.update_idletasks()
        width = self.winfo_width()
        height = self.winfo_height()
        x = (self.winfo_screenwidth() // 2) - (width // 2)
        y = (self.winfo_screenheight() // 2) - (height // 2)
        self.geometry(f'{width}x{height}+{x}+{y}')
        

    def submit_reset_password(self):
        dialog = tk.Toplevel(self.window)
        dialog.title("Forgot Password")
        dialog.grab_set()
        dialog.configure(bg='#003262')
        img = ImageTk.PhotoImage(file='logo.png')
        dialog.iconphoto(False, img)
        


        # Set size of the fund account dialog
        dialog_width = 400
        dialog_height = 300

        # Center the dialog relative to the parent window (self)
        parent_x = self.winfo_x()
        parent_y = self.winfo_y()
        parent_width = self.winfo_width()
        parent_height = self.winfo_height()

        # Calculate the position
        x = parent_x + (parent_width // 2) - (dialog_width // 2)
        y = parent_y + (parent_height // 2) - (dialog_height // 2)

        dialog.geometry(f"{dialog_width}x{dialog_height}+{x}+{y}")

        tk.Label(dialog, text="Enter your username:", bg='#6CB4EE').pack()
        username_entry = tk.Entry(dialog)
        username_entry.pack()

        tk.Label(dialog, text="Enter your Secret Question:", bg='#6CB4EE').pack()
        secret_entry = tk.Entry(dialog)
        secret_entry.pack()

        tk.Label(dialog, text="Enter your Secret Answer:", bg='#6CB4EE').pack()
        answer_entry = tk.Entry(dialog)
        answer_entry.pack()

        def ok_callback():
            username = username_entry.get()
            secretQ = secret_entry.get()
            secretA = answer_entry.get()
            if username and secretQ and secretA:
                try:
                    db = mysql.connector.connect(
                        host="localhost",
                        user="Bank",
                        password="Bankappsql",
                        database="Bank_data"
                    )
                    cursor = db.cursor()
                    cursor.execute("SELECT * FROM users WHERE username = %s AND secret_question = %s AND secret_answer = %s", (username, secretQ, secretA))
                    row = cursor.fetchone()
                    db.close()
                    if row:
                        # Show a message box with a welcome message
                        messagebox.showinfo("Login Success", f"Welcome, {username}! Login successful!")

                        if self.check_wifi_and_internet_speed():
                            # If there is an internet connection, use pygame
                            self.play_audio(username)
                            self.open_welcome_window(username)
                            self.withdraw()
                            dialog.destroy()

                            
                        else:
                            # If there is no internet connection, use pyttsx3
                            self.play_welcome_audio_pyttsx3(username)
                            # Open a new window
                            self.open_welcome_window(username)
                            self.withdraw()
                            dialog.destroy()
                    else:
                        messagebox.showerror("Error", "Invalid username or Secret Question and Answer")
                except ValueError:
                    messagebox.showerror("Error", "Invalid Secret Question")
            else:
                messagebox.showerror("Error", "Please enter username, secret question and answer")

        tk.Button(dialog, text="Retrieve Account", bg='#3047ff', command=ok_callback).pack()
        answer_entry.bind("<Return>", ok_callback)

                   
    def show(self):
        self.hide_button = Button(self.lgn_frame, image=self.show_image, command=self.hide, relief=FLAT, activebackground="white", borderwidth=0, background="#353839", cursor="hand2")
        self.hide_button.place(x=860, y=420)
        self.password_entry.config(show='')

    def hide(self):
        self.show_button = Button(self.lgn_frame, image=self.hide_image, command=self.show, relief=FLAT,activebackground="white", borderwidth=0, background="#353839", cursor="hand2")
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
            user="Bank",
            password="Bankappsql",
            database="Bank_data",
            auth_plugin='mysql_native_password'
        )
        cursor = db.cursor()

        try:
            # Check if username and password exist in the database
            cursor.execute("SELECT * FROM users WHERE username = %s AND password = %s", (username, password))
            row = cursor.fetchone()

            if row:
                # Show a message box with a welcome message
                self.username_entry.delete(0, tk.END)
                self.password_entry.delete(0, tk.END)
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
                tts = gTTS(text=f"Welcome {username}, to Properties Bank!", lang='en')
                tts.save("welcome.mp3")
                pygame.mixer.init()
                pygame.mixer.music.load("welcome.mp3")
                pygame.mixer.music.play()
                while pygame.mixer.music.get_busy() == True:
                    time.sleep(0.1) #audio time play
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
        engine.say(f"Welcome {username}, to Properties Bank!")
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

            # Perform a internet speed test
            start_time = time.time()
            response = requests.get("https://httpbin.org/bytes/1024", timeout=3)
            end_time = time.time()

            # Check if the response was successful and if the time taken is less than 2 seconds
            if response.status_code == 200 and (end_time - start_time) < 3:
                return True
            else:
                return False
        except (subprocess.CalledProcessError, requests.RequestException):
            return False
        
    



    def open_new_window(self):
        # Store the current geometry and state
        self.geometry_string = self.geometry()
        self.state_string = self.state()

        # Hide the main window
        self.withdraw()

        # Create and show the new window
        new_window = NewWindow(self)
        self.center_window()

    def window_state(self):
        if self.wm_state() == 'zoomed':
            return 'zoomed'
        else:
            return 'normal'
    




if __name__ == "__main__":
    app = LoginWindow()
    app.mainloop()


