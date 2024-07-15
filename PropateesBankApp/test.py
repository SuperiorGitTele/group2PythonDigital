# import tkinter as tk
# from tkinter import filedialog
# from PIL import Image, ImageTk

# class App:
#     def __init__(self, master):
#         self.master = master
#         self.image_path = None
#         self.logos = None

#         self.fund_account_button = ttk.Button(self.new_window, text="""Fund your account 
# from your other 
# PTP account""", style="Big.TButton", command=self.show_fund_account_dialog)
#         self.fund_account_button.place(x=0, y=300)
        
#         # Button to open the directory dialog and select a directory
#         self.open_dir_button = tk.Button(master, text="Select Directory", command=self.open_directory)
#         self.open_dir_button.pack()

#         # Button to load the image from the path stored in image_path.txt
#         self.load_image_button = tk.Button(master, text="Load Image from Path", command=self.load_image_from_path)
#         self.load_image_button.pack()

#         # Placeholder for the image label
#         self.sign_in_image_label = tk.Label(master)
#         self.sign_in_image_label.pack()
    
#     def show_fund_account_dialog(self):
#         fund_account_dialog = tk.Toplevel(self.new_window)
#         fund_account_dialog.title("Fund Your Account")
#         fund_account_dialog.configure(bg='#003262')
#         img = ImageTk.PhotoImage(file='logo.png')
#         fund_account_dialog.iconphoto(False, img)
#         fund_account_dialog.grab_set()

#         # Set size of the fund account dialog
#         dialog_width = 400
#         dialog_height = 300

#         # Center the dialog relative to the parent window (self.new_window)
#         parent_x = self.new_window.winfo_x()
#         parent_y = self.new_window.winfo_y()
#         parent_width = self.new_window.winfo_width()
#         parent_height = self.new_window.winfo_height()

#         # Calculate the position
#         x = parent_x + (parent_width // 2) - (dialog_width // 2)
#         y = parent_y + (parent_height // 2) - (dialog_height // 2)

#         fund_account_dialog.geometry(f"{dialog_width}x{dialog_height}+{x}+{y}")

#         tk.Label(fund_account_dialog, text="Other Account Number:", bg='#6CB4EE').pack()
#         other_account_entry = tk.Entry(fund_account_dialog)
#         other_account_entry.pack()

#         tk.Label(fund_account_dialog, text="Other Username:", bg='#6CB4EE').pack()
#         other_username_entry = tk.Entry(fund_account_dialog)
#         other_username_entry.pack()

#         tk.Label(fund_account_dialog, text="Account BVN:", bg='#6CB4EE').pack()
#         other_bvn_entry = tk.Entry(fund_account_dialog)
#         other_bvn_entry.pack()

#         tk.Label(fund_account_dialog, text="Account Password:", bg='#6CB4EE').pack()
#         other_password_entry = tk.Entry(fund_account_dialog, show="*")
#         other_password_entry.pack()

#         tk.Label(fund_account_dialog, text="Amount to Withdraw:", bg='#6CB4EE').pack()
#         amount_entry = tk.Entry(fund_account_dialog)
#         amount_entry.pack()

#         def fund_callback():
#             other_account_number = other_account_entry.get()
#             other_username = other_username_entry.get()
#             other_bvn = other_bvn_entry.get()
#             other_password = other_password_entry.get()
#             try:
#                 amount = int(amount_entry.get())
#             except ValueError:
#                 messagebox.showerror("Error", "Invalid amount. Please enter a numeric value.")
#                 return

#             self.fund_account_from_other(self.username, other_account_number, other_username, other_bvn, other_password, amount)
#             fund_account_dialog.destroy()

#         tk.Button(fund_account_dialog, text="Fund", bg='#0095B6', command=fund_callback).pack()

#     def open_directory(self):
#         directory = filedialog.askdirectory(
#             initialdir="/", 
#             title="Select directory"
#         )
#         if directory:
#             self.image_path = directory
#             with open('image_path.txt', 'w') as f:
#                 f.write(self.image_path)
            
#             # Assume the image file is named "show.png" within the selected directory
#             self.load_image(f"{self.image_path}/show.png")

#     def load_image_from_path(self):
#         try:
#             with open('image_path.txt', 'r') as f:
#                 path = f.read().strip()
#                 self.load_image(path)
#         except FileNotFoundError:
#             print("image_path.txt not found")
#         except Exception as e:
#             print(f"An error occurred: {e}")

#     def load_image(self, image_file):
#         try:
#             # Open and resize the image
#             image = Image.open(image_file)
#             image = image.resize((80, 80), resample=Image.LANCZOS)
#             self.logos = ImageTk.PhotoImage(image)
            
#             # Update the image label
#             self.sign_in_image_label.place_forget()  # Hide the old image label if needed
#             self.sign_in_image_label.config(image=self.logos)  # Update the image label with the new image
#             self.sign_in_image_label.place(x=50, y=50)  # Adjust the position as needed
#         except FileNotFoundError:
#             print(f"File not found: {image_file}")
#         except Exception as e:
#             print(f"An error occurred while loading the image: {e}")

# if __name__ == "__main__":
#     root = tk.Tk()
#     app = App(root)
#     root.mainloop()
