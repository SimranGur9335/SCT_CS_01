import tkinter as tk
from tkinter import messagebox

# Caesar Cipher Logic
def caesar_cipher(text, shift, mode):
    result = ""
    for char in text:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            if mode == "encrypt":
                result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
            elif mode == "decrypt":
                result += chr((ord(char) - shift_base - shift) % 26 + shift_base)
        else:
            result += char
    return result

# Button Function
def process_text():
    text = entry_text.get()
    shift = shift_value.get()
    mode = mode_var.get()

    if not text:
        messagebox.showerror("Error", "Please enter a message.")
        return

    try:
        shift = int(shift)
    except ValueError:
        messagebox.showerror("Error", "Shift must be an integer.")
        return

    result = caesar_cipher(text, shift, mode)
    output_label.config(text=f"Result: {result}")

# GUI Setup
root = tk.Tk()
root.title("Caesar Cipher Tool")

# Dark Mode Colors
bg_color = "#1e1e1e"
fg_color = "#ffffff"
accent_color = "#00bcd4"

root.configure(bg=bg_color)

# Styling function for consistent widget look
def style_widget(widget, font_size=11):
    widget.configure(bg=bg_color, fg=fg_color, font=("Segoe UI", font_size), highlightthickness=0, borderwidth=0)

# Labels and Entries
label1 = tk.Label(root, text="Enter your message:")
style_widget(label1)
label1.pack(pady=5)

entry_text = tk.Entry(root, width=40, bg="#333", fg=fg_color, insertbackground=fg_color)
entry_text.pack(pady=5)

label2 = tk.Label(root, text="Enter shift value:")
style_widget(label2)
label2.pack(pady=5)

shift_value = tk.Entry(root, width=10, bg="#333", fg=fg_color, insertbackground=fg_color)
shift_value.pack(pady=5)

# Mode Selection
mode_var = tk.StringVar(value="encrypt")

encrypt_radio = tk.Radiobutton(root, text="Encrypt", variable=mode_var, value="encrypt", bg=bg_color, fg=fg_color, selectcolor=bg_color, activebackground=bg_color)
decrypt_radio = tk.Radiobutton(root, text="Decrypt", variable=mode_var, value="decrypt", bg=bg_color, fg=fg_color, selectcolor=bg_color, activebackground=bg_color)

encrypt_radio.pack()
decrypt_radio.pack()

# Process Button
process_btn = tk.Button(root, text="Process", command=process_text, bg=accent_color, fg=bg_color, activebackground="#0097a7", padx=10, pady=5)
process_btn.pack(pady=10)

# Output Label
output_label = tk.Label(root, text="Result: ")
style_widget(output_label)
output_label.pack(pady=10)

# Start App
root.mainloop()
