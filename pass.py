import tkinter as tk
from tkinter import messagebox, filedialog
import secrets
import string
import pyperclip
import json
import os

# --------------------
# PASSWORD GENERATOR LOGIC
# --------------------
def generate_password(length, use_lower, use_upper, use_digits, use_symbols, avoid_ambiguous, exclude_chars):
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation
    ambiguous_chars = "Il1O0"

    char_pool = ""
    if use_lower:
        char_pool += lower
    if use_upper:
        char_pool += upper
    if use_digits:
        char_pool += digits
    if use_symbols:
        char_pool += symbols

    if avoid_ambiguous:
        char_pool = "".join(ch for ch in char_pool if ch not in ambiguous_chars)

    if exclude_chars:
        char_pool = "".join(ch for ch in char_pool if ch not in exclude_chars)

    if not char_pool:
        return None  # No characters to choose from

    return "".join(secrets.choice(char_pool) for _ in range(length))

# --------------------
# PASSWORD STRENGTH CHECK
# --------------------
def password_strength(pw):
    length_score = min(len(pw) / 4, 2)
    variety_score = len(set([
        any(c.islower() for c in pw),
        any(c.isupper() for c in pw),
        any(c.isdigit() for c in pw),
        any(c in string.punctuation for c in pw)
    ]))
    score = length_score + variety_score

    if score < 2:
        return "Weak"
    elif score < 3:
        return "Medium"
    else:
        return "Strong"

# --------------------
# GUI APPLICATION
# --------------------
class PasswordGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Random Password Generator")
        self.root.geometry("500x600")
        self.history = []

        # Load presets if available
        self.preset_file = "password_presets.json"
        self.load_presets()

        # Length
        tk.Label(root, text="Password Length:").pack()
        self.length_var = tk.IntVar(value=self.presets.get("length", 12))
        tk.Entry(root, textvariable=self.length_var).pack()

        # Checkboxes
        self.lower_var = tk.BooleanVar(value=self.presets.get("lower", True))
        self.upper_var = tk.BooleanVar(value=self.presets.get("upper", True))
        self.digits_var = tk.BooleanVar(value=self.presets.get("digits", True))
        self.symbols_var = tk.BooleanVar(value=self.presets.get("symbols", True))
        self.avoid_var = tk.BooleanVar(value=self.presets.get("avoid", False))

        tk.Checkbutton(root, text="Include Lowercase", variable=self.lower_var).pack(anchor="w")
        tk.Checkbutton(root, text="Include Uppercase", variable=self.upper_var).pack(anchor="w")
        tk.Checkbutton(root, text="Include Numbers", variable=self.digits_var).pack(anchor="w")
        tk.Checkbutton(root, text="Include Symbols", variable=self.symbols_var).pack(anchor="w")
        tk.Checkbutton(root, text="Avoid Ambiguous Characters", variable=self.avoid_var).pack(anchor="w")

        # Exclude chars
        tk.Label(root, text="Exclude Characters:").pack()
        self.exclude_var = tk.StringVar(value=self.presets.get("exclude", ""))
        tk.Entry(root, textvariable=self.exclude_var).pack()

        # Number of passwords
        tk.Label(root, text="Number of Passwords:").pack()
        self.count_var = tk.IntVar(value=self.presets.get("count", 1))
        tk.Entry(root, textvariable=self.count_var).pack()

        # Generate button
        tk.Button(root, text="Generate Passwords", command=self.generate_passwords).pack(pady=5)

        # Output
        tk.Label(root, text="Generated Passwords:").pack()
        self.output_box = tk.Text(root, height=8)
        self.output_box.pack()

        # Strength label
        self.strength_label = tk.Label(root, text="Strength: N/A")
        self.strength_label.pack()

        # Buttons
        tk.Button(root, text="Copy First to Clipboard", command=self.copy_to_clipboard).pack(pady=2)
        tk.Button(root, text="Save All to File", command=self.save_to_file).pack(pady=2)
        tk.Button(root, text="Save Preferences", command=self.save_presets).pack(pady=2)

        # History
        tk.Label(root, text="History (last 10):").pack()
        self.history_box = tk.Text(root, height=8, state="disabled")
        self.history_box.pack()

    def generate_passwords(self):
        self.output_box.delete(1.0, tk.END)
        self.generated_list = []

        for _ in range(self.count_var.get()):
            pw = generate_password(
                self.length_var.get(),
                self.lower_var.get(),
                self.upper_var.get(),
                self.digits_var.get(),
                self.symbols_var.get(),
                self.avoid_var.get(),
                self.exclude_var.get()
            )
            if pw:
                self.generated_list.append(pw)
                self.output_box.insert(tk.END, pw + "\n")
            else:
                messagebox.showerror("Error", "No valid characters selected!")
                return

        # Update strength based on first password
        if self.generated_list:
            self.strength_label.config(text=f"Strength: {password_strength(self.generated_list[0])}")

        # Add to history
        self.history.extend(self.generated_list)
        self.history = self.history[-10:]  # Keep last 10
        self.update_history_box()

    def update_history_box(self):
        self.history_box.config(state="normal")
        self.history_box.delete(1.0, tk.END)
        for pw in self.history:
            self.history_box.insert(tk.END, pw + "\n")
        self.history_box.config(state="disabled")

    def copy_to_clipboard(self):
        if hasattr(self, "generated_list") and self.generated_list:
            pyperclip.copy(self.generated_list[0])
            messagebox.showinfo("Copied", "First password copied to clipboard!")

    def save_to_file(self):
        if hasattr(self, "generated_list") and self.generated_list:
            file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                                     filetypes=[("Text Files", "*.txt")])
            if file_path:
                with open(file_path, "w") as f:
                    for pw in self.generated_list:
                        f.write(pw + "\n")
                messagebox.showinfo("Saved", f"Passwords saved to {file_path}")

    def save_presets(self):
        presets = {
            "length": self.length_var.get(),
            "lower": self.lower_var.get(),
            "upper": self.upper_var.get(),
            "digits": self.digits_var.get(),
            "symbols": self.symbols_var.get(),
            "avoid": self.avoid_var.get(),
            "exclude": self.exclude_var.get(),
            "count": self.count_var.get()
        }
        with open(self.preset_file, "w") as f:
            json.dump(presets, f)
        messagebox.showinfo("Saved", "Preferences saved successfully!")

    def load_presets(self):
        if os.path.exists(self.preset_file):
            with open(self.preset_file, "r") as f:
                self.presets = json.load(f)
        else:
            self.presets = {}

# --------------------
# MAIN EXECUTION
# --------------------
if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()
