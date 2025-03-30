# Problem from Starting Out With Python by Tony Gaddis
# Chapter 4: Decision Structures & Boolean Logic
#
# Problem 4.2:  The area of the rectangle is the rectangle's length times its width.
#               Write a program that asks for the length and width of two rectangles.
#               The program should tell the user which rectangle has the greater area,
#               or if the areas are equal.
#
#
# Author: Giorgio Murad Murad

# Prompting the user to enter the length and width of rectangles 1 and 2
width1 = float(input('Enter the width of rectangle 1: '))
length1 = float(input('Enter the length of rectangle 1: '))
width2 = float(input('Enter the width of rectangle 2: '))
length2 = float(input('Enter the length of rectangle 2: '))

# Computing the area values of each of the two rectangles
area1 = width1 * length1
area2 = width2 * length2

# Displaying which rectangle has the greater area, or if both areas are equal
if area1 > area2:
    print('The area of rectangle 1 is greater than the area of rectangle 2')
elif area2 > area1:
    print('The area of rectangle 2 is greater than the area of rectangle 1')
else:
    print('Both rectangles have equal areas')