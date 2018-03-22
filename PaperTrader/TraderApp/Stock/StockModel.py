from django.db import models

MAX_LENGTH_NAME = 60
MAX_LENGTH_SYMBOL = 6

class StockModel(models.Model):
	
	name = models.CharField(max_length = MAX_LENGTH_NAME)
	symbol = models.CharField(max_length = MAX_LENGTH_SYMBOL)

