import re
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
        
    def isDomain(self, str):
        if len(hostname) > 255:
            return False
        if hostname[-1] == ".":
            hostname = hostname[:-1]
        allowed = re.compile("(?!-)[A-Z\d-]{1,63}(?<!-)$", re.IGNORECASE)
        return all(allowed.match(x) for x in hostname.split("."))
