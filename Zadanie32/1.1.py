class User:
	def setAge(self,age):
		if (age >= 0):
			self.age = age
		else:
			raise Exception('need age more 0')

class Employee(User):
	def setAge(self, age):
		if (age <= 120):
			if (age >= 0):
				User.setAge(self, age)
			else:
				raise Exception('need age more 0')
		else:
			raise Exception('need age less 120')

eml = Employee()

eml.setAge(15)
print(eml.age)