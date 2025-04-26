from model import Model
from view import CalculatorView

class CalculatorController:
    def __init__(self, root):
        self.model = Model()
        self.view = CalculatorView(root)
        self.view.btn.config(command=self.calculate)
        self.view.entry.bind("<Return>", lambda e: self.calculate())

    def calculate(self):
        expression = self.view.get_expression()
        result = self.model.calculate(expression)
        self.view.set_result(result)
