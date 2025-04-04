# Problem from Starting Out With Python by Tony Gaddis
# Chapter 6: Value Returning Functions & Modules
#
# Problem 6.7:  Write a program that generates 100 random numbers, and displays how
#               many even numbers were generated, and how many odd numbers were generated.
#
#
# Author: Giorgio Murad Murad
import random

# Declaring variables corresponding to the number of even and odd numbers
even = 0
odd = 0

# Loop
for i in range(100):
    temp = random.randint(1,100)

    if temp % 2 == 0:
        even += 1
    else:
        odd += 1

# Displaying result after the loop
print("The number of even numbers generated is", even)
print("The number of odd numbers generated is", odd)