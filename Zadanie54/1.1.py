class Rectangle:
    length = 0
    height = 0

    def __init__(self, len, heig):
        self.length = len
        self.height = heig

    def getSquare(self):
        return self.length * self.height
    
    def getPerimeter(self):
        return self.length * 2 + self.height * 2
    
    def getRatio(self):
        return self.getSquare() / self.getPerimeter()
    
rect = Rectangle(5, 5)

print(rect.getRatio())