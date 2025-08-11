# Problem from Starting Out With Python by Tony Gaddis
# Chapter 8: Working with Sequences: Strings and Lists
#
# Problem 8.12: Write a program that reads account numbers from an external text file accounts.txt.
#               An account number is usually a number made up of seven digits, such as 5658845.
#               The program should prompt the user to enter an account number, and verifies if the
#               account number is included in the text file.
#               If it is included, the program should report to the user that the account number is
#               valid.
#               Otherwise, the program should acknowledge the user that the account number is invalid
#
#
# Author: Giorgio Murad Murad

# Opening the external text file for reading
file = open('accounts.txt', 'r')

# Prompting the user to input an account number
user = input('Enter account number: ')

accounts = []
for line in file:
    line = line.replace('\n', '')
    accounts.append(line)

# Checking if the user's account number is valid or not
if user in accounts:
    print('Account number is valid!')
else:
    print('Account number is not valid!')

# Closing the file
file.close()