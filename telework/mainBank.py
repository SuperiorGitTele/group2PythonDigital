import tkinter as tk
from tkinter import ttk
import sqlite3
from sideBar import Sidebar
from PIL import Image, ImageTk

class WelcomeWindow:
    def __init__(self, master, username):
        self.master = master
        self.username = username
        self.new_window = tk.Toplevel(self.master)
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

        self.lgn_frame = tk.Frame(self.new_window, bg='#3B3C36', bd=5, height=220, width=1528)
        self.lgn_frame.place(x=0, y=0)

        label = tk.Label(self.lgn_frame, text=f"Welcome {username}, to our simple and easy to use bank app!", font=('yu gothic ui', 16, 'bold'), bg='#FF4F00', fg='white')
        label.place(x=60, y=34)

        style = ttk.Style()
        style.configure("Big.TButton", font=("Arial", 17), foreground="red", background="black")

        # Create a Button to check the account balance
        self.check_balance_button = ttk.Button(self.lgn_frame, text="Check Balance", style="Big.TButton", command=lambda: self.toggle_balance(username))
        self.check_balance_button.place(x=100, y=120)

        # Create a Button to check the account balance
        self.check_balance_button = ttk.Button(self.lgn_frame, text="TRANSFER", style="Big.TButton")
        self.check_balance_button.place(x=300, y=120)

        # 
        self.check_balance_button = ttk.Button(self.lgn_frame, text="""FUND YOUR ACCOUNT YOUR 
OTHER PTP ACCOUNT""", style="Big.TButton")
        self.check_balance_button.place(x=600, y=120)

        self.check_balance_button = ttk.Button(self.lgn_frame, text="SUBSCRIPTION", style="Big.TButton")
        self.check_balance_button.place(x=1000, y=120)

        # Create a Label to display the account balance
        self.balance_label = None

        loginpage = tk.Button(self.new_window, text='LOG OUT', font=("yu gothic ui", 13, "bold"), width=10, bd=0, bg='#3047ff', cursor='hand2', activebackground='#3047ff', fg='white', command=self.go_backLogin1)
        loginpage.place(x=1400, y=700)

        # self.sidebar_button = tk.Button(self.lgn_frame, text="------\n------\n-------", font=("yu gothic ui", 13, "bold"), width=15, bd=0, bg='#3047ff', cursor='hand2', activebackground='#3047ff', fg='white', command=self.toggle_sidebar)
        # self.sidebar_button.place(x=1000, y=10)

        # Open the image file
        image = Image.open("drop.png")

        # Resize the image
        image = image.resize((20, 20), resample=Image.LANCZOS)  # Replace (20, 20) with your desired size

        # Convert the image to a PhotoImage
        dropdown_image = ImageTk.PhotoImage(image)

        self.sidebar_button = tk.Button(self.lgn_frame, image=dropdown_image, compound="top", font=("yu gothic ui", 4, "bold"), width=70, bd=0, bg='red', cursor='hand2', activebackground='#3B3C36', fg='white', command=self.toggle_sidebar)
        self.sidebar_button.image = dropdown_image
        self.sidebar_button.place(x=320, y=0)

        self.settings = tk.StringVar()
        self.settings.set("Settings")  # default value

        self.sidebar_menu = ttk.OptionMenu(self.lgn_frame, self.settings, "Change UserName", "Edit Account Details", command=self.toggle_sidebar)
        self.sidebar_menu.place(x=1400, y=10)

        self.sidebar = None

    def toggle_sidebar(self):
        if self.sidebar is None:
            self.sidebar = Sidebar(self.new_window)
            self.sidebar.place(x=1528, y=0, relwidth=0.2, relheight=1)
        self.sidebar.toggle()

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
            self.balance_label = ttk.Label(self.lgn_frame, text=f"Account Balance: {account_balance}", style="Big.TLabel", background="red")
            self.balance_label.place(x=100, y=160)
        else:
            self.balance_label.place_forget()
            self.balance_label = None

    def go_backLogin1(self):
        self.new_window.withdraw()
        self.master.deiconify()


# root = tk.Tk()
# welcome_window = WelcomeWindow(root, "username")
# root.withdraw()  # Hide the root window
# welcome_window.new_window.mainloop()