class Employee():

    name = None
    age = None
    salary = None

    def show(self):
        return self.name
    
employee = Employee()
employee.name = "Петр Я"
print(employee.show())