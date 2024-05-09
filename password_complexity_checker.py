import re
import tkinter as tk
from tkinter import messagebox

def check_password_strength(password):
    length = len(password)
    uppercase = any(char.isupper() for char in password)
    lowercase = any(char.islower() for char in password)
    digit = any(char.isdigit() for char in password)
    special_char = bool(re.search(r'[!@#$%^&*()\-_=+{};:,<.>]', password))

    score = length * 4
    if uppercase:
        score += 5
    if lowercase:
        score += 5
    if digit:
        score += 5
    if special_char:
        score += 5

    if length < 8:
        return "Weak - The password should be at least 8 characters long."
    elif score < 50:
        return "Weak"
    elif score < 70:
        return "Moderate"
    elif score < 100:
        return "Strong"
    else:
        return "Very Strong"

def check_password():
    password = password_entry.get()
    requirements = ""
    if len(password) < 8:
        requirements += "• The password should be at least 8 characters long.\n"
    if not any(char.isupper() for char in password):
        requirements += "• At least one uppercase letter is required.\n"
    if not any(char.islower() for char in password):
        requirements += "• At least one lowercase letter is required.\n"
    if not any(char.isdigit() for char in password):
        requirements += "• At least one digit is required.\n"
    if not bool(re.search(r'[!@#$%^&*()\-_=+{};:,<.>]', password)):
        requirements += "• At least one special character is required.\n"
    if requirements:
        popup = tk.Toplevel(root)
        popup.title("Password Requirements")
        popup.geometry("400x300")
        popup.config(bg="#333")
        req_label = tk.Label(popup, text=requirements, font=("Helvetica", 14), fg="white", bg="#333", justify="center")
        req_label.pack(pady=10)
        ok_button = tk.Button(popup, text="OK", command=popup.destroy, font=("Helvetica", 12), bg="gray", fg="white")
        ok_button.pack(pady=10)
    else:
        strength = check_password_strength(password)
        messagebox.showinfo("Password Strength", f"Password Strength: {strength}", icon='info')

# Create GUI
root = tk.Tk()
root.title("Password Complexity Checker")
root.geometry("600x400")
root.config(bg="#333")

# Function to center window
def center_window(window):
    window.update_idletasks()
    width = window.winfo_width()
    height = window.winfo_height()
    x = (window.winfo_screenwidth() // 2) - (width // 2)
    y = (window.winfo_screenheight() // 2) - (height // 2)
    window.geometry('{}x{}+{}+{}'.format(width, height, x, y))

center_window(root)

# Label
label = tk.Label(root, text="Enter your password:", font=("Helvetica", 18), bg="#333", fg="white")
label.pack(pady=10)

# Entry
password_entry = tk.Entry(root, show="*", font=("Helvetica", 16))
password_entry.pack(pady=10)

# Button
check_button = tk.Button(root, text="Check Strength", command=check_password, font=("Helvetica", 16), bg="gray", fg="white")
check_button.pack(pady=10)

root.mainloop()