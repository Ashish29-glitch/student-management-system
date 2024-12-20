import tkinter as tk
from tkinter import ttk

# Initialize the main window
win = tk.Tk()
win.geometry("1450x700+0+0")
win.title("Student Management System")

# Title label at the top
title_label = tk.Label(win, text="Students Management System", font=("Arial", 25, "bold"), border=15, relief=tk.GROOVE)
title_label.pack(side=tk.TOP, fill=tk.X)

# Frame for entering student details
detail_frame = tk.LabelFrame(win, text="Enter Details", font=("Arial", 20), bd=12, relief="groove", bg="lightgray")
detail_frame.place(x=20, y=110, width=420, height=560)

# Frame for displaying student data
data_frame = tk.Frame(win, bd=12, bg="lightgray", relief=tk.GROOVE)
data_frame.place(x=475, y=90, width=810, height=575)

# Variables to store input data
rollno = tk.StringVar()
name = tk.StringVar()
branch = tk.StringVar()
section = tk.StringVar()
contact = tk.StringVar()
email = tk.StringVar()
address = tk.StringVar()
fathersnm = tk.StringVar()
gender = tk.StringVar()
dob = tk.StringVar()

# Student details input fields
labels = [
    ("Roll No.", rollno),
    ("Name", name),
    ("Branch", branch),
    ("Section", section),
    ("Contact", contact),
    ("Father's Name", fathersnm),
    ("Address", address),
    ("Gender", gender),
    ("D.O.B", dob)
]

# Create input fields dynamically
for idx, (text, var) in enumerate(labels):
    row, col = divmod(idx, 2)
    label = tk.Label(detail_frame, text=text, font=("Arial", 17), bg="lightgray")
    label.grid(row=row, column=col * 2, padx=2, pady=2)
    entry = tk.Entry(detail_frame, bd=7, font=("Arial", 17), textvariable=var)
    entry.grid(row=row, column=col * 2 + 1, padx=2, pady=2)

# Buttons for Add, Update, Delete, Clear
btn_frame = tk.Frame(detail_frame, bg="lightgrey", bd=10, relief=tk.GROOVE)
btn_frame.place(x=20, y=420, width=400, height=100)

add_btn = tk.Button(btn_frame, text="Add", font=("Arial", 13), bg="green", width=15, bd=7)
add_btn.grid(row=0, column=0, padx=2, pady=2)

update_btn = tk.Button(btn_frame, text="Update", font=("Arial", 13), bg="blue", width=15, bd=7)
update_btn.grid(row=0, column=1, padx=3, pady=2)

delete_btn = tk.Button(btn_frame, text="Delete", font=("Arial", 13), bg="red", width=15, bd=7)
delete_btn.grid(row=1, column=0, padx=2, pady=2)

clear_btn = tk.Button(btn_frame, text="Clear", font=("Arial", 13), bg="blue", width=15, bd=7)
clear_btn.grid(row=1, column=1, padx=3, pady=2)

# Search section
search_frame = tk.Frame(data_frame, bg="lightgrey", bd=10, relief=tk.GROOVE)
search_frame.pack(side=tk.TOP, fill=tk.X)

search_lbl = tk.Label(search_frame, text="Search", font=("Arial", 13), bg="lightgrey")
search_lbl.pack(side=tk.LEFT, padx=12, pady=2)

search_in = ttk.Combobox(search_frame, font=("Arial", 14), state="readonly")
search_in['values'] = ("Name", "Roll No", "Contact", "Father's Name", "Branch", "Section", "D.O.B")
search_in.pack(side=tk.LEFT, padx=12, pady=2)

search_btn = tk.Button(search_frame, text="Search", font=("Arial", 13), bg="lightgrey", width=14, bd=9)
search_btn.pack(side=tk.LEFT, padx=12, pady=2)

showall_btn = tk.Button(search_frame, text="Show all", font=("Arial", 13), bg="lightgrey", width=14, bd=9)
showall_btn.pack(side=tk.LEFT, padx=12, pady=2)

# Table to display student data
main_frame = tk.Frame(data_frame, bg="lightgrey", bd=11, relief=tk.GROOVE)
main_frame.pack(fill=tk.BOTH, expand=True)

# Scrollbars for the table
y_scroll = tk.Scrollbar(main_frame, orient=tk.VERTICAL)
x_scroll = tk.Scrollbar(main_frame, orient=tk.HORIZONTAL)

# Treeview table to display student information
columns = ("Roll No", "Name", "Contact", "Father's Name", "Branch", "Section", "D.O.B")
student_table = ttk.Treeview(main_frame, columns=columns, yscrollcommand=y_scroll.set, xscrollcommand=x_scroll.set)

# Configure scrollbars
y_scroll.config(command=student_table.yview)
x_scroll.config(command=student_table.xview)

# Pack scrollbars
y_scroll.pack(side=tk.RIGHT, fill=tk.Y)
x_scroll.pack(side=tk.BOTTOM, fill=tk.X)

# Pack the treeview table
student_table.pack(fill=tk.BOTH, expand=True)

# Set headings for each column
for col in columns:
    student_table.heading(col, text=col)

# Set column widths
column_widths = {"Roll No": 100, "Name": 150, "Contact": 120, "Father's Name": 150, "Branch": 100, "Section": 100, "D.O.B": 120}
for col, width in column_widths.items():
    student_table.column(col, width=width)

# Hide the default first column (index column)
student_table['show'] = 'headings'

# Start the Tkinter event loop
win.mainloop()
