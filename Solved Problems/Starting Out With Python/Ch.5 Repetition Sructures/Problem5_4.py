# Problem from Starting Out With Python by Tony Gaddis
# Chapter 5: Repetition Structures
#
# Problem 5.4:  The distance a vehicle travels can be calculated as follows:
#                   Distance = Speed * Time
#
#               Write a program that asks the user to enter the speed of a vehicle (in miles per hour)
#               and the number of hours it has traveled.
#               The program should include a loop that displays the distance the vehicle has traveled
#               every hour of that time period.
#               Here is an example:
#               Speed of the vehicle    :   40 miles/hour
#               Hours traveled          :   3  hours
#
#               Hour                    Distance Traveled
#               -----------------------------------------
#                   1       |               40
#                   2       |               80
#                   3       |              120
#
#
# Author: Giorgio Murad Murad

# Prompting the user to enter the speed of the vehicle,
# and the number of hours it traveled
speed = int(input('Enter the speed of the traveling vehicle (in miles per hour): '))
hours = int(input('Enter the number of hours: '))

# Displaying Table
print(
    'Hour \t\t | \t\t Distance Traveled'
 '\n--------------------------------------'
)
for hour in range(1, hours + 1):
    print('{h:2d} \t\t\t | \t\t {d:3d}'.format(h=hour, d=(speed*hour)))