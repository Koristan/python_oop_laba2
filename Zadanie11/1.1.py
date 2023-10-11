class Employee:
    name = "Жуйка"
    age = None
    salary = 100000

    def __init__(self):
        print(self.name, "---", self.salary)

employee = Employee()