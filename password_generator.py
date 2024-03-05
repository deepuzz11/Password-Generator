import random
import string
import tkinter as tk
from tkinter import messagebox

def generate_password(length):
    # Define the characters to be used in the password
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Generate the password
    password = ''.join(random.choice(characters) for i in range(length))
    
    return password

def generate_password_gui():
    try:
        length = int(length_entry.get())
        if length <= 0:
            messagebox.showerror("Error", "Please enter a valid length for the password.")
            return
        
        password = generate_password(length)
        
        password_label.config(text="Generated Password: " + password)
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid integer for the length of the password.")

# Create a tkinter window
window = tk.Tk()
window.title("Password Generator")

# Create a label for instructions
instruction_label = tk.Label(window, text="Enter the desired length of the password:")
instruction_label.pack()

# Create an entry for the length of the password
length_entry = tk.Entry(window)
length_entry.pack()

# Create a button to generate the password
generate_button = tk.Button(window, text="Generate Password", command=generate_password_gui)
generate_button.pack()

# Create a label to display the generated password
password_label = tk.Label(window, text="")
password_label.pack()

# Run the tkinter event loop
window.mainloop()
