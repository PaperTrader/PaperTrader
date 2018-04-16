from PaperTraderApp.StockHandler.Stock import Stock
from PaperTraderApp.models import StockModel
from PaperTraderApp.StockHandler.StockObserver import StockObserver
from PaperTraderApp.StockHandler.StockScraper import StockScraper


# Use the FlyWeight design pattern?

class StockFactory:
    def __init__(self):
        self.stock_list = {}
    def getStockObject(self, symbol):
        if(symbol in self.stock_list.keys()):
            return self.stock_list[symbol]
        self.stock_list[symbol] = self.createStockObject(symbol)
        return self.stock_list[symbol]

    def createStockObject(self, symb):
        model = StockModel(symbol=symb)
        scraper = StockScraper(symb)
        stock = Stock(model.name, model.symbol, model.opening) 
        StockObserver(stock)
        return stock

    def updateAll(self):
        stocks = StockModel.objects.values('name', 'symbol')
        for item in stocks:
            stock = self.getStockObject(item['symbol'])
            print("Attempting to update {}".format(stock))
            stock.notifyObservers()
