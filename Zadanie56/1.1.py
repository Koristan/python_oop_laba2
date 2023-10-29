class Period:
    time1 = None
    time2 = None

    def __init__(self, time1, time2):

        time_1 = None
        time_2 = None

        time_1 = list(map(int, time1.split(':')))
        time_2 = list(map(int, time2.split(':')))

        self.time1 = time_1[0] * 86400 + time_1[1] * 3600 + time_1[2] * 60 + time_1[0]
        self.time2 = time_2[0] * 86400 + time_2[1] * 3600 + time_2[2] * 60 + time_2[0]

    def getSeconds(self):
        return self.time1 - self.time2
    
    def getMinutes(self):
        return self.time1 / 60 - self.time2 / 60
    
    def getHours(self):
        return self.time1 / 3600 - self.time2 / 3600
    
    def getDays(self):
        return self.time1 / 86400 - self.time2 / 86400
    

per = Period("12:15:35:24", "10:13:14:30")

print(per.getSeconds())
print(per.getMinutes())
print(per.getHours())
print(per.getDays())