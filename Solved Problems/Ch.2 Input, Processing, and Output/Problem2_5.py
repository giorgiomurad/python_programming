# Problem from Starting Out With Python by Tony Gaddis
# Chapter 2: Designing a Program
#
# Problem 2.5:  The distance of a traveling car can be calculated using the following
#               formula:
#                   Distance = Speed x Time
#               For a car that's traveling at the speed of 60 miles / hour,
#               Write a program that displays:
#                   . The distance of a 5 hour trip
#                   . The distance of an 8 hour trip
#                   . The distance of a 12 hour trip
#
#
# Author: Giorgio Murad Murad

# Speed of the traveling car
SPEED = 60

# The time of different trips
trip1 = 5
trip2 = 8
trip3 = 12

# Calculating the distance of every trip according to the speed and time
distance1 = SPEED * trip1
distance2 = SPEED * trip2
distance3 = SPEED * trip3

# Printing the results
print('The distance of a', trip1, 'hour trip is:', distance1, 'miles')
print('The distance of a', trip2, 'hour trip is:', distance2, 'miles')
print('The distance of a', trip3, 'hour trip is:', distance3, 'miles')