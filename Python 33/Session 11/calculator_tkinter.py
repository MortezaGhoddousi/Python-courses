import tkinter as tk

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Python Calculator")
        self.root.geometry("340x470")
        self.root.resizable(False, False)

        self.expression = ""

        self.display = tk.Entry(
            root,
            font=("Arial", 22),
            bd=10,
            relief=tk.RIDGE,
            justify="right"
        )
        self.display.pack(fill="both", padx=10, pady=10, ipady=10)

        self.create_buttons()

    def update_display(self):
        self.display.delete(0, tk.END)
        self.display.insert(0, self.expression)

    def press(self, value):
        self.expression += str(value)
        self.update_display()

    def clear(self):
        self.expression = ""
        self.update_display()

    def backspace(self):
        self.expression = self.expression[:-1]
        self.update_display()

    def calculate(self):
        try:
            result = str(eval(self.expression))
            self.expression = result
        except Exception:
            self.expression = "Error"
        self.update_display()

    def create_buttons(self):
        frame = tk.Frame(self.root)
        frame.pack(expand=True, fill="both", padx=10, pady=5)

        buttons = [
            ["C", "⌫", "%", "/"],
            ["7", "8", "9", "*"],
            ["4", "5", "6", "-"],
            ["1", "2", "3", "+"],
            ["0", ".", "=", ""]
        ]

        for r, row in enumerate(buttons):
            for c, text in enumerate(row):
                if text == "":
                    continue

                if text == "=":
                    command = self.calculate
                    bg = "#4CAF50"
                    fg = "white"
                elif text == "C":
                    command = self.clear
                    bg = "#f44336"
                    fg = "white"
                elif text == "⌫":
                    command = self.backspace
                    bg = "#ff9800"
                    fg = "white"
                else:
                    command = lambda t=text: self.press(t)
                    bg = "#e0e0e0"
                    fg = "black"

                button = tk.Button(
                    frame,
                    text=text,
                    command=command,
                    font=("Arial", 18, "bold"),
                    bg=bg,
                    fg=fg,
                    relief=tk.RAISED,
                    bd=3
                )

                button.grid(row=r, column=c, sticky="nsew", padx=4, pady=4)

        for i in range(5):
            frame.rowconfigure(i, weight=1)

        for i in range(4):
            frame.columnconfigure(i, weight=1)


def main():
    root = tk.Tk()
    Calculator(root)
    root.mainloop()


if __name__ == "__main__":
    main()