from abc import ABC, abstractmethod

class User(ABC):
    def __init__(self, name):
        self.__name = name
        self.__id = 0
        self._users = []

    def getName(self):
        return self.__name

    def _setname(self, name):
        self.__name = name

    def _setID(self, newID):
        self.__id = newID

    def getID(self):
        return self.__id


