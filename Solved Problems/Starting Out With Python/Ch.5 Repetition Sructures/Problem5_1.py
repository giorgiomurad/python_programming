# Problem from Starting Out With Python by Tony Gaddis
# Chapter 5: Repetition Structures
#
# Problem 5.1:  A bug collector collects bugs every day for seven days. Write a program
#               that keeps a running total of the number of bugs collected during the week.
#               For each day, the loop should ask the user the number of bugs collected.
#               And after the loop, the program should display the total amount of bugs
#               collected.-
#
#
# Author: Giorgio Murad Murad

# Declaring the number of days throughout the week
NUMBER_OF_DAYS = 7

# Initiating the total number of bugs collected
total = 0

# for loop that iterates according to the number of days
for i in range(NUMBER_OF_DAYS):
    temp = input('Enter the number of bugs collected throughout day ' + str(i+1) + ': ')
    total += int(temp)

# Printing the final result
print('The total number of bugs collected throughout the week is', total)