import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3
from datetime import datetime
import matplotlib.pyplot as plt


DATABASE = "bmi_records.db"


# ---------------- DATABASE ----------------

def create_database():
    try:
        connection = sqlite3.connect(DATABASE)
        cursor = connection.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS bmi_records (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                weight REAL NOT NULL,
                height REAL NOT NULL,
                bmi REAL NOT NULL,
                category TEXT NOT NULL,
                date TEXT NOT NULL
            )
        """)

        connection.commit()
        connection.close()

    except sqlite3.Error as error:
        messagebox.showerror(
            "Database Error",
            f"Could not create database:\n{error}"
        )


# ---------------- BMI CALCULATION ----------------

def calculate_bmi(weight, height):
    return weight / (height ** 2)


def get_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"


def get_category_color(category):
    if category == "Normal":
        return "green"
    elif category == "Underweight":
        return "orange"
    elif category == "Overweight":
        return "darkorange"
    else:
        return "red"


# ---------------- SAVE RECORD ----------------

def save_record(name, weight, height, bmi, category):
    try:
        connection = sqlite3.connect(DATABASE)
        cursor = connection.cursor()

        date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        cursor.execute("""
            INSERT INTO bmi_records
            (name, weight, height, bmi, category, date)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (name, weight, height, bmi, category, date))

        connection.commit()
        connection.close()

        return True

    except sqlite3.Error as error:
        messagebox.showerror(
            "Database Error",
            f"Could not save BMI record:\n{error}"
        )
        return False


# ---------------- CALCULATE BUTTON ----------------

def calculate():
    name = name_entry.get().strip()
    weight_text = weight_entry.get().strip()
    height_text = height_entry.get().strip()

    # Validate name
    if not name:
        messagebox.showerror(
            "Input Error",
            "Please enter a name."
        )
        return

    # Validate numbers
    try:
        weight = float(weight_text)
        height = float(height_text)

    except ValueError:
        messagebox.showerror(
            "Input Error",
            "Weight and height must be numeric values."
        )
        return

    # Validate positive values
    if weight <= 0:
        messagebox.showerror(
            "Input Error",
            "Weight must be greater than 0."
        )
        return

    if height <= 0:
        messagebox.showerror(
            "Input Error",
            "Height must be greater than 0."
        )
        return

    # Calculate BMI
    bmi = calculate_bmi(weight, height)
    category = get_category(bmi)

    # Display result
    result_label.config(
        text=f"BMI: {bmi:.2f}\nCategory: {category}",
        foreground=get_category_color(category)
    )

    # Save record
    if save_record(name, weight, height, bmi, category):
        messagebox.showinfo(
            "Success",
            "BMI calculated and record saved successfully."
        )


# ---------------- SHOW HISTORY ----------------

def show_history():
    name = name_entry.get().strip()

    if not name:
        messagebox.showerror(
            "Input Error",
            "Enter a user's name first."
        )
        return

    try:
        connection = sqlite3.connect(DATABASE)
        cursor = connection.cursor()

        cursor.execute("""
            SELECT date, weight, height, bmi, category
            FROM bmi_records
            WHERE name = ?
            ORDER BY date DESC
        """, (name,))

        records = cursor.fetchall()
        connection.close()

    except sqlite3.Error as error:
        messagebox.showerror(
            "Database Error",
            f"Could not read records:\n{error}"
        )
        return

    if not records:
        messagebox.showinfo(
            "History",
            f"No BMI records found for {name}."
        )
        return

    history_window = tk.Toplevel(root)
    history_window.title(f"BMI History - {name}")
    history_window.geometry("700x400")

    columns = ("date", "weight", "height", "bmi", "category")

    table = ttk.Treeview(
        history_window,
        columns=columns,
        show="headings"
    )

    table.heading("date", text="Date")
    table.heading("weight", text="Weight (kg)")
    table.heading("height", text="Height (m)")
    table.heading("bmi", text="BMI")
    table.heading("category", text="Category")

    table.column("date", width=170)
    table.column("weight", width=100)
    table.column("height", width=100)
    table.column("bmi", width=100)
    table.column("category", width=120)

    for record in records:
        table.insert(
            "",
            tk.END,
            values=(
                record[0],
                f"{record[1]:.2f}",
                f"{record[2]:.2f}",
                f"{record[3]:.2f}",
                record[4]
            )
        )

    table.pack(
        fill="both",
        expand=True,
        padx=10,
        pady=10
    )


# ---------------- SHOW BMI GRAPH ----------------

