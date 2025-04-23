from cryptography.fernet import Fernet
import tkinter as tk
from tkinter import ttk, filedialog, PhotoImage
from functools import partial

# Constants
button_height = 2
button_width = 30

# Functionality
def browse_files():
    browse_files.filename = filedialog.askopenfilename(title="Select a File")
    file_label.config(text=f"File Selected: {browse_files.filename}")
    password_label.pack(pady=(20, 5))
    password_entry.pack()
    encrypt_button.pack(pady=(15, 5))
    decrypt_button.pack()
    status_label.pack(pady=(20, 0))

def encrypt_file(pword):
    temp_key = pword.get()
    temp_key = ''.join(e for e in temp_key if e.isalnum())
    key = temp_key + ("s" * (43 - len(temp_key)) + "=")

    fernet = Fernet(key)

    with open(browse_files.filename, 'rb') as file:
        original = file.read()

    encrypted = fernet.encrypt(original)

    with open(browse_files.filename, 'wb') as file:
        file.write(encrypted)

    status_label.config(text="✅ File Encrypted Successfully")

def decrypt_file(pword):
    temp_key = pword.get()
    temp_key = ''.join(e for e in temp_key if e.isalnum())
    key = temp_key + ("s" * (43 - len(temp_key)) + "=")

    fernet = Fernet(key)

    with open(browse_files.filename, 'rb') as file:
        encrypted = file.read()

    decrypted = fernet.decrypt(encrypted)

    with open(browse_files.filename, 'wb') as file:
        file.write(decrypted)

    status_label.config(text="🔓 File Decrypted Successfully")

# UI Setup
window = tk.Tk()
window.title("Kcryption - Secure File Encryptor")
icon = PhotoImage(file="Kcryption/K.png")  # Adjust the path as needed
window.iconphoto(True, icon)
window.geometry("800x600")
window.configure(bg="#0f0f0f")

# Style
style = ttk.Style()
style.theme_use("clam")
style.configure("TButton", foreground="white", background="#333", font=("Segoe UI", 12), padding=10)
style.configure("TLabel", background="#0f0f0f", foreground="white", font=("Segoe UI", 14))

# Layout Widgets
title = ttk.Label(window, text="🔐 Kcryption", font=("Segoe UI", 24))
title.pack(pady=(30, 10))

file_label = ttk.Label(window, text="No file selected.")
file_label.pack(pady=(10, 10))

browse_button = ttk.Button(window, text="📂 Browse File", command=browse_files)
browse_button.pack(pady=10)

password_label = ttk.Label(window, text="Enter Password:")
password_var = tk.StringVar()
password_entry = ttk.Entry(window, textvariable=password_var, show="*", width=40)

# Bind encrypt/decrypt
submit_en = partial(encrypt_file, password_var)
submit_de = partial(decrypt_file, password_var)

encrypt_button = ttk.Button(window, text="Encrypt File", command=submit_en)
decrypt_button = ttk.Button(window, text="Decrypt File", command=submit_de)

status_label = ttk.Label(window, text="", font=("Segoe UI", 13))

credit_label = ttk.Label(window, text="© 2025 Built by Kwasi GA", font=("Segoe UI", 10))
credit_label.pack(side="bottom", pady=10)

window.mainloop()
