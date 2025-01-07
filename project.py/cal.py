import tkinter as tk

# Function to handle button clicks
def button_click(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + value)

# Function to clear the entry
def clear():
    entry.delete(0, tk.END)

# Function to evaluate the expression
def evaluate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Create the main application window
root = tk.Tk()
root.title("Calculator")

# Entry widget to display numbers and results
entry = tk.Entry(root, width=20, borderwidth=5, font=("Arial", 18), justify='right')
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Button layout
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('C', 4, 0), ('0', 4, 1), ('=', 4, 2), ('+', 4, 3),
]
# Create buttons and add to the window
for (text, row, col) in buttons:
    if text == "=":
        button = tk.Button(root, text=text, width=5, height=2, font=("Arial", 14), command=evaluate)
    elif text == "C":
        button = tk.Button(root, text=text, width=5, height=2, font=("Arial", 14), command=clear)
    else:
        button = tk.Button(root, text=text, width=5, height=2, font=("Arial", 14), 
                           command=lambda t=text: button_click(t))
    button.grid(row=row, column=col, padx=5, pady=5)

# Start the tkinter event loop
root.mainloop()
