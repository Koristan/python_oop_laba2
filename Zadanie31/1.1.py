class User:
    def setName(self,name):
        self.name = name 

    def getName(self):
        return self.name 

class Employee(User):
    def getName(self):
        return self.__name
    
    def getSurName(self):
        return self.__surname
    
    def getSalary(self):
        return self.__salary
    
    def setName(self, name):
        self.__name = name

    def setSurName(self, surname):
        self.__surname = surname
    
    def setSalary(self, salary):
        self.__salary = salary

    def getAge(self):
        return self.__age
    
    def setAge(self, age):
        self.__age = age
