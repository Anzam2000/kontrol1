from controller import CalculatorController
import tkinter as tk

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("400x150")
    app = CalculatorController(root)
    root.mainloop()
