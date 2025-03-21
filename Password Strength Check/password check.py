import re
import tkinter as tk
from tkinter import messagebox
import winsound  


COMMON_PASSWORDS = [
    "password", "123456", "12345678", "1234", "qwerty", "12345", 
    "dragon", "baseball", "football", "letmein", "monkey", "abc123"
]

def check_password_strength(password):
    """
    Check the strength of a password based on the following criteria:
    - Minimum length of 8 characters.
    - Contains at least one uppercase letter.
    - Contains at least one lowercase letter.
    - Contains at least one digit.
    - Contains at least one special character.
    - Not a common password.
    """
    
    if password.lower() in COMMON_PASSWORDS:
        return "Very weak: Password is too common."

    
    length_criteria = len(password) >= 8
    uppercase_criteria = re.search(r'[A-Z]', password) is not None
    lowercase_criteria = re.search(r'[a-z]', password) is not None
    digit_criteria = re.search(r'[0-9]', password) is not None
    special_char_criteria = re.search(r'[!@#$%^&*(),.?":{}|<>]', password) is not None

    criteria_met = sum([length_criteria, uppercase_criteria, lowercase_criteria, digit_criteria, special_char_criteria])

   
    if criteria_met == 5:
        return "Strong password! Great job."
    elif criteria_met >= 3:
        return "Moderate password. Consider adding more complexity."
    else:
        return "Weak password. Please improve it."

def on_check_password():
    """
    Function to handle the "Check Password" button click.
    """
    password = password_entry.get()  
    if not password:
        messagebox.showwarning("Input Error", "Please enter a password.")
        return

    result = check_password_strength(password)  
    result_label.config(text=result)  

   
    if result.startswith("Weak") or result.startswith("Very weak"):
        winsound.Beep(1000, 500)  

    
    if result == "Strong password! Great job.":
        messagebox.showinfo("Success", "Your password is strong!")

def toggle_password_visibility():
    """
    Function to toggle password visibility.
    """
    if password_entry.cget("show") == "*":
        password_entry.config(show="")  
        show_hide_button.config(text="Hide Password")
    else:
        password_entry.config(show="*")  
        show_hide_button.config(text="Show Password")


root = tk.Tk()
root.title("Password Strength Checker")


instruction_label = tk.Label(root, text="Enter a password to check its strength:")
instruction_label.pack(pady=10)

password_entry = tk.Entry(root, show="*", width=40)  
password_entry.pack(pady=10)

show_hide_button = tk.Button(root, text="Show Password", command=toggle_password_visibility)
show_hide_button.pack(pady=5)

check_button = tk.Button(root, text="Check Password", command=on_check_password)
check_button.pack(pady=10)

result_label = tk.Label(root, text="", fg="blue")
result_label.pack(pady=10)


root.mainloop()