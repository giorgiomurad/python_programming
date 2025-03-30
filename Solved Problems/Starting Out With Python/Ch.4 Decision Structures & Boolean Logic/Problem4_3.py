# Problem from Starting Out With Python by Tony Gaddis
# Chapter 4: Decision Structures & Boolean Logic
#
# Problem 4.3:  An objects mass is measured in kilograms, and it's weight is measured
#               in newtons.
#               The weight of an object is calculated using the below formula:
#                       W = M x 9.8
#
#               Write a program that asks the user for the object's mass, and calculates
#               the weight.
#               If the object weighs more than 1000 newtons, the program should display
#               that the object is too heavy. And if the object weighs less than 10 newtons,
#               the program should display that the object is too light.
#
#
# Author: Giorgio Murad Murad

# Prompting the user to enter the mass of the object
mass = float(input("Enter the mass of the object: "))

# Calculating the weight based on the mass
weight = mass * 9.8

if weight > 1000:
    print('The object is too heavy!')
elif weight >= 10:
    print('The object weighs', weight, 'newtons.')
else:
    print('The object is too light!')