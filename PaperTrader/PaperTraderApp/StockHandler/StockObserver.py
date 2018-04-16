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
        symbol = self.stock_subject.getSymbol()
        stockModel = None
        info = StockScraper(symbol)
        opening, closing, high, low, volume = info.getOpen(), info.getClose(), info.getHigh(), info.getLow(), info.getVolume()
        try:
            stockModel = StockModel.objects.get(symbol=self.stock_subject.getSymbol())
            stockModel.opening = opening
            stockModel.closing = closing
            stockModel.high = high
            stockModel.low = low
            stockModel.volume = volume
            stockModel.save()
        except StockModel.DoesNotExist:
            stockModel = StockModel.objects.create(name='NoName',symbol=symbol,opening=opening,closing=closing,high=high,low=low,volume=volume)
        self.stock_subject._update(stockModel.opening)
