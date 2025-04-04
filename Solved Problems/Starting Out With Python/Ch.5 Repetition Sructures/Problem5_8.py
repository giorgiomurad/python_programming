# Problem from Starting Out With Python by Tony Gaddis
# Chapter 5: Repetition Structures
#
# Problem 5.7:  Write a program that asks the user to enter a series of positive integers,
#               and displays their sum.
#               The user is asked to enter positive integers that end with a negative integer
#               to signal the program to stop taking numbers, and the program should display the
#               total sum of the numbers entered.
#
#
# Author: Giorgio Murad Murad

# Declaring a boolean variable, and the total sum
doContinue = True
total = 0

# Loop
count = 1
while doContinue:
    temp = int(input("Enter integer {}: ".format(count)))
    if temp < 0:
        doContinue = False
    else:
        total += temp
        count += 1

# Displaying the total sum
print('The total sum is', total)