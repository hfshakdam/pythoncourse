#an object is an instance of a class
#naming convention with objects is that the name is in title form
#e.g. Car not car

from Car import Car

car_1 = Car("Chevy","Camaro","2023","Yellow")
#I could make a car_2 using the Car object as a blueprint. So it's reusable

print(car_1.make)
print(car_1.model)
print(car_1.year)
print(car_1.colour)

car_1.drive()
car_1.stop()