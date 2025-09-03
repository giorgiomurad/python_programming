# Problem from Starting Out With Python by Tony Gaddis
# Chapter 10: Classes & Object-Oriented Programming
#
# Problem 10.1:     Write a class named Pet which should have the following data attributes:
#                       - __name            (Name of the pet)
#                       - __animal_type     (The type of pet)
#                       - __age             (The pet's age)
#
#                       - __init__()        (Function that initializes the pet instance)
#                       - set_name()        (Function to set the name of the pet)
#                       - set_animal_type() (Function to set the type of the pet)
#                       - set_age()         (Function to set the age of the pet)
#                       - get_name()        (Function that returns the name of the pet)
#                       - get_type()        (Function that returns the type of the pet)
#                       - get_age()         (Function that returns the age of the pet)
#
#
#                   Once you have written the class, write a program that creates an object of the class and prompts
#                   the user to enter the name, type, and age of the pet.
#                   The program should then use the object's accessors to access and display the properties of the
#                   class.
#
#
# Author: Giorgio Murad Murad

from Pet import Pet

# Prompting the user to enter the name, type, and age of the pet
pName = input("Enter the name of your pet: ")
pType = input("Enter the type of your pet: ")
pAge = int(input("Enter the age of your pet: "))

# Creating the pet object according to the information provided by the user
pet = Pet(pName, pType, pAge)

# Displaying the name, type, and age of the age
print()
print(
    "The name of the pet is:    {}\n"
    "The type of pet is:    {}\n"
    "The age of pet is:    {}\n"
    .format(pet.getName(), pet.getAnimal_type(), pet.getAge())
)