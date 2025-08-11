# String Functions

# 1. Joins a list of stings 'mylist' with 'str' as what separates the elements
print(", ".join(["spam", "eggs", "ham"]))        # spam, eggs, ham


# 2. Replaces one substring in a string with another
print("Hello ME".replace("ME", "World"))         # Hello World

# 3. Returns the index in the string where the given substring is found. The function returns -1 if the substring is not found in the string
print("Hello World".find("llo"))                # 2

# 4. Boolean function that returns True if 'str' starts with 'str1'. False otherwise
print("This is a sentence.".startswith("This"))  # True


# 5. Boolean function that returns True if 'str' ends with 'str1'. False otherwise
print("This is a sentence.".endswith("sentence"))# True


# 6. Returns a string with all characters capitalized
print("This is a sentence.".upper())             # THIS IS A SENTENCE


# 6. Returns a string with all characters in lower case
print("AN ALL CAPS SENTENCE".lower())            # an all caps sentence


# 7. opposite to join, turns a string with a certain separator into a list, and returns the list
print("spam, eggs, ham".split(", "))             # ["spam", "eggs", "ham"]


# 8. Returrns true if the string only contains alphabetic letters, and is atleast
# one character in lenght. Returns false otherwise.
str = "dfghjmnbvfghj"
print(str.isalpha())                             # True


# 9. Returns true if the string only cintains numerical digits, and is atleast one
# digit in length. Returns false otherwise.
str = "1244353"
print(str.isdigit())                             # True


# 10. [str].isalnum()
# Returns true if the string only contains alphabetic characters or digits.
str = "12fhtew23"
print(str.isalnum())                            # True


# 11. [str].islower()
# Returns true if all of the alphabectic characters are lowercase.


# 12. [str].isupper()
# Returns true if all of the alphabectic characters are uppercase.


# 13. len(str)
# Returns the number of characters in str
str = "abc"
print(len(str))             # 3


# 14. [str].strip()
# Returns the string where white spaces are removed from both sides of the string
str = "              FINAL           "
print(str.strip() + '5')                # FINAL5

# 15. [str].lstrip
# Returns a string with all leading white spaces removed from the string
str = "              FINAL           "
print(str.lstrip() + '5')               # FINAL           5

# 16. [str].rstrip
# Returns a string with all tailing white spaces removed from the string
str = "              FINAL           "
print(str.rstrip() + '5')               #               FINAL5

# 17. [str].strip(char)
# Returns a string where the instances of char are removed from both sides of the string

# 18. [str].lstrip(char)
# 19. [str].rstrip(char)