import tkinter as tk
from PIL import Image, ImageTk

class Sidebar(tk.Frame):
    def __init__(self, master, **kwargs):
        tk.Frame.__init__(self, master, **kwargs)
        self.master = master
        self.is_open = False
        self.configure(bg="#3B3C36")


        # Open the image file
        image = Image.open("bar12.png")

        # Resize the image
        image = image.resize((20, 30), resample=Image.LANCZOS)  # Replace (20, 20) with your desired size

        # Convert the image to a PhotoImage
        dropdown_image = ImageTk.PhotoImage(image)

        self.sidebar_button = tk.Button(self, image=dropdown_image, compound="top", font=("yu gothic ui", 4, "bold"), width=70, bd=0, bg='#3B3C36', cursor='hand2', activebackground='#3B3C36', fg='white', command=self.close_sidebar)
        self.sidebar_button.image = dropdown_image
        self.sidebar_button.place(x=10, y=2)

        # Logo picture
        self.logoside = Image.open('logopng.png')
        self.logoside = self.logoside.resize((80, 80), resample=Image.LANCZOS)  # Resize the image to 80x80 pixels using Lanczos resampling
        logos = ImageTk.PhotoImage(self.logoside)
        self.logo_label = tk.Label(self.master, image=logos, width=80, height=80, bg='#3B3C36')
        self.logo_label.image = logos  # Keep a reference to the image
        self.logo_label.place(x=70, y=0)

        # Buttons
        self.button1 = tk.Button(self, text="Dashboard", font=('yu gothic ui', 13, 'bold'), width=20, bd=0, bg='#0095B6', cursor='hand2', activebackground='#3047ff', fg='white', command=self.dashboard)
        self.button1.place(x=20, y=200)

        self.button3 = tk.Button(self, text="Account Details", font=('yu gothic ui', 13, 'bold'), width=20, bd=0, bg='#0095B6', cursor='hand2', activebackground='#3047ff', fg='white', command=self.AccountDetail)
        self.button3.place(x=20, y=300)

    def dashboard(self):
        dashboard_dialog = tk.Toplevel(self.master)
        dashboard_dialog .title("Dashboard")
        dashboard_dialog.configure(bg='#003262')
        img = ImageTk.PhotoImage(file='logo.png')
        dashboard_dialog.iconphoto(False, img)
        dashboard_dialog.grab_set()

        
        # Set size of the fund account dialog
        dialog_width = 600
        dialog_height = 500

        # Center the dialog relative to the parent window (self.new_window)
        parent_x = self.master.winfo_x()
        parent_y = self.master.winfo_y()
        parent_width = self.master.winfo_width()
        parent_height = self.master.winfo_height()

        # Calculate the position
        x = parent_x + (parent_width // 2) - (dialog_width // 2)
        y = parent_y + (parent_height // 2) - (dialog_height // 2)

        dashboard_dialog.geometry(f"{dialog_width}x{dialog_height}+{x}+{y}")





        # Create a button to open the dashboard
        self.dashboard_button = tk.Button(self.master, text="Open Dashboard", command=self.dashboard)
        self.dashboard_button.pack(pady=20)

    def dashboard(self):
        dashboard_dialog = tk.Toplevel(self.master)
        dashboard_dialog.title("Dashboard")
        dashboard_dialog.configure(bg='#003262')
        img = ImageTk.PhotoImage(file='logo.png')
        dashboard_dialog.iconphoto(False, img)
        dashboard_dialog.grab_set()

        # Set size of the fund account dialog
        dialog_width = 600
        dialog_height = 500

        # Center the dialog relative to the parent window (self.master)
        parent_x = self.master.winfo_x()
        parent_y = self.master.winfo_y()
        parent_width = self.master.winfo_width()
        parent_height = self.master.winfo_height()

        # Calculate the position
        x = parent_x + (parent_width // 2) - (dialog_width // 2)
        y = parent_y + (parent_height // 2) - (dialog_height // 2)

        dashboard_dialog.geometry(f"{dialog_width}x{dialog_height}+{x}+{y}")

        # Personal Information Section
        tk.Label(dashboard_dialog, text="Update Personal Information", bg='#003262', fg='white', font=('Arial', 10)).pack(pady=5)

        # Name Entry
        tk.Label(dashboard_dialog, text="Acct Name:", bg='#003262', fg='white', font=('Arial', 12)).pack(anchor='w', padx=20)
        name_entry = tk.Entry(dashboard_dialog, width=40)
        name_entry.pack(pady=5, padx=20)

        # Account number Entry
        tk.Label(dashboard_dialog, text="Account number:", bg='#003262', fg='white', font=('Arial', 12)).pack(anchor='w', padx=20)
        email_entry = tk.Entry(dashboard_dialog, width=40)
        email_entry.pack(pady=5, padx=20)


        # Email Entry
        tk.Label(dashboard_dialog, text="Email:", bg='#003262', fg='white', font=('Arial', 12)).pack(anchor='w', padx=20)
        email_entry = tk.Entry(dashboard_dialog, width=40)
        email_entry.pack(pady=5, padx=20)

        # Phone Number Entry
        tk.Label(dashboard_dialog, text="Phone Number:", bg='#003262', fg='white', font=('Arial', 12)).pack(anchor='w', padx=20)
        phone_entry = tk.Entry(dashboard_dialog, width=40)
        phone_entry.pack(pady=5, padx=20)

        # Save Button
        save_button = tk.Button(dashboard_dialog, text="Save", command=lambda: self.save_information(name_entry.get(), email_entry.get(), phone_entry.get()))
        save_button.pack(pady=20)

    # def save_information(self, name, email, phone):
    #     # Here you would typically save this information to a database or a file
    #     messagebox.showinfo("Information Saved", f"Name: {name}\nEmail: {email}\nPhone: {phone}")




    def AccountDetail(self):
        AccountDetail_dialog = tk.Toplevel(self.master)
        AccountDetail_dialog.title("Account Details")
        AccountDetail_dialog.configure(bg='#003262')
        img = ImageTk.PhotoImage(file='logo.png')
        AccountDetail_dialog.iconphoto(False, img)
        AccountDetail_dialog.grab_set()

        # Set size of the fund account dialog
        dialog_width = 600
        dialog_height = 500

        # Center the dialog relative to the parent window (self.master)
        parent_x = self.master.winfo_x()
        parent_y = self.master.winfo_y()
        parent_width = self.master.winfo_width()
        parent_height = self.master.winfo_height()

        # Calculate the position
        x = parent_x + (parent_width // 2) - (dialog_width // 2)
        y = parent_y + (parent_height // 2) - (dialog_height // 2)

        AccountDetail_dialog.geometry(f"{dialog_width}x{dialog_height}+{x}+{y}")

    

    def toggle(self):
            self.animate_open()
            if self.is_open:
                self.is_open = True

    def close_sidebar(self):
        self.animate_close()

    def animate_open(self):
        # Animate the opening of the sidebar
        if self.winfo_x() > -self.winfo_width():
            self.place(x=self.winfo_x() - 20, y=0, relwidth=0.2, relheight=1)
            self.after(10, self.animate_open)
        else:
            self.place(x=0, y=0, relwidth=0.2, relheight=1)
            self.is_open = True

    def animate_close(self):
        # Animate the closing of the sidebar
        if self.winfo_x() < 0:
            self.place(x=self.winfo_x() + 20, y=0, relwidth=0.2, relheight=1)
            self.after(10, self.animate_close)
        else:
            self.place_forget()
            self.is_open = False

# Example usage
if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("1200x600")  # Set window size

    sidebar = Sidebar(root, bg='#3B3C36')
    sidebar.place(x=0, y=0, relwidth=0.2, relheight=1)  # Initially place it in view

    # Toggle button to show/hide sidebar
    # toggle_button = tk.Button(root, text="Toggle Sidebar", command=sidebar.toggle)
    # toggle_button.pack(pady=20)

    root.mainloop()
