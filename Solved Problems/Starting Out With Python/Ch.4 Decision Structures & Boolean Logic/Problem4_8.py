# Problem from Starting Out With Python by Tony Gaddis
# Chapter 4: Decision Structures & Boolean Logic
#
# Problem 4.8:  Write a program that asks the user to enter the number of seconds,
#               and works as follows:
#                       - There are 60 seconds in a minute.
#                         If the number of seconds is greater than 60, the program should display
#                         how many minutes the given seconds make
#                       - There are 3600 seconds in an hour.
#                         If the number of seconds is greater than 3600, the program should display
#                         how many hours the given seconds make
#                       - There are 86400 seconds in a day.
#                         If the number of seconds is greater than 86400, the program should display
#                         how many days the given seconds make
#
#
# Author: Giorgio Murad Murad

# Declaring seconds per minute, seconds per hour, and seconds per day
SECONDS_PER_MINUTE = 60
SECONDS_HOUR = 3600
SECONDS_PER_DAY = 86400

# Prompting the user to enter the number of seconds
seconds = int(input("Enter number of seconds: "))

# Displaying Result
if seconds >= SECONDS_PER_DAY:
    days = int(seconds / SECONDS_PER_DAY)
    print(days, 'days.')
if seconds >= SECONDS_HOUR:
    hours = int(seconds / SECONDS_HOUR)
    print(hours, 'hours.')
if seconds >= SECONDS_PER_MINUTE:
    minutes = int(seconds / SECONDS_PER_MINUTE)
    print(minutes, 'minutes.')
else:
    print(seconds, 'seconds.')