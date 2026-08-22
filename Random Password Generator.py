import tkinter as tk
from tkinter import ttk, messagebox
import secrets
import string
import pyperclip


class PasswordGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title("🔐 Random Password Generator")
        self.root.geometry("600x650")
        self.root.resizable(False, False)

        self.history = []

        # Variables
        self.uppercase_var = tk.BooleanVar(value=True)
        self.lowercase_var = tk.BooleanVar(value=True)
        self.numbers_var = tk.BooleanVar(value=True)
        self.symbols_var = tk.BooleanVar(value=True)

        self.ambiguous_var = tk.BooleanVar(value=False)

        self.length_var = tk.IntVar(value=12)
        self.password_var = tk.StringVar()

        self.create_widgets()

    def create_widgets(self):

        # ==========================
        # TITLE
        # ==========================

        tk.Label(
            self.root,
            text="🔐 Random Password Generator",
            font=("Arial", 20, "bold")
        ).pack(pady=(15, 3))

        tk.Label(
            self.root,
            text="Create strong and secure passwords",
            font=("Arial", 10)
        ).pack(pady=(0, 10))

        # ==========================
        # LENGTH
        # ==========================

        length_frame = tk.LabelFrame(
            self.root,
            text="Password Length",
            font=("Arial", 10, "bold"),
            padx=10,
            pady=5
        )
        length_frame.pack(fill="x", padx=25, pady=5)

        self.length_label = tk.Label(
            length_frame,
            text="12",
            font=("Arial", 12, "bold")
        )
        self.length_label.pack()

        tk.Scale(
            length_frame,
            from_=8,
            to=64,
            orient="horizontal",
            variable=self.length_var,
            command=self.update_length,
            length=450
        ).pack()

        # ==========================
        # CHARACTER TYPES
        # ==========================

        type_frame = tk.LabelFrame(
            self.root,
            text="Character Types",
            font=("Arial", 10, "bold"),
            padx=10,
            pady=5
        )
        type_frame.pack(fill="x", padx=25, pady=5)

        # Put checkboxes in one row
        tk.Checkbutton(
            type_frame,
            text="A-Z",
            variable=self.uppercase_var
        ).grid(row=0, column=0, padx=15)

        tk.Checkbutton(
            type_frame,
            text="a-z",
            variable=self.lowercase_var
        ).grid(row=0, column=1, padx=15)

        tk.Checkbutton(
            type_frame,
            text="0-9",
            variable=self.numbers_var
        ).grid(row=0, column=2, padx=15)

        tk.Checkbutton(
            type_frame,
            text="Symbols",
            variable=self.symbols_var
        ).grid(row=0, column=3, padx=15)

        # ==========================
        # SECURITY OPTION
        # ==========================

        tk.Checkbutton(
            self.root,
            text="Exclude ambiguous characters (0, O, l, 1)",
            variable=self.ambiguous_var,
            font=("Arial", 9)
        ).pack(pady=5)

        # ==========================
        # PASSWORD
        # ==========================

        password_frame = tk.LabelFrame(
            self.root,
            text="Generated Password",
            font=("Arial", 10, "bold"),
            padx=10,
            pady=8
        )
        password_frame.pack(fill="x", padx=25, pady=5)

        tk.Entry(
            password_frame,
            textvariable=self.password_var,
            font=("Consolas", 15),
            justify="center",
            state="readonly"
        ).pack(fill="x")

        # ==========================
        # STRENGTH
        # ==========================

        strength_frame = tk.Frame(self.root)
        strength_frame.pack(pady=5)

        tk.Label(
            strength_frame,
            text="Strength:",
            font=("Arial", 10, "bold")
        ).pack(side="left")

        self.strength_label = tk.Label(
            strength_frame,
            text="Not Generated",
            font=("Arial", 10, "bold")
        )
        self.strength_label.pack(side="left", padx=8)

        self.strength_bar = ttk.Progressbar(
            self.root,
            length=450,
            mode="determinate",
            maximum=100
        )
        self.strength_bar.pack(pady=3)

        # ==========================
        # GENERATE BUTTON
        # ==========================

        button_frame = tk.Frame(self.root)
        button_frame.pack(pady=10)

        tk.Button(
            button_frame,
            text="🔑 GENERATE PASSWORD",
            command=self.generate_password,
            font=("Arial", 11, "bold"),
            padx=20,
            pady=8
        ).grid(row=0, column=0, padx=5)

        tk.Button(
            button_frame,
            text="📋 COPY",
            command=self.copy_password,
            font=("Arial", 11, "bold"),
            padx=20,
            pady=8
        ).grid(row=0, column=1, padx=5)

        # ==========================
        # HISTORY
        # ==========================

        history_frame = tk.LabelFrame(
            self.root,
            text="Last 5 Generated Passwords",
            font=("Arial", 10, "bold"),
            padx=5,
            pady=5
        )
        history_frame.pack(fill="x", padx=25, pady=5)

        self.history_listbox = tk.Listbox(
            history_frame,
            height=5,
            font=("Consolas", 10)
        )
        self.history_listbox.pack(fill="x")

    # ==========================
    # UPDATE LENGTH
    # ==========================

    def update_length(self, value):
        self.length_label.config(
            text=str(int(float(value)))
        )

    # ==========================
    # CHARACTER SETS
    # ==========================

    def get_character_sets(self):

        sets = []

        ambiguous = "0Ol1"

        if self.uppercase_var.get():

            chars = string.ascii_uppercase

            if self.ambiguous_var.get():
                chars = "".join(
                    c for c in chars
                    if c not in ambiguous
                )

            sets.append(chars)

        if self.lowercase_var.get():

            chars = string.ascii_lowercase

            if self.ambiguous_var.get():
                chars = "".join(
                    c for c in chars
                    if c not in ambiguous
                )

            sets.append(chars)

        if self.numbers_var.get():

            chars = string.digits

            if self.ambiguous_var.get():
                chars = "".join(
                    c for c in chars
                    if c not in ambiguous
                )

            sets.append(chars)

        if self.symbols_var.get():

            sets.append(string.punctuation)

        return sets

    # ==========================
    # GENERATE PASSWORD
    # ==========================

    def generate_password(self):

        length = self.length_var.get()

        # Minimum length
        if length < 8:
            messagebox.showerror(
                "Invalid Length",
                "Password length must be at least 8."
            )
            return

        character_sets = self.get_character_sets()

        # At least 2 types
        if len(character_sets) < 2:
            messagebox.showerror(
                "Invalid Selection",
                "Select at least 2 character types."
            )
            return

        password = []

        # Guarantee one character from each type
        for chars in character_sets:
            password.append(
                secrets.choice(chars)
            )

        # Combine character sets
        all_characters = "".join(character_sets)

        # Fill remaining characters
        while len(password) < length:
            password.append(
                secrets.choice(all_characters)
            )

        # Secure shuffle
        for i in range(len(password) - 1, 0, -1):
            j = secrets.randbelow(i + 1)
            password[i], password[j] = (
                password[j],
                password[i]
            )

        password = "".join(password)

        # Display
        self.password_var.set(password)

        # Strength
        self.update_strength(
            password,
            len(character_sets)
        )

        # History
        self.add_to_history(password)

        # Automatically copy
        self.copy_password(silent=True)

    # ==========================
    # STRENGTH
    # ==========================

    def update_strength(self, password, types):

        length = len(password)

        score = 0

        if length >= 8:
            score += 20

        if length >= 12:
            score += 20

        if length >= 16:
            score += 20

        score += types * 10

        score = min(score, 100)

        if score < 50:
            strength = "Weak"
        elif score < 80:
            strength = "Medium"
        else:
            strength = "Strong"

        self.strength_label.config(text=strength)
        self.strength_bar["value"] = score

    # ==========================
    # COPY
    # ==========================

    def copy_password(self, silent=False):

        password = self.password_var.get()

        if not password:

            if not silent:
                messagebox.showwarning(
                    "No Password",
                    "Generate a password first."
                )

            return

        try:

            pyperclip.copy(password)

            if not silent:
                messagebox.showinfo(
                    "Copied",
                    "Password copied to clipboard!"
                )

        except Exception as error:

            if not silent:
                messagebox.showerror(
                    "Clipboard Error",
                    str(error)
                )

    # ==========================
    # HISTORY
    # ==========================

    def add_to_history(self, password):

        self.history.insert(0, password)

        # Keep only last 5
        if len(self.history) > 5:
            self.history.pop()

        self.history_listbox.delete(
            0,
            tk.END
        )

        for item in self.history:
            self.history_listbox.insert(
                tk.END,
                item
            )


# ==============================
# START PROGRAM
# ==============================

if __name__ == "__main__":

    root = tk.Tk()

    app = PasswordGenerator(root)

    root.mainloop()