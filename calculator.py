import tkinter as tk

def on_button_click(value):
    if value == "=":
        try:
            result = str(eval(entry_var.get()))
            entry_var.set(result)
        except:
            entry_var.set("Error")
    elif value == "C":
        entry_var.set("")
    else:
        entry_var.set(entry_var.get() + value)

root = tk.Tk()
root.title("Simple Calculator")

entry_var = tk.StringVar()
entry = tk.Entry(root, textvariable=entry_var, font=("Arial", 18), bd=10, relief=tk.GROOVE, justify='right')
entry.grid(row=0, column=0, columnspan=4)

buttons = [
    ('7', '8', '9', '/'),
    ('4', '5', '6', '*'),
    ('1', '2', '3', '-'),
    ('C', '0', '=', '+')
]

for i, row in enumerate(buttons):
    for j, value in enumerate(row):
        tk.Button(root, text=value, font=("Arial", 18), width=5, height=2,
                  command=lambda v=value: on_button_click(v)).grid(row=i+1, column=j)

root.mainloop()
