# Problem from Starting Out With Python by Tony Gaddis
# Chapter 4: Decision Structures & Boolean Logic
#
# Problem 4.7:  Rewrite program 3.6 where the program calculates and displays the person's BMI.
#               Enhance the program so that the program would display a message indicating
#               whether the person is in optimal weight, underweight, or overweight.
#
#               A sedentary person's weight is considered to be optimal if his or her BMI is
#               between 18.5 and 25.
#               If the BMI is less than 18.5, the person is considered underweight.
#               If the BMI is greater than 25, the person is considered overweight.
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
    if bmi > 25:
        print('You are overweight')
    elif bmi > 18.5:
        print('Your weight is optimal')
    else:
        print('You are underweight')

#Calling the function
getBMI(weight, height)