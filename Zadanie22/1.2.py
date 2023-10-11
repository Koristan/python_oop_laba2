class Validator:
    pass
    def isEmail(self, str):
        if (len(str) > 0):
            index = str.find('@')
            if (str[index+1:] == "mail.ru"):
                return "Correct"
            else:
                return "Incorrect"
            
        else:
            return "Wrong string"
        
valid = Validator()
print(valid.isEmail("kfjssjkfk@mail.ru"))