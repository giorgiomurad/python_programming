# String Functions

# 1. Joins a list of stings 'mylist' with 'str' as what separates the elements
print(", ".join(["spam", "eggs", "ham"]))        # spam, eggs, ham


# 2. Replaces one substring in a string with another
print("Hello ME".replace("ME", "World"))         # Hello World


# 3. Boolean function that returns True if 'str' starts with 'str1'. False otherwise
print("This is a sentence.".startswith("This"))  # True


# 4. Boolean function that returns True if 'str' ends with 'str1'. False otherwise
print("This is a sentence.".endswith("sentence"))# True


# 5. Returns a string with all characters capitalized
print("This is a sentence.".upper())             # THIS IS A SENTENCE


# 6. Returns a string with all characters in lower case
print("AN ALL CAPS SENTENCE".lower())            # an all caps sentence


# 7. opposite to join, turns a string with a certain separator into a list
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
# Removes spaces from both sides of the string
str = "              FINAL           "
print(str.strip())