def show_graph():
    name = name_entry.get().strip()

    if not name:
        messagebox.showerror(
            "Input Error",
            "Enter a user's name first."
        )
        return

    try:
        connection = sqlite3.connect(DATABASE)
        cursor = connection.cursor()

        cursor.execute("""
            SELECT date, bmi
            FROM bmi_records
            WHERE name = ?
            ORDER BY date ASC
        """, (name,))

        records = cursor.fetchall()
        connection.close()

    except sqlite3.Error as error:
        messagebox.showerror(
            "Database Error",
            f"Could not read BMI data:\n{error}"
        )
        return

    if not records:
        messagebox.showinfo(
            "BMI Trend",
            f"No BMI records found for {name}."
        )
        return

    dates = [record[0] for record in records]
    bmi_values = [record[1] for record in records]

    plt.figure(figsize=(9, 5))

    plt.plot(
        dates,
        bmi_values,
        marker="o"
    )

    # Reference lines
    plt.axhline(
        y=18.5,
        linestyle="--",
        label="Underweight limit"
    )

    plt.axhline(
        y=25,
        linestyle="--",
        label="Normal limit"
    )

    plt.axhline(
        y=30,
        linestyle="--",
        label="Obese limit"
    )

    plt.title(f"BMI Trend - {name}")
    plt.xlabel("Date")
    plt.ylabel("BMI")

    plt.xticks(rotation=45)
    plt.legend()
    plt.grid(True)
    plt.tight_layout()

    plt.show()


# ---------------- CLEAR FIELDS ----------------

def clear_fields():
    name_entry.delete(0, tk.END)
    weight_entry.delete(0, tk.END)
    height_entry.delete(0, tk.END)

    result_label.config(
        text="BMI: --\nCategory: --",
        foreground="black"
    )


# ---------------- GUI ----------------

create_database()

root = tk.Tk()
root.title("BMI Calculator")
root.geometry("500x600")
root.resizable(False, False)


title_label = tk.Label(
    root,
    text="BMI Calculator",
    font=("Arial", 24, "bold")
)

title_label.pack(pady=20)


subtitle_label = tk.Label(
    root,
    text="Calculate and track your Body Mass Index",
    font=("Arial", 11)
)

subtitle_label.pack(pady=5)


# Input frame
input_frame = tk.Frame(root)
input_frame.pack(pady=20)


tk.Label(
    input_frame,
    text="Name:",
    font=("Arial", 12)
).grid(row=0, column=0, padx=10, pady=10, sticky="w")

name_entry = tk.Entry(
    input_frame,
    width=25,
    font=("Arial", 12)
)

name_entry.grid(row=0, column=1, padx=10, pady=10)


tk.Label(
    input_frame,
    text="Weight (kg):",
    font=("Arial", 12)
).grid(row=1, column=0, padx=10, pady=10, sticky="w")

weight_entry = tk.Entry(
    input_frame,
    width=25,
    font=("Arial", 12)
)

weight_entry.grid(row=1, column=1, padx=10, pady=10)


tk.Label(
    input_frame,
    text="Height (m):",
    font=("Arial", 12)
).grid(row=2, column=0, padx=10, pady=10, sticky="w")

height_entry = tk.Entry(
    input_frame,
    width=25,
    font=("Arial", 12)
)

height_entry.grid(row=2, column=1, padx=10, pady=10)


# Calculate button
calculate_button = tk.Button(
    root,
    text="Calculate BMI",
    command=calculate,
    font=("Arial", 12, "bold"),
    width=20
)

calculate_button.pack(pady=10)


# Result
result_label = tk.Label(
    root,
    text="BMI: --\nCategory: --",
    font=("Arial", 18, "bold")
)

result_label.pack(pady=20)


# Other buttons
button_frame = tk.Frame(root)
button_frame.pack(pady=10)


history_button = tk.Button(
    button_frame,
    text="View History",
    command=show_history,
    width=15
)

history_button.grid(row=0, column=0, padx=5)


graph_button = tk.Button(
    button_frame,
    text="Show BMI Trend",
    command=show_graph,
    width=15
)

graph_button.grid(row=0, column=1, padx=5)


clear_button = tk.Button(
    root,
    text="Clear",
    command=clear_fields,
    width=15
)

clear_button.pack(pady=10)


info_label = tk.Label(
    root,
    text=(
        "BMI Categories:\n"
        "Underweight: < 18.5\n"
        "Normal: 18.5 - 24.9\n"
        "Overweight: 25 - 29.9\n"
        "Obese: >= 30"
    ),
    font=("Arial", 10)
)

info_label.pack(pady=20)


root.mainloop()