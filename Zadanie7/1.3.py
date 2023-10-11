class Employee():

    name = None
    age = None
    salary = None

    def show(self):
        return self.salary
    
employee = Employee()
employee.salary = 300
print(employee.show())