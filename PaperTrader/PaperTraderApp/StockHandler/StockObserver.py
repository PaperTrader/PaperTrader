from PaperTraderApp.models import StockModel
from PaperTraderApp.StockHandler.Observer import Observer
from PaperTraderApp.StockHandler.StockScraper import StockScraper

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
        stockScraper = StockScraper(self.stock_subject.getSymbol())
        stockModel.opening = stockScraper.getOpen()
        stockModel.closing = stockScraper.getClose()
        stockModel.high = stockScraper.getHigh()
        stockModel.low = stockScraper.getLow()
        stockModel.volume = stockScraper.getVolume()
        stockModel.save()
        self.stock_subject._update(stockModel.opening)
