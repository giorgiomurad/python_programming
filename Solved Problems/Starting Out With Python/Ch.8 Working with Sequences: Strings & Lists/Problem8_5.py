# Problem from Starting Out With Python by Tony Gaddis
# Chapter 8: Working with Sequences: Strings and Lists
#
# Problem 8.5:  Many companies use telephone numbers like 555-GET-FOOD so the number is easier for their
#               customers to remember. On a standard telephone, the alphabetic letters are mapped to the
#               numbers in the following fashion:
#               A, B, and C:    2           D, E, and F:    3
#               G, H, and I:    4           J, K, and L:    5
#               M, N, and O:    6           P, Q, R, and S: 7
#               T, U, and V:    8           W, X, Y, and Z: 9
#
#               Write a program that asks the user to enter a 10-character telephone number in the format
#               XXX-XXX-XXXX. The application the telephone number with any alphabetic characters that
#               appeared in the original translated to their numeric equivalent.
#               For example, if the user enters 555-GET-FOOD, the application should display 555-438-3663.
#
#
# Author: Giorgio Murad Murad

# Initializing a list of characters from A to Z
codeList = [
    [],
    ['A', 'B', 'C'],
    ['D', 'E', 'F'],
    ['G', 'H', 'I'],
    ['J', 'K', 'L'],
    ['M', 'N', 'O'],
    ['P', 'Q', 'R', 'S'],
    ['T', 'U', 'V'],
    ['W', 'X', 'Y', 'Z']
]

# Prompting the user to enter a telephone number
input = input('Enter a ten-character telephone number in the format XXX-XXX-XXXX: ')
str = input.upper().split('-')

# Initializing a new string list and variable
newList = []
str2 = ''

# Converting every character to its corresponding telephone code number
for temp in str:
    str2 = ''

    for t in temp:
        if t.isdigit():
            str2 += t
        else:
            for code in codeList:
                index = codeList.index(code)+1

                for letter in code:
                    if letter == t:
                        str2 += '{D}'.format(D=index)

    newList.append(str2)

# Displaying final code
newList = '-'.join(newList)
print('The telephone code is {}'.format(newList))