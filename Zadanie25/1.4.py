class Employee:
    __name = None
    __age = None
    __salary = None

    position = None
    departament = None

    def __init__(self, name, age, salary, position, departament):
        self.__name = name
        self.__age = age
        self.__salary = salary
        self.position = position
        self.departament = departament

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

class EmployeeCollection:
    def __init__(self):
        self.__employeers = []

    def add(self, empl):
        self.__employeers.append(empl)
        
    def show(self):
        for i in self.__employeers:
            print(i.getName())

    def summary(self):
        sum = 0
        for i in self.__employeers:
            sum += int(i.getSalary()[:-1])
        print(sum)

emplColl = EmployeeCollection()
emplColl.add(Employee("Petya", 15, 1000, "Moscow", "Pos"))
emplColl.add(Employee("Vanya", 15, 1000, "Moscow", "Pos"))

emplColl.summary()