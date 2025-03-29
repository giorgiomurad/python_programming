# Problem from Starting Out With Python by Tony Gaddis
# Chapter 2: Designing a Program
#
# Problem 2.1:  Write a program that displays the following information:
#                   - The user's name
#                   - The user's address, city, state, and ZIP
#                   - The user's telephone number
#                   - The user's college major
#
#
# Author: Giorgio Murad Murad

# Prompting the user to input name, address, city, state, ZIP, telephone, and major
name = input('Name: \t')
address = input('Address: \t')
city = input('City: \t')
state = input('State: \t')
ZIP = input('Zip: \t')
telephone = input('Telephone: \t')
major = input('Major: \t')

# Line breaks
print()
print()

# Displaying the results in order
print('Your Name: \t\t', name)
print('Your Address: \t', address)
print('Your City: \t\t', city)
print('Your State: \t', state)
print('Your ZIP: \t\t', ZIP)
print('Your Telephone: ', telephone)
print('Your Major: \t', major)