import tkinter as tk
from tkinter import messagebox
import pygame
from gtts import gTTS
import os
import time

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.username_label = tk.Label(self, text="Enter your username:")
        self.username_label.pack()

        self.username_entry = tk.Entry(self)
        self.username_entry.pack()

        self.submit_button = tk.Button(self)
        self.submit_button["text"] = "Submit"
        self.submit_button["command"] = self.play_audio
        self.submit_button.pack()

    def play_audio(self):
        username = self.username_entry.get()
        if username:
            tts = gTTS(text=f"Welcome, {username}!", lang='en')
            tts.save("welcome.mp3")
            pygame.mixer.init()
            pygame.mixer.music.load("welcome.mp3")
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy() == True:
                time.sleep(0.1)  # wait for the audio to finish playing
            pygame.mixer.quit()  # quit Pygame to release the file
            os.remove("welcome.mp3")
            messagebox.showinfo("Welcome", f"Welcome, {username}!")
        else:
            messagebox.showerror("Error", "Please enter a username")

root = tk.Tk()
app = Application(master=root)
app.mainloop()