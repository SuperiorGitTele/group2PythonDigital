import tkinter as tk
from tkinter import messagebox

class SubscriptionWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Airtime and Data Subscription")
        
        # Airtime Subscription Button
        tk.Button(root, text="Buy Airtime", command=self.open_airtime_window).grid(row=0, column=0, padx=10, pady=10)
        
        # Data Subscription Button
        tk.Button(root, text="Buy Data", command=self.open_data_window).grid(row=0, column=1, padx=10, pady=10)
    
    def open_airtime_window(self):
        self.new_window("Airtime")

    def open_data_window(self):
        self.new_window("Data")

    def new_window(self, subscription_type):
        new_win = tk.Toplevel(self.root)
        new_win.title(f"Buy {subscription_type}")
        
        tk.Label(new_win, text=f"Enter your phone number to buy {subscription_type}").grid(row=0, column=0, padx=10, pady=10)
        self.phone_var = tk.StringVar()
        tk.Entry(new_win, textvariable=self.phone_var).grid(row=1, column=0, padx=10, pady=10)
        
        tk.Button(new_win, text="Submit", command=lambda: self.submit(subscription_type)).grid(row=2, column=0, pady=10)

    def submit(self, subscription_type):
        phone_number = self.phone_var.get()
        
        if not phone_number:
            messagebox.showwarning("Input Error", "Please enter your phone number.")
            return
        
        # Here you can add the logic to handle the subscription
        # For demonstration, we just show a success message
        messagebox.showinfo("Subscription Successful", f"Subscribed to {subscription_type} for phone number {phone_number}.")

# if __name__ == "__main__":
#     root = tk.Tk()
#     app = SubscriptionWindow(root)
#     root.mainloop()
