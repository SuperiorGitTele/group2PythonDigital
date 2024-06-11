import tkinter as tk
from PIL import Image, ImageTk

class Sidebar(tk.Frame):
    def __init__(self, master, **kwargs):
        tk.Frame.__init__(self, master, **kwargs)
        self.master = master
        self.is_open = False
        self.configure(bg="#3B3C36")

        # Close button
        # self.close_button = tk.Button(self, text="X", font=('yu gothic ui', 16, 'bold'), bg='#3B3C36', fg='white', command=self.close_sidebar)
        # self.close_button.place(x=10, y=10)

        # Open the image file
        image = Image.open("drop.png")

        # Resize the image
        image = image.resize((20, 20), resample=Image.LANCZOS)  # Replace (20, 20) with your desired size

        # Convert the image to a PhotoImage
        dropdown_image = ImageTk.PhotoImage(image)

        self.sidebar_button = tk.Button(self, image=dropdown_image, compound="top", font=("yu gothic ui", 4, "bold"), width=70, bd=0, bg='red', cursor='hand2', activebackground='#3B3C36', fg='white', command=self.close_sidebar)
        self.sidebar_button.image = dropdown_image
        self.sidebar_button.place(x=10, y=2)

        # Logo picture
        self.logoside = Image.open('ps2.png')
        self.logoside = self.logoside.resize((80, 80), resample=Image.LANCZOS)  # Resize the image to 80x80 pixels using Lanczos resampling
        logos = ImageTk.PhotoImage(self.logoside)
        self.logo_label = tk.Label(self.master, image=logos, width=80, height=80, bg='#3B3C36')
        self.logo_label.image = logos  # Keep a reference to the image
        self.logo_label.place(x=70, y=0)

        # Buttons
        self.button1 = tk.Button(self, text="Dashboard", font=('yu gothic ui', 13, 'bold'), width=20, bd=0, bg='#3047ff', cursor='hand2', activebackground='#3047ff', fg='white')
        self.button1.place(x=10, y=200)

        self.button2 = tk.Button(self, text="Transactions", font=('yu gothic ui', 13, 'bold'), width=20, bd=0, bg='#3047ff', cursor='hand2', activebackground='#3047ff', fg='white')
        self.button2.place(x=10, y=300)

        self.button3 = tk.Button(self, text="Account Settings", font=('yu gothic ui', 13, 'bold'), width=20, bd=0, bg='#3047ff', cursor='hand2', activebackground='#3047ff', fg='white')
        self.button3.place(x=10, y=500)

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

# # Example usage
# if __name__ == "__main__":
#     root = tk.Tk()
#     root.geometry("1200x600")  # Set window size

#     sidebar = Sidebar(root, bg='#3B3C36')
#     sidebar.place(x=0, y=0, relwidth=0.2, relheight=1)  # Initially place it in view

#     # Toggle button to show/hide sidebar
#     # toggle_button = tk.Button(root, text="Toggle Sidebar", command=sidebar.toggle)
#     # toggle_button.pack(pady=20)

#     root.mainloop()
