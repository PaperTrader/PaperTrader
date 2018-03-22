import json
import urllib.request
import datetime
from enum import Enum

API_KEY = "ZB98IZZOUGC86XX6"
# kate-spencer-6
class Api_Type(Enum):
    DAILY = "TIME_SERIES_DAILY"
    WEEK = "TIME_SERIES_WEEKLY"

class StockScraper:
    def __init__(self, api_type, symbol):
        if(not isinstance(api_type, Api_Type)):
            api_type = Api_Type.DAILY
        self.api_type = api_type
        
    def getQuote(self, symbol):
        print(self.api_type)
        url = "https://www.alphavantage.co/query?function={0}&symbol={1}&interval=1min&outputsize=compact&apikey={2}".format('TIME_SERIES_DAILY', symbol, API_KEY)
        response = urllib.request.urlopen(url)
        data = json.loads(response.read())
        daily_data = data['Time Series (Daily)']
        return daily_data[str(datetime.date.today())]
    
    '''
        Day should be in format YYYY-MM-DD
    '''
    
s = StockScraper(Api_Type.DAILY, 'GOOG')
print(s.getQuote('GOOG'))
