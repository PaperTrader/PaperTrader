
def generateID():
   return 1 # TODO: Make this do something actually important
class User:
    def __init__(self, name):
        self.__name = name
        self.__id = generateID()
        self.__users = []
        
        '''
        The class diagram specifies a protected list of users.
        Forgot what the purpose of that was, and not sure if it's neccesary.
        That said, we can use the Composite Design pattern here to do this
        Check out:
        https://github.com/Dpasi314/DesignPatterns/blob/master/src/main/java/Composite/Employee.java

        Similarily, we'll probably end up using a UserFactory looking at this now in order to generate users.
        Not sure if I'm jumping the gun though on that one.
        '''
    def getName(self):
        return self.__name
    
    def setName(self, name):
        #TODO: Any restritions that we should care about here?
        self.__name = name
    
    def getID(self):
        return self.__id



        
        
