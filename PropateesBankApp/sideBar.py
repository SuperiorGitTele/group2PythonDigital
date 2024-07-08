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
        image = image.resize((20, 30), resample=Image.LANCZOS)
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
        self.button1 = tk.Button(self, text="Activities", font=('yu gothic ui', 13, 'bold'), width=20, bd=0, bg='#0095B6', cursor='hand2', activebackground='#3047ff', fg='white', command=self.activities)
        self.button1.place(x=20, y=200)

        self.button2 = tk.Button(self, text="Account Details", font=('yu gothic ui', 13, 'bold'), width=20, bd=0, bg='#0095B6', cursor='hand2', activebackground='#3047ff', fg='white', command=self.AcctDetail)
        self.button2.place(x=20, y=300)

        self.button3 = tk.Button(self, text="Settings", font=('yu gothic ui', 11, 'bold'), width=22, bd=0, bg='#0095B6', cursor='hand2', activebackground='#3047ff', fg='white', command=self.setting)
        self.button3.place(x=20, y=400)

    def activities(self):
        activities = tk.Toplevel(self.master)
        activities.title("Login Activities")
        activities.configure(bg='#003262')
        img = ImageTk.PhotoImage(file='logo.png')
        activities.iconphoto(False, img)
        activities.grab_set()

        # Set size of the fund account dialog
        dialog_width = 600
        dialog_height = 600

        # Center the dialog relative to the parent window (self.master)
        parent_x = self.master.winfo_x()
        parent_y = self.master.winfo_y()
        parent_width = self.master.winfo_width()
        parent_height = self.master.winfo_height()

        # Calculate the position
        x = parent_x + (parent_width // 2) - (dialog_width // 2)
        y = parent_y + (parent_height // 2) - (dialog_height // 2)

        activities.geometry(f"{dialog_width}x{dialog_height}+{x}+{y}")

        label = tk.Label(activities, text="Text", bg="#0095B6")
        label.place(x=50, y=50)
 


    def AcctDetail(self):
        AcctDetail = tk.Toplevel(self.master)
        AcctDetail.title("Activities")
        AcctDetail.configure(bg='#0095B6')
        img = ImageTk.PhotoImage(file='logo.png')
        AcctDetail.iconphoto(False, img)
        AcctDetail.grab_set()

        # Set size of the fund account dialog
        dialog_width = 600
        dialog_height = 600

        # Center the dialog relative to the parent window (self.master)
        parent_x = self.master.winfo_x()
        parent_y = self.master.winfo_y()
        parent_width = self.master.winfo_width()
        parent_height = self.master.winfo_height()

        # Calculate the position
        x = parent_x + (parent_width // 2) - (dialog_width // 2)
        y = parent_y + (parent_height // 2) - (dialog_height // 2)

        AcctDetail.geometry(f"{dialog_width}x{dialog_height}+{x}+{y}")

    def setting(self):
        setting = tk.Toplevel(self.master)
        setting.title("Activities")
        setting.configure(bg='#003262')
        img = ImageTk.PhotoImage(file='logo.png')
        setting.iconphoto(False, img)
        setting.grab_set()

        # Set size of the fund account dialog
        dialog_width = 600
        dialog_height = 600

        # Center the dialog relative to the parent window (self.master)
        parent_x = self.master.winfo_x()
        parent_y = self.master.winfo_y()
        parent_width = self.master.winfo_width()
        parent_height = self.master.winfo_height()

        # Calculate the position
        x = parent_x + (parent_width // 2) - (dialog_width // 2)
        y = parent_y + (parent_height // 2) - (dialog_height // 2)

        setting.geometry(f"{dialog_width}x{dialog_height}+{x}+{y}")

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
    sidebar.place(x=0, y=0, relwidth=0.2, relheight=1)  

    root.mainloop()
