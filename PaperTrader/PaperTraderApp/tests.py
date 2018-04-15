from django.test import TestCase
from PaperTraderApp.models import StockModel
from PaperTraderApp.StockHandler.StockScraper import StockScraper
from PaperTraderApp.StockHandler.StockObserver import StockObserver
from PaperTraderApp.StockHandler.Stock import Stock
from PaperTraderApp.Users.Trader import Trader
from PaperTraderApp.Balance.Balance import Balance, BalanceException
from PaperTraderApp.Portfolio.Portfolio import Portfolio, StockException
from PaperTraderApp.StockHandler.StockFactory import StockFactory

class StockFactoryTests(TestCase):
    def test_StockFactory(self):
        s = StockFactory()
        s.createStockObject('Tesla', 'TSLA')

class ObserverTests(TestCase):
    def test_observer(self):
        s = Stock('Google Inc', 'GOOG', 0.0)
        StockObserver(s)
        s.notifyObservers()
        self.assertNotEquals(s.getPrice(), 0.0)

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
    
    def test_stockscraper_all(self):
        s = StockScraper('GOOG')
        value = s.getOpen()
        self.assertGreaterEqual(float(value), 0.0)

        value = s.getClose()
        self.assertGreaterEqual(float(value), 0.0)

        value = s.getHigh()
        self.assertGreaterEqual(float(value), 0.0)

        value = s.getLow()
        self.assertGreaterEqual(float(value), 0.0)

        value = s.getVolume()
        self.assertGreaterEqual(float(value), 0.0)

class PortfolioTests(TestCase):
    def test_portfolio_value(self):
        p = Portfolio()
        self.assertEquals(p.getTotalValue(), 0.0)

    def test_portfolio_buy(self):
        p = Portfolio()
        s = Stock('Google Inc', 'GOOG', 90.0)
        try:
            p.buy(s, 2)
        except BalanceException as e:
            self.assertEquals("Value invalid for function", e.message)

    def test_portfolio_sell(self):
        p = Portfolio()
        s = Stock('Google Inc', 'GOOG', 90.0)
        try:
            p.sell(s, 2)
        except StockException as e:
            self.assertEquals("Insufficient number of stock", e.message)

# Create your tests here.
