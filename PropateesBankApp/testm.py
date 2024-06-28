import subprocess
import tkinter as tk
from tkinter import messagebox
import pygame

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.username = tk.Entry(self)
        self.username.pack(side="top")

        self.submit = tk.Button(self)
        self.submit["text"] = "Submit"
        self.submit["command"] = self.check_wifi_and_play_sound
        self.submit.pack(side="top")

    def check_wifi_and_play_sound(self):
        if self.check_wifi_connection():
            messagebox.showinfo("Pygame successful!", "You are connected to a WiFi network!")
            self.play_sound(self.username.get())
        else:
            messagebox.showinfo("Error", "You are not connected to a WiFi network!")

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

    def play_sound(self, username):
        pygame.init()
        pygame.mixer.music.load("welcome.mp3")
        pygame.mixer.music.play()
        print(f"Welcome, {username}!")

root = tk.Tk()
app = Application(master=root)
app.mainloop()