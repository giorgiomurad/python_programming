# Problem from Starting Out With Python by Tony Gaddis
# Chapter 10: Classes & Object-Oriented Programming
#
# Problem 10.3:     Make a class that holds the following personal data:
#                       - name, address, age, and phone number
#                       - Appropriate accessor and mutator methods
#
#                   The program should create three class instances with the program
#                   prompting the user to enter the names, addresses, ages, and phone numbers of
#                   three persons.
#                   The program should display the information of each person
#
#
# Author: Giorgio Murad Murad

from Person import Person

# List of persons
persons = []

# Loop to gather personal information of every person
for i in range(3):
    # Asking the user to enter information of every person
    name = input("Enter the name of person " + str(i + 1) + ": ")
    address = input("Enter the address of person " + str(i + 1) + ": ")
    age = input("Enter the age of person " + str(i + 1) + ": ")
    phone = input("Enter the phone number of person " + str(i + 1) + ": ")

    print()
    print()

    # Creating a new person object, and adding the object to the list
    persons.append(Person(name, address, age, phone))


# Loop to display personal information of every person
for person in persons:
    print(
        "Person {}: \n"
        "Name: {}\n"
        "Address: {}\n"
        "Age: {}\n"
        "Phone Number: {}\n"
        .format(
            persons.index(person), person.getName(), person.getAddress(),
            person.getAge(), person.getPhone()
        )
    )
    print("\n")