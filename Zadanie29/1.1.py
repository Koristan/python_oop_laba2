class User:
    def setName(self,name):
        self.name = name 

    def getName(self):
        return self.name 

class Employee(User):
    pass

empl = Employee()

empl.setName("Yasher")
print(empl.getName())