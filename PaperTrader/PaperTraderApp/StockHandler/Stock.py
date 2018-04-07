class Stock:
    def __init__(self, name, symbol, price):
        self.__name = name
        self.__symbol = symbol
        self.__price = price

    def getName(self):
        return self.__name 

    def getSymbol(self):
        return self.__symbol

    def getPrice(self):
        return self.__price

    def _update(price):
        self.price = price
    
