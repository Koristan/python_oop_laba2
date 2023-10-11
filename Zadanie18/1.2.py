class Employee:
    __name = None
    __age = None
    __salary = None

    def __init__(self, name, age, salary):
        self.__name = name
        self.__age = age
        self.__salary = salary

    def getName(self):
        return self.__name
    
    def getAge(self):
        return self.__age
    
    def getSalary(self):
        return f"{self.__salary}$"
    
    def setName(self, name):
        self.__name = name
    
    def setAge(self, age):
        if (age > 120 or age < 0):
            raise Exception("Age is incorrect")
        else:
            self.__age = age
    
    def setSalary(self, salary):
        self.__salary = salary
    
empl = Employee("dral", 10, 10000)

print(empl.getSalary())