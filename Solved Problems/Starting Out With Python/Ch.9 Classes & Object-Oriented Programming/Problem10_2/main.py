# Problem from Starting Out With Python by Tony Gaddis
# Chapter 10: Classes & Object-Oriented Programming
#
# Problem 10.2:     Write a class named Car that has the following data attributes:
#                       - __year_model      (for the car's year model)
#                       - __make            (for the make of the car)
#                       - __speed           (for the car's current speed, should start at value 0)
#
#                   The class should also include the following methods:
#                       - __init__()        (To initialize the car object)
#                       - accelerate()      (Adds five to the speed of the car)
#                       - brake()           (Subtracts five from the speed of the car)
#                       - get_speed()       (Returns the current speed of the car)
#
#
#                   The program should create a Car object, and calls the accelerate method five times.
#                   After every method call, the car's speed should be accessed displayed.
#                   Then, the program should call the brake method five times, and display the car's speed after
#                   every brake call.
#
#
# Author: Giorgio Murad Murad

from Car import Car

# Gathering input from the user
year_model = input("Input the year model of the car: ")
make = input("Input the make of the car: ")

# Creating car object
car = Car(year_model, make)

# Using a loop to call the accelerate method, and display the speed five times
for i in range(5):
    car.accelerate()
    print("The current car speed is", car.get_speed())

print()
print()

# Using a loop to call the brake method, and display the speed five times
for i in range(5):
    car.brake()
    print("The current car speed is", car.get_speed())