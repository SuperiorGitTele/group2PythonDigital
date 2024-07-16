import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk

class WelcomeWindow:
    def __init__(self, master):
        self.master = master
        self.master.title("Subscription Service")
        self.master.configure(bg='#003262')

        # Adjust main window size
        self.master.geometry("500x300")

        img = ImageTk.PhotoImage(file='logo.png')
        self.master.iconphoto(False, img)

        # Frame for buttons to place them on the same line
        button_frame = tk.Frame(self.master, bg='#003262')
        button_frame.pack(pady=50)

        # Subscription options with increased button size
        tk.Button(button_frame, text="Buy Airtime", command=lambda: self.new_window("Airtime"), width=20, height=2).grid(row=0, column=0, padx=10)
        tk.Button(button_frame, text="Buy Data", command=lambda: self.new_window("Data"), width=20, height=2).grid(row=0, column=1, padx=10)

    def new_window(self, subscription_type):
        new_win = tk.Toplevel(self.master)
        new_win.title(f"Buy {subscription_type}")
        new_win.configure(bg='#003262')

        # Adjust subscription window size
        new_win.geometry("400x300")

        tk.Label(new_win, text=f"Enter your phone number to buy {subscription_type}", bg='#003262', fg='white').pack(padx=10, pady=10)
        self.phone_var = tk.StringVar()
        tk.Entry(new_win, textvariable=self.phone_var).pack(padx=10, pady=10)

        tk.Label(new_win, text="Enter the amount", bg='#003262', fg='white').pack(padx=10, pady=10)
        self.amount_var = tk.StringVar()
        tk.Entry(new_win, textvariable=self.amount_var).pack(padx=10, pady=10)

        tk.Button(new_win, text="Submit", command=lambda: self.submit(new_win, subscription_type)).pack(pady=10)

    def submit(self, window, subscription_type):
        phone_number = self.phone_var.get()
        amount = self.amount_var.get()

        if not phone_number:
            messagebox.showwarning("Input Error", "Please enter your phone number.")
            return
        
        if not amount:
            messagebox.showwarning("Input Error", "Please enter the amount.")
            return
        
        # Close the input window
        window.destroy()

        # Show a receipt
        self.show_receipt(subscription_type, phone_number, amount)

    def show_receipt(self, subscription_type, phone_number, amount):
        receipt_win = tk.Toplevel(self.master)
        receipt_win.title("Receipt")
        receipt_win.configure(bg='#003262')

        # Adjust receipt window size
        receipt_win.geometry("400x300")

        receipt_text = (
            f"Receipt\n\n"
            f"Subscription Type: {subscription_type}\n"
            f"Phone Number: {phone_number}\n"
            f"Amount: {amount}\n"
        )

        tk.Label(receipt_win, text=receipt_text, font=("Helvetica", 12), bg='#003262', fg='white').pack(padx=20, pady=20)
        tk.Button(receipt_win, text="Close", command=receipt_win.destroy).pack(pady=10)

if __name__ == "__main__":
    root = tk.Tk()
    app = WelcomeWindow(root)
    root.mainloop()
