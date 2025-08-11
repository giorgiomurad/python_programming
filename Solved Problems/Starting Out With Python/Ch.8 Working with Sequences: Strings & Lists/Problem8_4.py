# Problem from Starting Out With Python by Tony Gaddis
# Chapter 8: Working with Sequences: Strings and Lists
#
# Problem 8.4:  Write a program that asks a user to enter a string, and then converts the string into Morse Code
#
#
# Author: Giorgio Murad Murad

# Prompting the user to enter a string value
str = input('Enter a string value to display its Morse Code: \n')
strUpper = str.upper()

# Initializing a list with all the characters that can be converted into Morse Code
characters = [
    ' ', ',', '.', '?',
    '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I',
    'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
    'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
]

# Initializing a list with all the Morse Codes ordered by the character list
morseCodes = [
    ' ', '--..--', '.-.-.-', '--..--', '-----', '.----', '..---', '...--', '....-', '.....',
    '-....', '--...', '---..', '----.', '.-', '-...', '-.-.', '-..', '.', '..-.',
    '--.', '....', '..', '.---', '-.-', '.-..', '--', '-.', '---', '.--.',
    '--.-', '.-.', '...', '-', '..-', '...-', '.--', '-..-', '-.-', '--..'
]

# Initializing and list of integers, and filling it with Morse Codes for every string character
strCode = []
for i in range(len(str)):
    temp = strUpper[i]

    for ch in characters:
        if temp == ch:
            ind = characters.index(ch)
            code = morseCodes[ind]

            strCode.append(code)
            break

# Displaying the Morse Code of the string value
print(str + ' in Morse Code is ' + ''.join(strCode))