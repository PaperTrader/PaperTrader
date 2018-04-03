from django.test import TestCase
from PaperTraderApp.models import StockModel
from PaperTraderApp.StockHandler.StockHandler import StockScraper
from PaperTraderApp.Users.Trader import Trader

class UserTests(TestCase):
    def test_user(self):
        test = Trader("Bob")
        self.assertEquals(test.getName(), 'Bob')

    def test_setName(self):
        test = Trader("Test")
        test._setname("Test1")
        self.assertEquals(test.getName(), 'Test1')

    def test_getID(self):
        test = Trader("Test")
        test._setID(10)
        self.assertEquals(test.getID(), 10)

class StockTests(TestCase):
    def test_retrive(self):
        stock = StockModel(name="Google Inc",
                           symbol="GOOG")
        self.assertEquals(str(stock), 'Google Inc (GOOG)')
    
    def test_stockscraper_singleton(self):
        s = StockScraper()
        s2 = StockScraper()
        self.assertEquals(s, s2)

    def test_stockscraper_open(self):
        s = StockScraper()
        value = s.getOpen('GOOG')
        self.assertGreaterEqual(float(value), 0.0)

    def test_stockscraper_close(self):
        s = StockScraper()
        value = s.getClose('GOOG')
        self.assertGreaterEqual(float(value), 0.0)

    def test_stockscraper_high(self):
        s = StockScraper()
        value = s.getHigh('GOOG')
        self.assertGreaterEqual(float(value), 0.0)

    def test_stockscraper_low(self):
        s = StockScraper()
        value = s.getLow('GOOG')
        self.assertGreaterEqual(float(value), 0.0)

    def test_stockscraper_volume(self):
        s = StockScraper()
        value = s.getVolume('GOOG')
        self.assertGreaterEqual(float(value), 0.0)

# Create your tests here.
