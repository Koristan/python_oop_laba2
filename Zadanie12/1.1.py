class Employee:
    name = None
    age = None
    salary = None

    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

employee = Employee("Жуйка", 15, 120000)