class Car:
    color = None
    fuel = None
    maxSpeed = None
    owner = None

    speed = 0

    def go(self):
        self.speed = 100
    
    def turn(self):
        self.speed = -100
    
    def stop(self):
        self.speed = 0

myCar = Car()
myCar.color = "Blue"
myCar.fuel = 50
myCar.maxSpeed = 120
owner = "Великий Константин"

myCar.go()
print(myCar.speed)