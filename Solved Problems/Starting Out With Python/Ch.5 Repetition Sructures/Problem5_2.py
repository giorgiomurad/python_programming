# Problem from Starting Out With Python by Tony Gaddis
# Chapter 5: Repetition Structures
#
# Problem 5.2:  Running on a particular treadmill burns 3.9 calories per minute.
#               Write a program that uses a loop to display the number of calories
#               burnt after 10, 15, 20, 25, 30 minutes.-
#
#
# Author: Giorgio Murad Murad

# Declaring calories burned per minute
caloriesPerMinute = 3.9

# For loop for display the results
for i in [10, 15, 20, 25, 30]:
    temp = i * caloriesPerMinute
    print(
        'The amount of calories burnt after {m} minutes is {c:.2f} calories.'
        .format(m=i, c=temp)
    )