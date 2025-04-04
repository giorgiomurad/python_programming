# Problem from Starting Out With Python by Tony Gaddis
# Chapter 5: Repetition Structures
#
# Problem 5.7:  Write a program that calculates the amount of money the person
#               would earn over a period of time if his or her salary is one penny
#               the first day, two pennies the second day, and continues to double
#               every day.
#               The program should ask the user to enter the number of days, and displays
#               a table showing what the salary was for each day.
#               The program then shows the total pay at the end of the period in dollars,
#               not in pennies.-
#
#
# Author: Giorgio Murad Murad

# Prompting the user to enter the number of days of saving pennies
days = int(input('Enter how many days are for saving money: '))

# Declaring pennies and total pennies
pennies = 1
tpennies = 0

# Using a for-loop to display the table
print('Day \t | \t Pennies \t | \t Total Saved ($)')
print('-------------------------------------------')
for day in range(1, days + 1):
    tpennies += pennies
    print(
        '{d:3d} \t | \t {p:5d} \t\t | \t ${tp:5.2f}'
        .format(d=day, p=pennies, tp=(tpennies / 100))
        )
    pennies *= 2