# Problem from Starting Out With Python by Tony Gaddis
# Chapter 6: Value Returning Functions & Modules
#
# Problem 6.5:  An object that is in motion is said to have Kinetic Energy.
#               The following formula to calculate an object's kinetic energy is:
#                       KE = 1/2 * M * V^2
#               (M for the object's mass in kg, and V for the object's velocity in meters per second)
#
#               Write a function that takes an object's mass and velocity, and return's the object's
#               kinetic energy.
#               The program should prompt the user to enter the required values, call the function, and
#               display the value returned.
#
#
# Author: Giorgio Murad Murad
import math

# Function that takes an object's mass and velocity,
# calculates the kinetic energy, and returns its value
def kinetic_energy(m, v):
    ke = (1/2) * m * math.pow(v, 2)
    return ke


# Prompting the user to input the object's mass in kilograms and velocity in meters per second
mass = float(input("Enter the object's mass [kg]: "))
velocity = float(input("Enter the object's velocity [m/s]: "))

# Calling the function, and giving its perimeter values
kinetic = kinetic_energy(mass, velocity)

# Displaying the object's kinetic energy
print("The kinetic energy is: ", kinetic)