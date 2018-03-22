import User
from TraderApp.Portfolio import *

class Trader(User):

	def __init__(self, portfolio):
		self.__portfolio = Portfolio()

	def getPortfolio(self):
		return self.__portfolio
t = Trader(Portfolio())
