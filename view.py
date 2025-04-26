import tkinter as tk


class CalculatorView:
    def __init__(self, root):
        self.entry = tk.Entry(root)
        self.entry.place(x=20, y=20)

        self.btn = tk.Button(root, text='Вычислить')
        self.btn.place(x=20, y=60)

        self.lbl = tk.Label(root)
        self.lbl.place(x=200, y=20)
    def set_result(self, result):
        self.lbl.config(text=f'= {result}')

    def get_expression(self):
        return self.entry.get()
