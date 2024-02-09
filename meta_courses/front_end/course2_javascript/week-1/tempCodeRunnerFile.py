class Car:
    def __init__(self) -> None:
        self.mileage = 98765
        self.color = 'red'
    
    def turnTheKey(self):
        print('The engine is running')

    def lightsOn(self):
        print('The lights are on.')

car = Car()
print(car)
car.turnTheKey()
car.lightsOn()