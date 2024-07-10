import tkinter as tk
from PIL import Image, ImageTk
from tkinter import ttk, filedialog

class Sidebar(tk.Frame):
    def __init__(self, master,**kwargs):
        tk.Frame.__init__(self, master, **kwargs)
        self.master = master
        self.is_open = False
        self.image_path = None
        self.configure(bg="#3B3C36")


        # Open the image file
        image = Image.open("bar12.png")
        image = image.resize((40, 40), resample=Image.LANCZOS)
        dropdown_image = ImageTk.PhotoImage(image)
        self.sidebar_button = tk.Button(self, image=dropdown_image, compound="top", font=("yu gothic ui", 4, "bold"), width=70, bd=0, bg='#3B3C36', cursor='hand2', activebackground='#3B3C36', fg='white', command=self.close_sidebar)
        self.sidebar_button.image = dropdown_image
        self.sidebar_button.place(x=10, y=0)

        logoside2 = Image.open('femalelogo.png')
        logoside2 = logoside2.resize((80, 80), resample=Image.LANCZOS)
        logos = ImageTk.PhotoImage(logoside2)
        logo_label3 = tk.Label(self, image=logos, bg='#3B3C36')
        logo_label3.image = logos
        logo_label3.__reduce__()
        logo_label3.place(x=70, y=85)
        
        

        self.username_label = tk.Label(self, text=f": Signed in", bg='#3B3C36', fg="white")
        self.username_label.place(x=70, y=180)


        # Buttons
        self.button1 = tk.Button(self, text="Activities", font=('yu gothic ui', 13, 'bold'), width=20, bd=0, bg='#0095B6', cursor='hand2', activebackground='#3047ff', fg='white', command=self.dashboard)
        self.button1.place(x=20, y=250)

        self.button2 = tk.Button(self, text="Account Details", font=('yu gothic ui', 13, 'bold'), width=20, bd=0, bg='#0095B6', cursor='hand2', activebackground='#3047ff', fg='white', command=self.AcctDetail)
        self.button2.place(x=20, y=350)

        self.button3 = tk.Button(self, text="Settings", font=('yu gothic ui', 11, 'bold'), width=22, bd=0, bg='#0095B6', cursor='hand2', activebackground='#3047ff', fg='white', command=self.setting)
        self.button3.place(x=20, y=450)

    def dashboard(self):
        dashboard = tk.Toplevel(self.master)
        dashboard.title("Dashboard")
        dashboard.configure(bg='#003262')
        img = ImageTk.PhotoImage(file='logo.png')
        dashboard.iconphoto(False, img)
        dashboard.grab_set()

        # Set size of the dashboard dialog
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

        dashboard.geometry(f"{dialog_width}x{dialog_height}+{x}+{y}")

        # Add welcome message
        tk.Label(dashboard, text="Welcome to Your Dashboard", bg="#003262", fg="white", font=('Arial', 20, 'bold')).place(x=60, y=20)

        

        # tk.Label(quick_actions_frame, text="Quick Actions", bg="#003262", fg="white", font=('Arial', 14, 'bold')).pack(anchor='w')
        # tk.Button(quick_actions_frame, text="Transfer Funds", font=('Arial', 12), bg='#0095B6', fg='white', cursor='hand2').pack(anchor='w', pady=5)
        # tk.Button(quick_actions_frame, text="Pay Bills", font=('Arial', 12), bg='#0095B6', fg='white', cursor='hand2').pack(anchor='w', pady=5)
        # tk.Button(quick_actions_frame, text="Deposit Checks", font=('Arial', 12), bg='#0095B6', fg='white', cursor='hand2').pack(anchor='w', pady=5)


        # label = tk.Label(activities, text="Text", bg="#0095B6", font=('Arial', 12))
        # label.place(x=50, y=50)

        logoside = Image.open('femalelogo.png')
        logoside = logoside.resize((80, 80), resample=Image.LANCZOS)
        logos = ImageTk.PhotoImage(logoside)
        logo_labe = tk.Label(dashboard, image=logos, bg='#003262')
        logo_labe.image = logos
        logo_labe.__reduce__()
        logo_labe.place(x=40, y=70)

        self.logo_label = tk.Label(dashboard, bg='#003262')
        self.logo_label.place(x=40, y=70)

        def load_image_from_path():
            if self.image_path:
                image = Image.open(self.image_path)
                image = image.resize((80, 80), resample=Image.LANCZOS)
                self.logos = ImageTk.PhotoImage(image)
                self.logo_label.config(image=self.logos)
                logo_labe.place_forget()

        
        def upload_photo():
            file_path = filedialog.askopenfilename()
            if file_path:
                self.image_path = file_path
                # Save image path to a configuration file or database for persistence
                with open('image_path.txt', 'w') as f:
                    f.write(self.image_path)
                load_image_from_path()
                
        
        upload_button = tk.Button(dashboard, text="Upload Photo", command=upload_photo)
        upload_button.place(x=40, y=160)

        load_image_from_path()

 


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
