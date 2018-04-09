from PaperTraderApp.models import StockModel
from PaperTraderApp.StockHandler.Observer import Observer

class StockObserver(Observer):
    def __init__(self,stock_subject):
        self.stock_subject = stock_subject
        self.stock_subject.attach(self)
    
    '''
    Update to do what we want! But omg. It works!
    Also what we want is to update the price!
    '''
    def update(self):
       sm = StockModel(symbol=self.stock_subject.getName()) 
       print(sm)
