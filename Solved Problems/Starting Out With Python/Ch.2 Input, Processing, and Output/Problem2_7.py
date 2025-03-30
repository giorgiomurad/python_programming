# Problem from Starting Out With Python by Tony Gaddis
# Chapter 2: Designing a Program
#
# Problem 2.7:  A car's miles per gallon can be calculated using the following formula:
#                   MPG = miles / gallons
#               Write a program that prompts the user to enter the miles traveled and the amount
#               of gallons, and displays the car's miles per gallon.
#
#
# Author: Giorgio Murad Murad

# Prompting the user to input the value of miles and gallons
miles = float(input("Enter the distance in miles: "))
gallons = float(input("Enter the amount of gallons: "))

# Computing the value of miles per gallon
milesPerGallon = miles / gallons

# Displaying Result
print("The miles per gallon is ", milesPerGallon)