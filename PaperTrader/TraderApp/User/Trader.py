import User

class Trader(User):

	def __init__(self, portfolio):
		self.__portfolio = portfolio

	def getPortfolio(self):
		return self.__portfolio