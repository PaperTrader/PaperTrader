from PaperTraderApp.models import StockModel
from PaperTraderApp.StockHandler.Observer import Observer
from PaperTraderApp.StockHandler.StockHandler import StockScraper

class StockObserver(Observer):
    def __init__(self,stock_subject):
        self.stock_subject = stock_subject
        self.stock_subject.attach(self)
    
    '''
    Update to do what we want! But omg. It works!
    Also what we want is to update the price!
    '''
    def update(self):
        stockModel = StockModel(symbol=self.stock_subject.getSymbol()) 
        stockScraper = StockScraper()
        updateQuote = stockScraper.getQuote(self.stock_subject.getSymbol())
        stockModel.opening = updateQuote['1. open']
        stockModel.closing = updateQuote['4. close']
        stockModel.high = updateQuote['2. high']
        stockModel.low = updateQuote['3. low']
        stockModel.volume = updateQuote['5. volume']
        stockModel.save()
        self.stock_subject._update(stockModel.opening)
