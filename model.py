class Model:
    def calculate(self, expression):
        try:
            return str(eval(expression))
        except:
            return "Ошибка"
