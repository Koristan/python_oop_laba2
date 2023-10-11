class Student:
  pass

class Employee:
  pass

employee = Employee()
print(isinstance(employee, Employee)) #True
print(isinstance(employee,Student)) #False