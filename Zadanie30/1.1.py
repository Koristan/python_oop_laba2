class User:
    def setName(self,name):
        self.name = name 

    def getName(self):
        return self.name 

class Employee(User):
    
    def getSalary(self):
        return self.__salary
    
    def setSalary(self, salary):
        self.__salary = salary
    