# Zach Thomas
# M03 Lab - Case Study: Lists, Functions, and Classes
# 4/4/2024

class Vehicle():
    def __init__(self, car):
        self.car = car

class Automobile(Vehicle):
    def __init__(self, year, make, model, doors, roof, car):
        super().__init__(car)
        self.car = car
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof

car = input('Enter the vehicle type(car/truck/plane/boat/broomstick): ')
year = input('Enter the vehicle year: ')
make = input('Enter the vehicle make: ')
model = input('Enter the vehicle model: ')
doors = input('Enter the amount of wheels(2 or 4): ')
roof = input('Enter the type of roof (solid or sun roof): ')

print('Vehicle type:', car)
print('Year:', year)
print('Make:', make)
print('Model:', model)
print('Number of doors:', doors)
print('Type of roof:', roof)