from PaperTraderApp.StockHandler.Observer import Observer
import datetime as dt


class Stock:
    def __init__(self, name, symbol, price):
        self.__name = name
        self.__symbol = symbol
        self.__price = price
        self.__lastUpdate = dt.datetime.now()

        # Below is everthing for Observer
        self.observers = [] # List of observers attatched to this subject, right now will only be Stock

    def getName(self):
        return self.__name 

    def getSymbol(self):
        return self.__symbol

    def getPrice(self):
        return self.__price

    def _update(self, price):
        self.__price = price

    def attach(self, observer):
        if not isinstance(observer, Observer):
            raise InvalidObserverException("Invalid observer type")
        self.observers.append(observer)
   
    def notifyObservers(self):
        if(not (dt.datetime.now() - self.__lastUpdate).total_seconds() > 21600): #This is 6 hours
            print("Unwilling to update. Current time diff is: ", (dt.datetime.now() - self.__lastUpdate).total_seconds())
            return
        for observer in self.observers:
            observer.update()
        self.__lastUpdate = dt.datetime.now()

    def __repr__(self):
        return "{} ({})".format(self.__name, self.__symbol)

class InvalidObserverException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)
