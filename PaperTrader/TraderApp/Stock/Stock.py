class Stock:
    def __init__(self, name, symbol, price):
        self.__name = name     # String
        self.__symbol = symbol # String
        self.__price = price   # Float

    '''
    Not sure how we should handle the stock object being static in the sense
    that once we create it we can't neccesarily modify values.

    An important note here is that price will be update when the update
    method gets called from the Subject.

    Using observer here is probably the best, where the stock is the
    observer and the subject is trader/portfolio
    '''


    def getName():
        return this.__name

    def getSymbol():
        return this.__symbol

    def getPrice():
        return this.__price

    def update(): # To be used with the observer pattern, or visitor
        pass

