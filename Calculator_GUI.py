# Calculator GUI for userinterface
import tkinter as tk
from Calculator_logic import (
    add,
    subtract,
    multiply,
    divide,
)  # Corrected spelling of 'subtract'


def caulculate():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        operation = operation_var.get()


        if operation == "+":
            result = add(num1, num2)
        elif operation == "-":
            result = subtract(num1, num2)
        elif operation == "*":
            result = multiply(num1, num2)
        elif operation == "/":
            result = divide(num1, num2)

        
        result_label.config(text=f"Result: {result}")
    except ValueError:
             result_label.config(text=f"Error: Invalid input!")






        # setting up tkinter GUI
root = tk.Tk()
root.title("Calculator GUI")

window_height = 400
window_width = 400
root.geometry(f"{window_height}x{window_width}")

screen_width= root.winfo_screenwidth()
screen_height= root.winfo_height()

x_position = (screen_width // 2) - (window_width // 2)
y_position = (screen_height // 2) - (window_height // 2)

root.geometry(f"{window_height}x{window_width}+{x_position}+{y_position}")

# input fields and layout
entry1 = tk.Entry(root)
entry1.grid(row=0, column=1)
entry2 = tk.Entry(root)
entry2.grid(row=1, column=1)

operation_var = tk.StringVar(root)
operation_var.set("+")

operation_menu = tk.OptionMenu(root, operation_var, "+", "-", "*", "/")
operation_menu.grid(row=2, column=1)

caulculate_button = tk.Button(root, text="Calculate", command=caulculate)
caulculate_button.grid(row=3, column=1)

result_label = tk.Label(root, text="Result:")
result_label.grid(row=4, column=1)

root.mainloop()
