class Employee:
    # Initializer that initializes an employee object given the employee's information
    def __init__(self, name, number, department, job_title):
        self.setName(name)
        self.setNumber(number)
        self.setDepartment(department)
        self.setJobTitle(job_title)

    # Function that sets the employee's name
    def setName(self, name):
        self.__name = name

    # Function that sets the employee's ID number
    def setNumber(self, number):
        self.__number = number

    # Function that set the employee's department
    def setDepartment(self, department):
        self.__department = department

    # Function that sets the job title of the employee
    def setJobTitle(self, job_title):
        self.__job_title = job_title

    # Function that returns the name of the employee
    def getName(self):
        return self.__name

    # Function that returns the ID number of the employee
    def getNumber(self):
        return self.__number

    # Function that returns the department of the employee
    def getDepartment(self):
        return self.__department

    # Function that returns the job title of the employee
    def getJobTitle(self):
        return self.__job_title

    # Function that displays all the employee's information
    def __str__(self):
        return (
            "{n:15s}\t{id:5d}\t{d:15s}\t{j:15s}"
            .format(n=self.__name, id=self.__number, d=self.__department, j=self.__job_title)
        )