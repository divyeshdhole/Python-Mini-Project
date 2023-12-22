import tkinter as tk
from tkinter import messagebox
import pandas as pd
import datetime as dt

class BirthdayEntryGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Birthday Entry GUI")

        # Title text in bold
        title_text = "Name : Divyesh Dhole\nPRN : 211101027\nRoll No : 25"
        self.label_title = tk.Label(root, text=title_text, font=("Helvetica", 12, "bold"))
        self.label_title.pack(pady=10)

        self.label_name = tk.Label(root, text="Enter Name:")
        self.label_name.pack(pady=5)
        self.entry_name = tk.Entry(root)
        self.entry_name.pack(pady=5)

        self.label_date = tk.Label(root, text="Enter Birthdate (DD/MM):")
        self.label_date.pack(pady=5)
        self.entry_date = tk.Entry(root)
        self.entry_date.pack(pady=5)

        self.label_email = tk.Label(root, text="Enter Email:")
        self.label_email.pack(pady=5)
        self.entry_email = tk.Entry(root)
        self.entry_email.pack(pady=5)

        self.button_submit = tk.Button(root, text="Submit", command=self.submit_birthday)
        self.button_submit.pack(pady=10)

    def submit_birthday(self):
        try:
            name = self.entry_name.get()
            birthdate_str = self.entry_date.get()
            email = self.entry_email.get()

            if not name or not birthdate_str or not email:
                messagebox.showwarning("Incomplete Information", "Please enter name, birthdate, and email.")
                return

            birthdate = tuple(map(int, birthdate_str.split('/')))

            friends_data = pd.DataFrame({
                'name': [name],
                'email': [email],
                'month': [birthdate[1]],
                'day': [birthdate[0]],
            })

            with open("C:/Users/PCP/Desktop/Day 32 - Bday Wisher/Day 32 - Bday Wisher/Bday Wisher/birthdays.csv", 'a', newline='') as file:
                friends_data.to_csv(file, header=False, index=False)

            messagebox.showinfo("Success", "Birthday entry added successfully!")

            self.entry_name.delete(0, tk.END)
            self.entry_date.delete(0, tk.END)
            self.entry_email.delete(0, tk.END)

        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = BirthdayEntryGUI(root)
    root.mainloop()