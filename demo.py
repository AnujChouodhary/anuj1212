import tkinter as tk

root=tk.Tk()
root.title("My first app")
root.geometry("500x200")
tk.Label(root, text="First Number").grid(
    row=0, column=0, padx=10, pady=10
)
num1 = tk.Entry(root)
num1.grid(row=0, column=1)

tk.Label(root, text="Second Number").grid(
    row=1, column=0, padx=10, pady=10
)
num2 = tk.Entry(root)
num2.grid(row=1, column=1)


result = tk.Label(root, text="Result: ")
result.grid(row=2, column=0, columnspan=2, padx=30,pady=30)

def calculate(op):
    
    a = float(num1.get())
    b = float(num2.get())

    if op == "+":
            ans = a + b
    elif op == "-":
            ans = a - b
    elif op == "*":
            ans = a * b
    elif op == "/":
        if b == 0:
            result.config(text="Cannot divide by zero")
            return
        ans = a / b



    result.config(text="Result: " + str(ans))


tk.Button(
    root, text="Add",
    command=lambda: calculate("+")
).grid(row=3, column=0, padx=5, pady=5)





root.mainloop()