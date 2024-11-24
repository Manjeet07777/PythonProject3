import tkinter as tk

# Function to handle button clicks
def button_click(value):
    current = entry.get()
    if value == "=":
        try:
            result = eval(current)  # Evaluate the expression
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif value == "C":
        entry.delete(0, tk.END)  # Clear the entry field
    else:
        entry.insert(tk.END, value)  # Add the button text to the entry field

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")

# Entry widget for the display with Helvetica font
entry = tk.Entry(root, width=20, font=("Helvetica", 40), justify="right")
entry.grid(row=0, column=0, columnspan=4, pady=10)

# Button layout with Courier font
buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "C", "0", "=", "+"
]

# Add buttons to the window
row = 1
col = 0
for button in buttons:
    b = tk.Button(root, text=button, width=5, height=2, font=("Courier", 20),
                  command=lambda value=button: button_click(value))
    b.grid(row=row, column=col, padx=5, pady=5)
    col += 1
    if col > 3:  # Move to the next row after 4 buttons
        col = 0
        row += 1

# Run the application
root.mainloop()
