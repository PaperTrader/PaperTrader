from abc import ABC, abstractmethod

class Observer(ABC):
    def __init__(self):
        self._stock_subject
    
    @abstractmethod
    def update(self):
        raise NotImplementedError("Observer needs to include this method!")
