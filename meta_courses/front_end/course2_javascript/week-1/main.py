# for i in range(2,10):
#     print(f'\nTabuada do {i}')
#     for x in range(1,10):
#         print(f'{i}x{x} = {i*x}')

f2 = [n**2 for n in range(2,11)]
print(f2)



def listBuilder(*args):
    list_builder = [arg for arg in args]
    return list_builder

list_builder = listBuilder('a','b','c','d')
print(list_builder)


st = lambda x: x**2
print(st(2))

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