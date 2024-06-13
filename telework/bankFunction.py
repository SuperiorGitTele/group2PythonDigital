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