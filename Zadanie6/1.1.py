class Employee():

    name = None
    age = None
    salary = None

    def show(self):
        return f"{self.name} --- {self.salary}"
    
employee = Employee()
employee.name = "Петр Первый"
employee.salary = 300
print(employee.show())