import User

class Administrator(User):

	def __init__(self, adminId):
		self.__adminId = adminId

	def getAdminId(self):
		return self.__adminId

	def addStock(self, symb):
		pass

	def getUserByName(self, name):
            nullUser = User(None, None)
                for user in users:
                    if(user.getName() == name): return user
                return nullUser

	def getUserById(self, id_num):
		nullUser = User(None, None)
                for user in users:
                    if(user.getID() == id_num): return user
                return nullUser
