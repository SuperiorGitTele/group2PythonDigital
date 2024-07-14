import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

class App:
    def __init__(self, master):
        self.master = master
        self.image_path = None
        self.logos = None
        
        # Button to open the directory dialog and select a directory
        self.open_dir_button = tk.Button(master, text="Select Directory", command=self.open_directory)
        self.open_dir_button.pack()

        # Button to load the image from the path stored in image_path.txt
        self.load_image_button = tk.Button(master, text="Load Image from Path", command=self.load_image_from_path)
        self.load_image_button.pack()

        # Placeholder for the image label
        self.sign_in_image_label = tk.Label(master)
        self.sign_in_image_label.pack()

    def open_directory(self):
        directory = filedialog.askdirectory(
            initialdir="/", 
            title="Select directory"
        )
        if directory:
            self.image_path = directory
            with open('image_path.txt', 'w') as f:
                f.write(self.image_path)
            
            # Assume the image file is named "show.png" within the selected directory
            self.load_image(f"{self.image_path}/show.png")

    def load_image_from_path(self):
        try:
            with open('image_path.txt', 'r') as f:
                path = f.read().strip()
                self.load_image(path)
        except FileNotFoundError:
            print("image_path.txt not found")
        except Exception as e:
            print(f"An error occurred: {e}")

    def load_image(self, image_file):
        try:
            # Open and resize the image
            image = Image.open(image_file)
            image = image.resize((80, 80), resample=Image.LANCZOS)
            self.logos = ImageTk.PhotoImage(image)
            
            # Update the image label
            self.sign_in_image_label.place_forget()  # Hide the old image label if needed
            self.sign_in_image_label.config(image=self.logos)  # Update the image label with the new image
            self.sign_in_image_label.place(x=50, y=50)  # Adjust the position as needed
        except FileNotFoundError:
            print(f"File not found: {image_file}")
        except Exception as e:
            print(f"An error occurred while loading the image: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
