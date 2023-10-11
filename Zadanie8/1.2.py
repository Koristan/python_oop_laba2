class Student:
    name = None
    surname = None

    def first_letter(self):
        return f"{self.name[0].upper()}{self.name[1:]}"
    
student = Student()
student.name = "чернь"
print(student.first_letter())