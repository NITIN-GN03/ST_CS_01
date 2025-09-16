import tkinter as tk
from tkinter import messagebox

# Caesar Cipher Functions
def caesar_encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            result += char
    return result

def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)

# GUI Functions
def encrypt_message():
    message = entry_message.get("1.0", tk.END).strip()
    shift = entry_shift.get()
    
    if not shift.isdigit():
        messagebox.showerror("Error", "Shift value must be a number")
        return
    
    shift = int(shift)
    encrypted = caesar_encrypt(message, shift)
    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, encrypted)

def decrypt_message():
    message = entry_message.get("1.0", tk.END).strip()
    shift = entry_shift.get()
    
    if not shift.isdigit():
        messagebox.showerror("Error", "Shift value must be a number")
        return
    
    shift = int(shift)
    decrypted = caesar_decrypt(message, shift)
    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, decrypted)

# GUI Setup
root = tk.Tk()
root.title("Caesar Cipher - Encrypt & Decrypt")
root.geometry("500x400")
root.config(bg="#f0f0f0")

# Input Message
label_message = tk.Label(root, text="Enter Message:", font=("Arial", 12), bg="#f0f0f0")
label_message.pack(pady=5)

entry_message = tk.Text(root, height=4, width=50, font=("Arial", 12))
entry_message.pack(pady=5)

# Shift Value
label_shift = tk.Label(root, text="Enter Shift Value:", font=("Arial", 12), bg="#f0f0f0")
label_shift.pack(pady=5)

entry_shift = tk.Entry(root, font=("Arial", 12), width=10)
entry_shift.pack(pady=5)

# Buttons
frame_buttons = tk.Frame(root, bg="#f0f0f0")
frame_buttons.pack(pady=10)

btn_encrypt = tk.Button(frame_buttons, text="Encrypt", font=("Arial", 12), command=encrypt_message, bg="#4CAF50", fg="white", width=12)
btn_encrypt.grid(row=0, column=0, padx=10)

btn_decrypt = tk.Button(frame_buttons, text="Decrypt", font=("Arial", 12), command=decrypt_message, bg="#2196F3", fg="white", width=12)
btn_decrypt.grid(row=0, column=1, padx=10)

# Output Message
label_output = tk.Label(root, text="Output:", font=("Arial", 12), bg="#f0f0f0")
label_output.pack(pady=5)

output_text = tk.Text(root, height=4, width=50, font=("Arial", 12))
output_text.pack(pady=5)

# Run GUI
root.mainloop()
