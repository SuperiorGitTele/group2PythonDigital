
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
# import function





class NewWindow(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("Register with PROPATEES")
        self.master = master
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
        self.txt = """WELCOME TO PROPATEES BANK"""
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
        self.login = Button(self, text='GO BACK TO LOGIN PAGE', font=("yu gothic ui", 13, "bold"), width=25, bd=0, bg='#3047ff', cursor='hand2', activebackground='#3047ff', fg='white', command=self.go_backLogin)
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

        # Date of Birth Section
        self.dob_label = Label(self.lgn_frame, text="Date of Birth", bg="#4B3621", fg="white", font=("yu gothic ui", 13, "bold"))
        self.dob_label.place(x=350, y=300)

        self.dob_entry = Entry(self.lgn_frame, highlightthickness=0, relief=FLAT, bg="#7C0902", fg="#6b6a69", font=("yu gothic ui ", 12, "bold"), insertbackground = '#6b6a69')
        self.dob_entry.place(x=380, y=340, width=100)

        self.dob_line = Canvas(self.lgn_frame, width=75, height=2.0, bg="#bdb9b1", highlightthickness=0)
        self.dob_line.place(x=380, y=360)

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
        self.dob_entry.bind("<Return>", lambda event: self.register())

        self.password_line = Canvas(self.lgn_frame, width=300, height=2.0, bg="#bdb9b1", highlightthickness=0)
        self.password_line.place(x=550, y=440)

        def focus_password_entry(self, event=None):
            self.password_entry.focus()

        # Bind the Enter key to focus on the password entry field
        self.username_entry.bind("<Return>", lambda event: focus_password_entry(self))

        def focus_password_entry1(self, event=None):
            self.dob_entry.focus()

        # Bind the Enter key to focus on the password entry field
        self.password_entry.bind("<Return>", lambda event: focus_password_entry1(self))

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
            (file='hide.png')

        self.hide_image = ImageTk.PhotoImage \
            (file='show.png')

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
        dob = self.dob_entry.get()

        if not username or not password or not dob:
            messagebox.showerror("Error", "Please fill in all fields: username, password, and date of birth")
            return

        # Parse the date of birth
        try:
            day, month, year = map(int, dob.split('/'))
            dob = f"{year}-{month:02d}-{day:02d}"
        except ValueError:
            messagebox.showerror("Error", "Invalid date of birth format. Please use DD/MM/YYYY")
            return

        # Connect to database
        conn = sqlite3.connect("users.db")
        c = conn.cursor()

        # Create table if it doesn't exist
        c.execute("""CREATE TABLE IF NOT EXISTS users (
            username TEXT PRIMARY KEY,
            password TEXT,
            dob DATE
        )""")

        # Check if username already exists
        c.execute("SELECT 1 FROM users WHERE username=?", (username,))
        if c.fetchone():
            messagebox.showerror("Error", "Username already exists. Please choose a different username.")
            conn.close()
            return

        # Insert new user
        c.execute("INSERT INTO users (username, password, dob) VALUES (?, ?, ?)", (username, password, dob))
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
        self.withdraw()
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