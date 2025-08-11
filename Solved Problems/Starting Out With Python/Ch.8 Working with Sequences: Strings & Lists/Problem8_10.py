# Problem from Starting Out With Python by Tony Gaddis
# Chapter 8: Working with Sequences: Strings and Lists
#
# Problem 8.10: Write a program that lets the user enter the total rainfall for each of the 12 months into a list.
#               The program should calculate and display the total rainfall for the year, the average monthly
#               rainfall, and the months with the highest and lowest amounts of rainfall.
#
#
# Author: Giorgio Murad Murad

# Initializing a list that carries the names of the months
months = [
    'January', 'February', 'March', 'April', 'May',
    'June', 'July', 'August', 'September', 'October',
    'November', 'December'
]

# Initializing the required variables for the program
totalRainfall = 0
monthlyRainfalls = []

# Asking the user to enter the amount of rainfall in every month throughout the year
for month in months:
    temp = int(input('Enter the amount of rainfall throughout {}: '.format(month)))
    totalRainfall += temp
    monthlyRainfalls.append(temp)

print()
print()

# Displaying the total yearly rainfall, the average monthly rainfall, and the months with the lowest
# and highest amount of rainfall
average = totalRainfall / len(monthlyRainfalls)
lowestRain   = min(monthlyRainfalls)
lowestMonth  = months[monthlyRainfalls.index(lowestRain)]
highestRain  = max(monthlyRainfalls)
highestMonth = months[monthlyRainfalls.index(highestRain)]


print((
    'The total yearly rainfall is: {total}\n'
    'The average monthly rainfall is: {average:>2.2f}\n'
    'The month with the highest rainfall is {h1} with {h2}\n'
    'The month with the lowest rainfall is {l1} with {l2}\n'
).format(
    total=totalRainfall, average=average, h1=highestMonth,
    h2=highestRain, l1=lowestMonth, l2=lowestRain
    ))