import customtkinter as ctk
import math

def addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b

def power(a, b):
    if b == 0:
        return 1
    return a ** b

def root(a, b):
    if a < 0 and b % 2 == 0:
        return "Error: Complex result"
    return a ** (1 / b)

def factorial(a):
    if a == 0:
        return 1
    return a * factorial(a - 1)

def sin(a):
    return math.sin(a)

def cos(a):
    return math.cos(a)

class MyButtonFrame(ctk.CTkFrame):  # Create buttons
    def __init__(self, master, console_callback):
        super().__init__(master)
        self.entry = ctk.CTkEntry(self, width=260)
        self.entry.grid(row=0, column=0, columnspan=5, padx=1, pady=1)

        buttons = [
            ("C", 1, 0),  # Clear button
            ("Del", 1, 1),  # Delete button
            ("^", 1, 2),  # Power button
            ("√n", 1, 3),  # Nth root button
            ("!", 1, 4),  # Factorial button
            ("7", 2, 0),
            ("8", 2, 1),
            ("9", 2, 2),
            ("/", 2, 3),
            ("(", 2, 4),
            ("4", 3, 0),
            ("5", 3, 1),
            ("6", 3, 2),
            ("*", 3, 3),
            (")", 3, 4),
            ("1", 4, 0),
            ("2", 4, 1),
            ("3", 4, 2),
            ("-", 4, 3),
            ("sin()", 4, 4),
            (".", 5, 0),
            ("0", 5, 1),
            ("=", 5, 2),
            ("+", 5, 3),
            ("cos()", 5, 4),
        ]

        def button_input(text):
            if text == "=":  # Display the result
                input_text = self.entry.get()
                try:
                    result = eval(input_text)
                    self.entry.delete(0, ctk.END)
                    self.entry.insert(0, str(result))
                    console_callback(result)
                except Exception as e:
                    self.entry.delete(0, ctk.END)
                    self.entry.insert(0, "Error")
            elif text == "C":  # Clear the input field
                self.entry.delete(0, ctk.END)
            elif text == "Del":
                current_text = self.entry.get()
                self.entry.delete(0, ctk.END)
                self.entry.insert(0, current_text[:-1])
            elif text == "^":
                current_text = self.entry.get()
                self.entry.delete(0, ctk.END)
                self.entry.insert(0, current_text + "**")
            elif text == "!":
                current_text = self.entry.get()
                self.entry.delete(0, ctk.END)
                self.entry.insert(0, f"factorial({current_text})")
            elif text == "√n":
                current_text = self.entry.get()
                self.entry.delete(0, ctk.END)
                self.entry.insert(0, f"root({current_text}, n)")
            elif text == "sin()":
                current_text = self.entry.get()
                self.entry.delete(0, ctk.END)
                self.entry.insert(0, f"sin({current_text})")
            elif text == "cos()":
                current_text = self.entry.get()
                self.entry.delete(0, ctk.END)
                self.entry.insert(0, f"cos({current_text})")
            else:
                current_text = self.entry.get()
                self.entry.delete(0, ctk.END)
                self.entry.insert(0, current_text + text)

        for button_text, row, column in buttons:
            ctk.CTkButton(self, text=button_text, width=50, height=50, command=lambda text=button_text: button_input(text)).grid(row=row, column=column, padx=1, pady=1, sticky="w")

class App(ctk.CTk): # Main loop
    def __init__(self):
        super().__init__()
        self.title('Calculator')
        self.geometry('265x330')
        self.grid_rowconfigure((0, 5), weight=1)
        self.grid_columnconfigure((0, 4), weight=1)
        
        self.result = 0  # Variable to store the result
        self.console_output = ctk.CTkTextbox(self, height=8, width=260)
        self.console_output.grid(row=6, column=0, columnspan=5, padx=5, pady=5, sticky="w")
        
        self.button_frame = MyButtonFrame(self, console_callback=self.update_console)
        self.button_frame.grid(row=0, column=0, padx=1, pady=(1, 0), sticky="w")

    def update_console(self, result):
        # Append the calculation and result to the console output
        console_text = self.console_output.get("1.0", ctk.END)
        self.console_output.delete("1.0", ctk.END)
        console_text += f"{self.button_frame.entry.get()} = {result}\n"
        self.console_output.insert(ctk.END, console_text)
        
app = App()
app.mainloop()
