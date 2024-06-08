import tkinter as tk

class DropdownExample:
    def __init__(self, master):
        self.master = master
        self.master.title("Dropdown Example")

        self.options = ["Transfer","Transfer to a PTP Account", "Transfer to Other Accounts"]
        self.variable = tk.StringVar(self.master)
        self.variable.set(self.options[0])  # default value

        self.dropdown = tk.OptionMenu(self.master, self.variable, *self.options)
        self.dropdown.pack()

        self.button = tk.Button(self.master, text="Start Transaction", command=self.get_selected_option)
        self.button.pack()

    def get_selected_option(self):
        if self.variable.get() == "Transfer to a PTP Account":
            self.transfers_to_a_ptp_account()
        
        elif self.variable.get() == "Transfer to Other Accounts":
            self.transfer_to_other()
        else:
            print("Nah")

    def transfers_to_a_ptp_account(self):
        print("Hello")

    def transfer_to_other(self):
        print("What")

root = tk.Tk()
app = DropdownExample(root)
root.mainloop()