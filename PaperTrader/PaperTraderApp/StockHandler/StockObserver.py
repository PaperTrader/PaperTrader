from PaperTraderApp.StockHandler.Observer import Observer
from PaperTraderApp.models import StockModel

class StockObserver(Observer):
    def __init__(stock_subject):
        self.stock_subject = stock_subject
        self.stock_subject.attach(self)

    def update(self):
        #TODO: Update code goes here!
        pass
