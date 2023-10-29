class User:
	__name = ''

	def setName(self,name):
		self.__name = name

	def getName(self):
		return self.__name

class Employee(User):
	__name = None
	def setName(self,name):
		if (len(name) > 0):
			self.__name = self.getName()