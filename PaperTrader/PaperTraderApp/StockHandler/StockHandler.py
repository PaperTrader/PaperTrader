import json
import urllib.request
import datetime
from enum import Enum
from PaperTraderApp.StockHandler.Stock import Stock
import http.client


API_KEY = "ZB98IZZOUGC86XX6"
class Singleton(type):
    def __init__(cls, name, bases, attrs, **kwargs):
        super().__init__(name, bases, attrs)
        cls._instance = None

    def __call__(cls, *args, **kwargs):
        if(cls._instance is None):
            cls._instance = super().__call__(*args, **kwargs)
        return cls._instance

'''
{'1. open': '93.7400', '2. high': '93.9000', '3. low': '92.1100', '4. close': '92.8900', '5. volume': '31752589'} (
'''

'''
Modifications to be done:
    - That copy paste code of result = self.getQuote(symbol) in all of the #get functions, is no bueno. We should store the data and then access it until we modify the Singleton
        - But wait? Isn't that creating a global variable. Isn't that exactly what Singleton isn't supposed to be doing?
        - Is Singleton even the right thing to be doing here? Using it to condense the API calls so just one class....hmmm

'''
class StockScraper(metaclass=Singleton):
    def getQuote(self, symbol):
        url = "https://www.alphavantage.co/query?function={0}&symbol={1}&interval=1min&outputsize=compact&apikey={2}".format('TIME_SERIES_DAILY', symbol, API_KEY)
        response = urllib.request.urlopen(url)
        data = json.loads(response.read())
        daily_data = data['Time Series (Daily)']
        data = None
        data = daily_data[self.getMostRecentBusinessDay()]
        return data

    def getOpen(self, symbol):
        result = self.getQuote(symbol)
        return result['1. open']

    def getClose(self, symbol):
        result = self.getQuote(symbol)
        return result['4. close']

    def getHigh(self, symbol):
        result = self.getQuote(symbol)
        return result['2. high']

    def getLow(self, symbol):
        result = self.getQuote(symbol)
        return result['3. low']

    def getVolume(self, symbol):
        result = self.getQuote(symbol)
        return result['5. volume']

    def getMostRecentBusinessDay(self):
        today = datetime.datetime.today()
        weekdays = [0, 1, 2, 3, 4]
        if(today.weekday() in weekdays):
            return str(today).split()[0]
        shift = datetime.timedelta(max(1,(today.weekday() + 6) % 7 - 3))
        today = today - shift
        return str(today).split()[0]
