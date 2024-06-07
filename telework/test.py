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


class LoginForm(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("PAMPROSTEES Bank log in") 
        self.geometry("1080x760")
        self.state('zoomed')
        self.resizable(0, 0)
        self.window = self
        state = self.state('zoomed')

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
        self.txt = """WELCOME TO PAMPROSTEES BANK"""
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

        self.bind("<Return>", lambda event: self.login_function())
        
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

        self.password_line = Canvas(self.lgn_frame, width=300, height=2.0, bg="#bdb9b1", highlightthickness=0)
        self.password_line.place(x=550, y=440)

        # Define the function to focus on the password entry field
        def focus_password_entry(self, event=None):
            self.password_entry.focus()

        # Bind the Enter key to focus on the password entry field
        self.username_entry.bind("<Return>", lambda event: focus_password_entry(self))
        self.bind("<Return>", lambda event: self.login_function())

        # ======== Password icon ================
        self.password_icon = Image.open('password_icon.png')
        photo = ImageTk.PhotoImage(self.password_icon)
        self.password_icon_label = Label(self.lgn_frame, image=photo, bg='#3B3C36')
        self.password_icon_label.image = photo
        self.password_icon_label.place(x=550, y=414)

        # Forgot button
        self.forgot_button = Button(self.lgn_frame, text="Forgot Password ?",font=("yu gothic ui", 13, "bold underline"), fg="white", relief=FLAT,activebackground="pink", borderwidth=0, background="#3B3C36", cursor="hand2")
        self.forgot_button.place(x=630, y=510)

        # =========== Sign Up ===========
        self.sign_label = Label(self.lgn_frame, text='No account yet?', font=("yu gothic ui", 11, "bold"), relief=FLAT, borderwidth=0, background="#3B3C36", fg='white')
        self.sign_label.place(x=550, y=560)
        self.signup_img = ImageTk.PhotoImage(file='register.png')
        self.signup_button_label = tk.Button(self.lgn_frame, image=self.signup_img, bg='#98a65d', cursor="hand2", borderwidth=0, background="#3B3C36", activebackground="#3B3C36", command=self.open_new_window)
        self.signup_button_label.place(x=670, y=555, width=111, height=35)

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

        self.show_button = Button(self.lgn_frame, image=self.show_image, command=self.show, relief=FLAT,activebackground="white", borderwidth=0, background="#3B3C36", cursor="hand2")
        self.show_button.place(x=860, y=420)

    def show(self):
        self.hide_button = Button(self.lgn_frame, image=self.hide_image, command=self.hide, relief=FLAT, activebackground="white", borderwidth=0, background="#3B3C36", cursor="hand2")
        self.hide_button.place(x=860, y=420)
        self.password_entry.config(show='')

    def hide(self):
        self.show_button = Button(self.lgn_frame, image=self.show_image, command=self.show, relief=FLAT,activebackground="white", borderwidth=0, background="#3B3C36", cursor="hand2")
        self.show_button.place(x=860, y=420)
        self.password_entry.config(show='*')

    

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

            # self.play_welcome_audio_pygame(username)
            self.play_welcome_audio_pyttsx3(username)

            # Open a new window
            new_window = tk.Toplevel(self.window)
            new_window.title("Welcome")
            new_window.geometry("1080x760")
            new_window.state('zoomed')
            new_window.configure(bg='#F7E7CE')
            self.withdraw()

            

            label = Label(new_window, text=f"Welcome {username}, to our simple and easy to use bank app!", font=('yu gothic ui', 16, 'bold'), bg='#FF4F00', fg='white')
            label.place(x=50, y=50)

            # Play a welcome audio
            # if self.check_internet():
                # If there is an internet connection, use pygame
            
            # else:
                # If there is no internet connection, use pyttsx3
                # 
        else:
            messagebox.showerror("Login Error", "Invalid username or password")

        conn.close()

    
    def play_sound(text, username):
        tts = gTTS(text=f"Welcome, {username}", lang='en')
        tts.save("welcome.mp3")
        pygame.init()
        pygame.mixer.init()
        pygame.mixer.music.load("welcome.mp3")
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy() == True:
            continue
        os.remove("welcome.mp3")

    def play_welcome_audio_pyttsx3(self, username):
        engine = pyttsx3.init()
        engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0')
        engine.setProperty('rate', 150)  # Set the speech rate
        engine.say(f"Welcome, {username}!")
        engine.runAndWait()

    # def check_internet(self):
    #     hostname = "8.8.8.8"  # Google's public DNS server
    #     response = os.system("ping -c 1 " + hostname)

    #     # check the response...
    #     if response == 0:
    #         return True
    #     else:
    #         return False
    
    # def check_wifi_connection(self):
    #     try:
    #         output = subprocess.check_output(["netsh", "wlan", "show", "interfaces"])
    #         output = output.decode("utf-8")
    #         for line in output.split("\n"):
    #             if "SSID" in line:
    #                 ssid = line.split(":")[1].strip()
    #                 if ssid:
    #                     return True
    #         return False
    #     except subprocess.CalledProcessError:
    #         return False


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
        

class NewWindow(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("New Window")
        self.geometry("400x200")
        self.state('zoomed')
        self.master = master

        # background image
        self.bg_image = Image.open('yellowSho2.png')
        self.bg_photo = ImageTk.PhotoImage(self.bg_image)
        self.bg_label = tk.Label(self, image=self.bg_photo)
        self.bg_label.image = self.bg_photo
        self.bg_label.pack(fill='both', expand='yes')


        # red frame at the center
        self.lgn_frame = tk.Frame(self, bg='#7C0902', width='950', height="600")
        self.lgn_frame.place(x=300, y=100)

        # welcome text
        self.txt = """WELCOME TO PAMPROSTEES BANK"""
        self.heading = Label(self.lgn_frame, text=self.txt, font=('yu gothic ui', 25, 'bold'), bg='#7C0902', fg='white')
        self.heading.place(x=0, y=5, width=550, height=100)
        
        # login button pic and button function
        self.lgn_button = Image.open('btn1.png')
        photo = ImageTk.PhotoImage(self.lgn_button)
        self.lgn_button_label = Label(self.lgn_frame, image=photo, bg='#7C0902')
        self.lgn_button_label.image = photo
        self.lgn_button_label.place(x=550, y=450)
        self.login = Button(self.lgn_button_label, text='REGISTER', font=("yu gothic ui", 13, "bold"), width=25, bd=0, bg='#3047ff', cursor='hand2', activebackground='#3047ff', fg='white', command=self.register)
        self.login.place(x=20, y=10)
        self.login = Button(self, text='GO BACK TO LOGIN PAGE', font=("yu gothic ui", 13, "bold"), width=25, bd=0, bg='#3047ff', cursor='hand2', activebackground='#3047ff', fg='white', command=self.register)
        self.login.place(x=20, y=30)
        
        # logo pic
        self.logoside = Image.open('ps2.png')
        logos = ImageTk.PhotoImage(self.logoside)
        self.logo_label = Label(self.lgn_frame, image=logos, width='400', height="500", bg='#7C0902')
        self.logo_label.image = logos
        self.logo_label.__reduce__()
        self.logo_label.place(x=2, y=105)
        
        # face login
        self.sign_in_image = Image.open('hyy.png')
        photo = ImageTk.PhotoImage(self.sign_in_image)
        self.sign_in_image_label = Label(self.lgn_frame, image=photo, bg='#7C0902')
        self.sign_in_image_label.image = photo
        self.sign_in_image_label.place(x=620, y=130)
        
        # Sign in text
        self.sign_in_label = Label(self.lgn_frame, text="Register and Join us😎!", bg="#3D0C02", fg="white", font=("yu gothic ui", 17, "bold"))
        self.sign_in_label.place(x=560, y=240)

        # Username Section
        self.username_label = Label(self.lgn_frame, text="Username", bg="#4B3621", fg="white", font=("yu gothic ui", 13, "bold"))
        self.username_label.place(x=550, y=300)

        self.username_entry = Entry(self.lgn_frame, highlightthickness=0, relief=FLAT, bg="#7C0902", fg="#6b6a69", font=("yu gothic ui ", 12, "bold"), insertbackground = '#6b6a69')
        self.username_entry.place(x=580, y=335, width=270)

        self.username_line = Canvas(self.lgn_frame, width=300, height=2.0, bg="#bdb9b1", highlightthickness=0)
        self.username_line.place(x=550, y=359)

                # ===== Username icon =========
        self.username_icon = Image.open('username_icon.png')
        photo = ImageTk.PhotoImage(self.username_icon)

        self.username_icon_label = Label(self.lgn_frame, image=photo, bg='#7C0902')
        self.username_icon_label.image = photo
        self.username_icon_label.place(x=550, y=332)

        # Password Section
        self.password_label = Label(self.lgn_frame, text="Password", bg="#4B3621", fg="white", font=("yu gothic ui", 13, "bold"))
        self.password_label.place(x=550, y=380)

        self.password_entry = Entry(self.lgn_frame, highlightthickness=0, relief=FLAT, bg="#7C0902", fg="#6b6a69", font=("yu gothic ui", 12, "bold"), show="*", insertbackground = '#6b6a69')
        self.password_entry.place(x=580, y=416, width=244)

        self.password_line = Canvas(self.lgn_frame, width=300, height=2.0, bg="#bdb9b1", highlightthickness=0)
        self.password_line.place(x=550, y=440)

        # ======== Password icon ================
        self.password_icon = Image.open('password_icon.png')
        photo = ImageTk.PhotoImage(self.password_icon)
        self.password_icon_label = Label(self.lgn_frame, image=photo, bg='#7C0902')
        self.password_icon_label.image = photo
        self.password_icon_label.place(x=550, y=414)

        
        # Password Icon
        self.password_icon = Image.open('password_icon.png')
        photo = ImageTk.PhotoImage(self.password_icon)
        self.password_icon_label = Label(self.lgn_frame, image=photo, bg='#7C0902')
        self.password_icon_label.image = photo
        self.password_icon_label.place(x=550, y=414)

        # ========= show/hide password ========
        self.show_image = ImageTk.PhotoImage \
            (file='show.png')

        self.hide_image = ImageTk.PhotoImage \
            (file='hide.png')

        self.show_button = Button(self.lgn_frame, image=self.show_image, command=self.show, relief=FLAT,activebackground="white", borderwidth=0, background="#7C0902", cursor="hand2")
        self.show_button.place(x=860, y=420)

    def show(self):
        self.hide_button = Button(self.lgn_frame, image=self.hide_image, command=self.hide, relief=FLAT, activebackground="white", borderwidth=0, background="#7C0902", cursor="hand2")
        self.hide_button.place(x=860, y=420)
        self.password_entry.config(show='')

    def hide(self):
        self.show_button = Button(self.lgn_frame, image=self.show_image, command=self.show, relief=FLAT,activebackground="white", borderwidth=0, background="#7C0902", cursor="hand2")
        self.show_button.place(x=860, y=420)
        self.password_entry.config(show='*')

    def register(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if not username or not password:
            messagebox.showerror("Error", "Please fill in both username and password")
            return

        # Connect to database
        conn = sqlite3.connect("users.db")
        c = conn.cursor()

        # Create table if it doesn't exist
        c.execute("""CREATE TABLE IF NOT EXISTS users (
            username TEXT PRIMARY KEY,
            password TEXT
        )""")

        # Insert new user
        c.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
        conn.commit()
        conn.close()

        messagebox.showinfo("Success", "User registered successfully!")
        self.username_entry.delete(0, tk.END)
        self.password_entry.delete(0, tk.END) 
        self.master.geometry(self.master.geometry_string)
        if self.master.state_string == 'zoomed':
            self.master.state('zoomed')
        else:
            self.master.state('normal')
        self.master.deiconify()



if __name__ == "__main__":
    app = LoginForm()
    app.mainloop()

