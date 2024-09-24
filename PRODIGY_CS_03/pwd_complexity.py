# Password complexity checker

import re
from tkinter import *

def check_length():
    length_score = 0
    password_length = len(password)
    if password_length < 8:
        errors.append("> Password should be at least 8 characters long")
        status_label.config(text="Too weak", fg="#FF5370")
    elif password_length >= 8 and password_length < 12:
        length_score += 2
    elif password_length >= 12 and password_length < 16:
        length_score += 4
    else:
        length_score += 6
    return length_score

def check_uppercase():
    uppercase_score = 0
    if not re.search(r'[A-Z]', password):
        errors.append("> Password should have at least one uppercase letter")
        return uppercase_score
    uppercase_score += 2
    return uppercase_score

def check_lowercase():
    lowercase_score = 0
    if not re.search(r'[a-z]', password):
        errors.append("> Password should have at least one lowercase letter")
        return lowercase_score
    lowercase_score += 2
    return lowercase_score

def check_digits():
    digits_score = 0
    if not re.search(r'[0-9]', password):
        errors.append("> Password should have at least one digit")
        return digits_score
    digits_score += 2
    return digits_score

def check_special_char():
    special_char_score = 0
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        errors.append("> Password should have at least one special character")
        return special_char_score
    special_char_score += 2
    return special_char_score

def check_sequence():
    sequence_score = 0
    if re.search(r'(.)\1{2,}', password):
        errors.append("> Password should not have repeated characters")
        return sequence_score
    sequence_score += 2
    return sequence_score

def check_password():
    global password
    password = password_entry.get()
    result_label.config(text="")
    status_label.config(text="")
    errors.clear()
    
    # Check if the password is in the common passwords list
    with open('PRODIGY_CS_03/common_pwd.txt', 'r') as f:
        pwd_lists = f.read().splitlines()
        if password in pwd_lists:
            result_label.config(text="Password is too common\nScore : 0 / 10", fg="#FF5370")
            status_label.config(text="Very weak", fg="#FF5370")
            return
    
    # Calculate total score
    total_score = [check_length(), check_uppercase(), check_lowercase(), check_digits(), check_special_char(), check_sequence()]
    total = sum(total_score)

    # Display results and errors
    if total < 8:
        result_label.config(text=f"Weak Password\nScore: {total}", fg="#FF5370")
    elif total >= 8 and total < 12:
        result_label.config(text=f"Strong Password\nScore: {total}", fg="#FFCB6B")
        status_label.config(text="Good enough", fg="#82AAFF")
    elif total >= 12:
        result_label.config(text=f"Very Strong Password\nScore: {total}", fg="#C3E88D")
        status_label.config(text="Excellent", fg="#C3E88D")

    if errors:
        result_label.config(text="\n".join(errors), fg="#FF5370")

# Create the GUI
root = Tk()
root.title("PRODIGY_CS_03")
root.geometry("500x500")
root.config(bg="#1E1E1E")

errors = []

# Header
header_label = Label(root, text="Password Complexity Checker", font=("Helvetica", 20, "bold"), fg="#D4D4D4", bg="#1E1E1E")
header_label.pack(pady=20)

# Password label
password_label = Label(root, text="Enter the password", font=("Helvetica", 14), fg="#D4D4D4", bg="#1E1E1E")
password_label.pack(padx=20)

# Password entry
password_entry = Entry(root, font=("Helvetica", 14), bg="#2D2D2D", fg="#FFFFFF", insertbackground="#FFFFFF", relief="flat")
password_entry.pack(pady=20)

# Check button
check_button = Button(root, text="Check Score", font=("Helvetica", 14), bg="#007ACC", fg="#FFFFFF", activebackground="#007ACC", activeforeground="#FFFFFF", command=check_password)
check_button.pack(pady=20)

# Result label
result_label = Label(root, text="", font=("Helvetica", 14), fg="#D4D4D4", bg="#1E1E1E")
result_label.pack(pady=20)

# Status label
status_label = Label(root, text="", font=("Helvetica", 14), fg="#D4D4D4", bg="#1E1E1E")
status_label.pack(pady=20)

root.mainloop()
