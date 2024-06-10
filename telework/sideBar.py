import tkinter as tk

class Sidebar(tk.Frame):
    def __init__(self, master, **kwargs):
        tk.Frame.__init__(self, master, **kwargs)
        self.master = master
        self.pack_forget()
        self.is_open = False

        self.label = tk.Label(self, text="Sidebar", font=('yu gothic ui', 16, 'bold'), bg='#3B3C36', fg='white')
        self.label.place(x=10, y=10)

        self.button1 = tk.Button(self, text="Dashboard", font=('yu gothic ui', 13, 'bold'), width=20, bd=0, bg='#3047ff', cursor='hand2', activebackground='#3047ff', fg='white')
        self.button1.place(x=10, y=50)

        self.button2 = tk.Button(self, text="Transactions", font=('yu gothic ui', 13, 'bold'), width=20, bd=0, bg='#3047ff', cursor='hand2', activebackground='#3047ff', fg='white')
        self.button2.place(x=10, y=90)

        self.button3 = tk.Button(self, text="Account Settings", font=('yu gothic ui', 13, 'bold'), width=20, bd=0, bg='#3047ff', cursor='hand2', activebackground='#3047ff', fg='white')
        self.button3.place(x=10, y=130)

    def toggle(self):
        if self.is_open:
            self.place_forget()
            self.is_open = False
        else:
            self.place(x=0, y=0, relwidth=0.2, relheight=1)
            self.is_open = True
            self.animate_open()

    def animate_open(self):
        if self.winfo_x() < 0:
            self.place(x=self.winfo_x() + 1, y=0, relwidth=0.2, relheight=1)
            self.after(10, self.animate_open)
        else:
            self.place(x=0, y=0, relwidth=0.2, relheight=1)

