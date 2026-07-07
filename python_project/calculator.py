import tkinter as tk

class Calculator:
    def __init__(self, root):
        self.root = root
        root.title("Simple Calculator")
        root.geometry("320x400")
        root.resizable(False, False)

        self.expression = ""

        self.text_input = tk.StringVar()

        # Entry widget for display
        self.entry = tk.Entry(root, font=('arial', 20, 'bold'), textvariable=self.text_input, bd=10, insertwidth=4,
                              width=14, borderwidth=4, relief='ridge', justify='right')
        self.entry.grid(row=0, column=0, columnspan=4)

        # Buttons
        button_texts = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', 'C', '+',
            '='
        ]

        # Create buttons in grid
        row_val = 1
        col_val = 0
        for bt in button_texts:
            if bt == '=':
                btn = tk.Button(root, text=bt, width=33, height=3, command=self.equal_press)
                btn.grid(row=5, column=0, columnspan=4)
            else:
                btn = tk.Button(root, text=bt, width=8, height=3,
                                command=lambda x=bt: self.button_press(x))
                btn.grid(row=row_val, column=col_val)
                col_val += 1
                if col_val > 3:
                    col_val = 0
                    row_val += 1

    def button_press(self, key):
        if key == 'C':
            self.expression = ""
            self.text_input.set("")
        else:
            self.expression += key
            self.text_input.set(self.expression)

    def equal_press(self):
        try:
            result = str(eval(self.expression))
            self.text_input.set(result)
            self.expression = result
        except Exception:
            self.text_input.set("Error")
            self.expression = ""

if __name__ == "__main__":
    root = tk.Tk()
    calc = Calculator(root)
    root.mainloop()
