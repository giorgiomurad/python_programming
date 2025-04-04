# Problem from Starting Out With Python by Tony Gaddis
# Chapter 6: Value Returning Functions & Modules
#
# Problem 6.3:  The following formula can be used to calculate the distance
#               of a fallen object:
#                                   Distance = (1/2)Gravity * Time^2
#
#               Write a program that asks the user to enter the time it took
#               for a fallen object to reach the ground, and calls the function
#               that calculates and returns the distance of the fall.
#               (The time is in seconds, and the Gravity is 9.8)
#
#
# Author: Giorgio Murad Murad
import math


# Function that takes the time value in seconds, and returns the distance of the fall
def fallen_object(ts):
    d = (1/2) * 9.8 * math.pow(ts, 2)
    return d


# Prompting the user to enter the value of time of a fallen object (in seconds)
time = int(input("Enter the time it took for a fallen object to reach the ground: "))

# Calling the function, and assigning the returned value to a variable
distance = fallen_object(time)

# Displaying Result
print("The distance of the fallen object is", distance)