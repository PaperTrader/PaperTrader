'''
    Using the InvalidBalanceException, will require a try/catch
    
    try:
        Balance#add(-1)
    except InvalidBalanceException as e:
        print(str(e))
'''
class Balance:
    def __init__(self):
        self.__balance = 0.0
    def add(self, amount):
        if(amount <= 0):
            raise InvalidBalanceException("Amount to add less than zero")
        self.__balance += amount

    def sub(self, amount):
        if(amount > self.__balance):
            raise InvalidBalanceException("Amount to subtract exceeds current balance")
        self.__balance -= balance

    def set(self, amount):
        if(amount < 0):
            raise InvalidBalanceException("Amount can not be less than zero")
        self.__balance = 0

    def getBalance(self):
        return self.__balance



class InvalidBalanceException(Exception):
    pass
