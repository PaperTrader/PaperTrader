import json
import urllib.request
import datetime
from enum import Enum
from PaperTraderApp.StockHandler.Stock import Stock
import time


API_KEY = "ZB98IZZOUGC86XX6"

class StockScraper:
    def __init__(self, symbol):
        self.symbol = symbol
        self.quote = self.__getQuote(self.symbol)
    
    def __getQuote(self, symbol):
        time.sleep(2)
        url = "https://www.alphavantage.co/query?function={0}&symbol={1}&interval=1min&outputsize=compact&apikey={2}".format('TIME_SERIES_DAILY', symbol, API_KEY)
        #print("----------------------------")
        #print(url)
        #print("----------------------------")
        #print("Attempting to get quote for {}".format(symbol))

        response = urllib.request.urlopen(url)
        data = json.loads(response.read())
        daily_data = data['Time Series (Daily)']
        data = None
        data = daily_data[self.getMostRecentBusinessDay()]
        return data

    def getOpen(self):
        return self.quote['1. open']

    def getClose(self):
        return self.quote['4. close']

    def getHigh(self):
        return self.quote['2. high']

    def getLow(self):
        return self.quote['3. low']

    def getVolume(self):
        return self.quote['5. volume']

    def getMostRecentBusinessDay(self):
        today = datetime.datetime.today()
        weekdays = [0, 1, 2, 3, 4]
        if(today.weekday() in weekdays) and (today.hour > 9):
            return str(today).split()[0]
        shift = datetime.timedelta(max(1,(today.weekday() + 6) % 7 - 3))
        today = today - shift
        return str(today).split()[0]
