# Problem from Starting Out With Python by Tony Gaddis
# Chapter 3: Simple Functions
#
# Problem 3.6:  Write a program that calculates and displays the person's
#               body mass index (BMI).
#
#               The formula to calculate a person's BMI is:
#                   BMI = (weight x 703) / (height x height)
#               The weight is in pounds, and the height is in inches.
#
#
# Author: Giorgio Murad Murad

# Prompting the user to enter the weight and height
weight = float(input("Enter your weight in pounds: "))
height = float(input("Enter your height in inches: "))

# Function to calculate and display the person's BMI
def getBMI(w, h):
    bmi = (w * 703) / (h * h)
    print('Your calculated BMI is', bmi)

#Calling the function
getBMI(weight, height)