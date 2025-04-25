
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, cash):
        if cash > 0:
            self.__balance += cash
        else:
            print("сумма должны быть положительна")
    def withdraw(self, cash):
        if cash <= 0:
            print("Сумма для снятия должна быть положительной")
        elif cash > self.__balance:
            print("Недостаточно средств на счете")
        else:
            self.__balance -= cash
    @property
    def get_balance(self):
        return self.__balance
    @get_balance.setter
    def get_balance(self, value):
        self.__balance = value
