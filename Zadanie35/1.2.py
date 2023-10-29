class User:
	__name = None
	__surname = None
	
	def setName(self,name):
		self.__name = name 
	
	def getName(self):
		return self.__name 
	
	def setSurn(self, surname):
		self.__surname = surname 
	
	def getSurn(self):
		return self.__surname 
	
	
class Employeer(User):
    def getFull(self):
        return self.__name + ' ' + self.__surname 

empl = Employeer()

empl.setName("Поганец")
print(empl.getFull())