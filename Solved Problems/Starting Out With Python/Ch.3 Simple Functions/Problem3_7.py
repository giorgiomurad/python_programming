# Problem from Starting Out With Python by Tony Gaddis
# Chapter 3: Simple Functions
#
# Problem 3.7:  A nutritionist who works for a fitness club helps members by evaluating
#               their diet.
#               As part of her evaluation, she asks members for the number of fat grams
#               and carbohydrates consumed daily. Then, she calculates the amount of
#               calories that result from the fat, using the following formula:
#                       Calories = Fat x 9
#
#               Next, she calculates the number of calories that result from the
#               carbohydrates using the following formula:
#                       Calories = Carbs x 4
#
#               Write a program that helps the nutritionist calculate a person's
#               amount of calories, and displays their result.
#
#
# Author: Giorgio Murad Murad

# Prompting the user to enter the amount of fat and carbohydrates consumed daily
fat = float(input('Enter the amount of fat consumed daily: '))
cb  = float(input('Enter the amount of carbohydrates consumed daily: '))


# Method to calculate and display calories from fat
def fatCalories(f):
    calories = f * 9
    print('The amount of calories from fat is ', calories)

# Method to calculate and display calories from carbohydrates
def cbCalories(c):
    calories = cb * 4
    print('The amount of calories from carbohydrates is ', calories)

# Method to call methods
def getCalories(f, c):
    fatCalories(f)
    cbCalories(c)


# Calling the main function, giving it the value of fat and carbohydrates
getCalories(fat, cb)