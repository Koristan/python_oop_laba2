class User:
	def __init__(self,name, surname):
		self.name = name 
		self.surname = surname 
	
	def getName(self):
		return self.name 
	
	def getSurn(self):
		return self.surname 
	
class Employeer(User):
	salary = None
	age = None

	def __init__(self, name, surname, salary, age):
		super().__init__(name, surname)
		self.salary = salary
		self.age = age

	def getSalary(self):
		print(self.salary)

	def getAge(self):
		print(self.age)

empl = Employeer("raz", "dva", 150, 10)
empl.getAge()

	