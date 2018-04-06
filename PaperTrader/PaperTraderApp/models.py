from django.db import models
from django.urls import reverse
import json

# Create your models here.
MAX_LENGTH_NAME = 60
MAX_LENGTH_SYMB = 6
MAX_DIGITS = 20


class StockModel(models.Model):
    name = models.CharField(max_length=MAX_LENGTH_NAME)
    symbol = models.CharField(max_length=MAX_LENGTH_SYMB)
    opening = models.DecimalField(max_digits=MAX_DIGITS, decimal_places=2)
    closing = models.DecimalField(max_digits=MAX_DIGITS, decimal_places=2)
    high = models.DecimalField(max_digits=MAX_DIGITS, decimal_places=2)
    low  = models.DecimalField(max_digits=MAX_DIGITS, decimal_places=2)
    volume = models.DecimalField(max_digits=MAX_DIGITS, decimal_places=0)
    
    def __str__(self):
        return "{0} ({1})".format(self.name, self.symbol)

    def get_absolute_url(self):
        return reverse("stock-list", kwargs={ 'pk' : self.pk }) # We'll need this when it comes to deleting stock object

class AdminStockModel(models.Model):
    name = models.CharField(max_length=MAX_LENGTH_NAME)

class PortfolioModel(models.Model):
    stocks = models.CharField(max_length=99999999999)
    balance = models.FloatField()

    def set_stocks(stock_list, self):
        self.stocks = json.dumps(stock_list)
    def get_stocks(self):
        return json.loads(self.stocks)
    

