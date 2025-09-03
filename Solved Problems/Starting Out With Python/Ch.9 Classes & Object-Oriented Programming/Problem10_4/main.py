# Problem from Starting Out With Python by Tony Gaddis
# Chapter 10: Classes & Object-Oriented Programming
#
# Problem 10.4:     Write a class named Employee that holds the following data about an employee:
#                   Name, ID, number, department, and job title.
#                   Once the class has been written, write a program that creates three Employee objects
#                   to hold the following data:
#
#                       Name            Number      Department      Job Title
#                       ----------------------------------------------------------
#                       Susan Meyers    47899       Accounting      Vice President
#                       Mark Jones      39119       IT              Programmer
#                       Joe Rogers      81774       Manufacturing   Engineer
#
#                   The program should store the given data in three objects and then display the data
#                   for each employee on screen.
#
#
# Author: Giorgio Murad Murad
from Employee import Employee

# List to carry the three employee objects
employees = []

# Loop to gather employee info from the user, initialize employee objects,
# and store them in the employee list
for i in range(1, 4):
    # Prompting the user to enter employee information
    print("Employee #{}".format(i))
    name = input("Enter Employee Name : ")
    id = int(input("Enter Employee ID Number: "))
    department = input("Enter Employee Department : ")
    job = input("Enter Employee Job Title : ")

    # Adding the newly initialized employee object to the list
    employees.append(Employee(name, id, department, job))
    print()


# Using a loop to display the information of the employees
print(
    "{n:15s}\t{id:5s}\t{d:15s}\t{j:15s}"
    .format(n="Name", id="ID", d="Department", j="Job Title")
)
print("----------------------------------------------")
for employee in employees:
    print(employee)