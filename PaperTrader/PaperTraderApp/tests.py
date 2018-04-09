from django.test import TestCase
from PaperTraderApp.models import StockModel
from PaperTraderApp.StockHandler.StockHandler import StockScraper
from PaperTraderApp.StockHandler.StockObserver import StockObserver
from PaperTraderApp.StockHandler.Stock import Stock
from PaperTraderApp.Users.Trader import Trader
from PaperTraderApp.Balance.Balance import Balance, BalanceException

class ObserverTests(TestCase):
    def test_observer(self):
        s = Stock('Google Inc', 'GOOG', 90.0)
        StockObserver(s)
        s.notifyObservers()
class BalanceTests(TestCase):
    def test_balance(self):
        b = Balance()
        self.assertEquals(b.getBalance(), 0.0)

    def test_balance_add(self):
        b = Balance()
        b.add(10.0)
        self.assertEquals(b.getBalance(), 10.0)

    def test_balance_sub(self):
        b = Balance()
        b.add(10.0)
        b.sub(5.0)
        self.assertEquals(b.getBalance(), 5.0)

    def test_balance_set(self):
        b = Balance()
        b.add(10.0)
        b.set(9.0)
        self.assertEquals(b.getBalance(), 9.0)

    def test_balance_add_exception(self):
        b = Balance()
        try:
            b.add(-1.0)
        except BalanceException as e:
            self.assertEquals("Value invalid for function", e.message)

    def test_balance_sub_exception1(self):
        b = Balance()
        try:
            b.sub(-1.0)
        except BalanceException as e:
            self.assertEquals("Value invalid for function", e.message)

    def test_balance_sub_exception2(self):
        b = Balance()
        b.set(100)
        try:
            b.sub(101)
        except BalanceException as e:
            self.assertEquals("Value invalid for function", e.message)


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
