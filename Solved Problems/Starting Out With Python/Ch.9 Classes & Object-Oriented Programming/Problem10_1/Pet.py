class Pet:

    # Initializer that initializes the pet object given its name, type, and age
    def __init__(self, name, animal_type, age):
        self.setName(name)
        self.setAnimal_type(animal_type)
        self.setAge(age)

    # Function that sets the name of the pet
    def setName(self, name):
        self.__name = name

    # Function that sets the type of the pet
    def setAnimal_type(self, animal_type):
        self.__animal_type = animal_type

    # Function that sets the age of the pet
    def setAge(self, age):
        self.__age = age

    # Function that returns the name of the pet
    def getName(self):
        return self.__name

    # Function that returns the type of the pet
    def getAnimal_type(self):
        return self.__animal_type

    # Function that returns the age of the pet
    def getAge(self):
        return self.__age