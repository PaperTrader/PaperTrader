from PaperTraderApp.Users.User import User
class Trader(User):
    def __init__(self, name):
        super().__init__(name)
        self.__portfolio = None
    def getPortfolio():
        return self.__portfolio
