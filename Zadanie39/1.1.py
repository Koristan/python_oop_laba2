class User:
    name = None

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name
    
class Employee(User):
    age = 0

    def setAge(self, age):
        self.age = age

    def getAge(self):
        return self.age

class Programmer(Employee):
    language = None

    def setLanguage(self, language):
        self.language = language

    def getLanguage(self):
        return self.language
    
class Desinger(Employee):
    programm = None

    def setProgramm(self, programm):
        self.programm = programm

    def getProgramm(self):
        return self.programm