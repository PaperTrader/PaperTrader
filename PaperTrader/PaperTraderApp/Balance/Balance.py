class Balance:
    def __init__(self):
        self.__balance = 0.0

    def add(self, amount):
        if(amount < 0):
            raise BalanceException
        self.__balance += amount

    def sub(self, amount, balance):
        print(amount, balance)
        if(amount > balance):
            raise BalanceException
        if(amount < 0):
            raise BalanceException

        self.__balance -= amount
        return self.__balance

    def set(self, amount):
        self.__balance = amount

    def getBalance(self):
        return self.__balance

class BalanceException(Exception):
    def __init__(self):
        self.message = "Value invalid for function"
        super().__init__(self.message)
