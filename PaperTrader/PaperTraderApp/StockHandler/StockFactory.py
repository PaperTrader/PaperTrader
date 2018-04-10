from PaperTraderApp.StockHandler.Stock import Stock
from PaperTraderApp.models import StockModel

class StockFactory:
    def __init__(self):
        pass

    def getStockObject(self, NameOrSymbol):
        symbOk = self.__caseCheck(NameOrSymbol) 
        sm = None
        if(symbOk):
            sm = StockModel(symbol=NameOrSymbol)
        else:
            sm = StockMode(name=NameOrSymbol)
        return Stock(sm.name, sm.symbol, sm.opening)
           

    def __caseCheck(self, string):
        upper = True
        for item in string:
           if item == item.lower():
               upper = False
               return upper
        return upper
