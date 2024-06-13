import tkinter as tk

class Sidebar(tk.Frame):
    def __init__(self, master, **kwargs):
        tk.Frame.__init__(self, master, **kwargs)
        self.master = master
        self.pack_forget()
        self.is_open = False

        self.label = tk.Label(self, text="Sidebar")
        self.label.pack(pady=10)

        self.button1 = tk.Button(self, text="Button 1")
        self.button1.pack(pady=5)

        self.button2 = tk.Button(self, text="Button 2")
        self.button2.pack(pady=5)

        self.button3 = tk.Button(self, text="Button 3")
        self.button3.pack(pady=5)

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

class MainApplication(tk.Frame):
    def __init__(self, master, **kwargs):
        tk.Frame.__init__(self, master, **kwargs)
        self.master = master
        self.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        self.label = tk.Label(self, text="Main Application")
        self.label.pack(pady=10)

        self.sidebar_button = tk.Button(self, text="Open/Close Sidebar", command=self.toggle_sidebar)
        self.sidebar_button.pack(pady=10)

        self.sidebar = Sidebar(master)

    def toggle_sidebar(self):
        self.sidebar.toggle()

root = tk.Tk()
root.title("Sidebar Example")

main_app = MainApplication(root)

root.mainloop()