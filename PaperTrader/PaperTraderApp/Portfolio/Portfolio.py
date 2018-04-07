from PaperTraderApp.Balance.Balance import Balance
class Portfolio:
    def __init__(self):
        self.__balance = Balance()
        self.__stocks = {}

    def getStocks(self):
        return self.__stocks

    def getHistory(self):
        '''
            I have NO idea what we plan on doing here
        '''
        pass

