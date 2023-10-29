class Circle:
    __radius = 0

    def __init__(self, radius):
        self.__radius = radius

    def square(self):
        return self.__radius * self.__radius * 3.1415
    
    def length(self):
        return self.__radius * 2 * 3.1415
    
cir = Circle(10)

print(cir.square(), cir.length())
