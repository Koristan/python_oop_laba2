class Employee:
    name = None
    age = None
    salary = None

    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def show(self):
        print(self.salary)

    def procent(self):
        self.salary += int(self.salary * 0.1)

employee = Employee("Жуйка", 15, 120000)
employee.procent()
employee.show()