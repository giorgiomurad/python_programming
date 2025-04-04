# Problem from Starting Out With Python by Tony Gaddis
# Chapter 6: Value Returning Functions & Modules
#
# Problem 6.9:  Enhance the last program by making the program display all prime
#               numbers from 1 to 100.
#
#
# Author: Giorgio Murad Murad

# Function
def is_prime(integer):
    for i in range(2, integer):
        if integer % i == 0:
            return False

    return True


# Loop to display all prime numbers
print("All prime numbers from 1 to 100:")
for i in range(1, 101):
    if is_prime(i):
        print(i, end=" ")