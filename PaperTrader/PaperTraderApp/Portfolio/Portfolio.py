from PaperTraderApp.Balance.Balance import Balance

class Portfolio:
    def __init__(self, user):
        self.__balance = Balance()
        self.__stocks = {}
        self.__user = user
#        self.__portfolio = PortfolioModel.objects.get(user=self.__user)

    def getStocks(self):
        return self.__stocks


    def getHistory(self):
        '''
            I have NO idea what we plan on doing here
        '''
        pass

    def getTotalValue(self):
        value = 0
        for st in self.__stocks:
            value += (self.__stocks[st][0]*st.getPrice())

        return value + self.__balance.getBalance()


    def getStockQuantity(self, stock):
        if stock.getSymbol() not in self.__stocks:
            raise StockException

        return self.__stocks[stock.getSymbol()][0]

    def buy(self, stock, quantity):
        '''
            this will handle the balance exceptions
        '''
        self.__balance.sub(stock.getPrice() * quantity)

        '''
            store stock in dict as tuple of quantity and price ( price can be used for history/gain? )
        '''
        self.__stocks[stock.getSymbol()] = (quantity, stock.getPrice())

    def sell(self, stock, quantity):
        if stock.getSymbol() not in self.__stocks:
            raise StockException

        if self.__stocks[stock.getSymbol()][0] < quantity:
            raise StockException

        self.__balance.add(stock.getPrice() * quantity)
        self.__stocks[stock.getSymbol()][0] -= quantity

    def getPortfolioHandler(self):
        pass

    '''
        do we need these ?
    '''
    def addStock(self, stock):
        pass

    def removeStock(self):
        pass

class StockException(Exception):
    def __init__(self):
        self.message = "Insufficient number of stock"
        super().__init__(self.message)

