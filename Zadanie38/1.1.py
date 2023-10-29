class User:
	_name = None
	
	def _setName(self,name):
		self._name = name 
	
	def getName(self):
		return self._name 


class Employee(User):
	def _setName(self,name):
		if (len(name) > 0):
			self._name = name 
			
empl = Employee()

empl._setName("Постаппеляционный приговор")
print(empl.getName())