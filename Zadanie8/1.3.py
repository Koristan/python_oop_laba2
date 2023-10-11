class Student:
    name = None
    surname = None

    def iniziali(self):
        return f"{self.name[0].upper()}.{self.surname[0].upper()}."
    
student = Student()
student.name = "чернь"
student.surname = "нечернь"
print(student.iniziali())