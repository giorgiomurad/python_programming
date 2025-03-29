# The Random Class
import random

# 1. random.seed(a)
# In case you don't want a random generated value to change
random.seed(10)
print(random.random())  # 0.571

random.seed(10)
print(random.random())  # 0.571



# 2. random.random()
# Generates a random float value between 0.0 and 1.0
random.random() # 0.2286



# 3. random.randrange(a, b, c)
# Can be called with one, two, or three arguments:
# With one argument (a):
# Generates a random integer value between 0 included and 'a' excluded
#
# With two arguments (a, b):
# Generates a random integer value between a included and 'b' excluded
#
# With three arguments (a, b, c):
# Generates a random integer variable from a list of integers between
# 'a' included and 'b' excluded with 'c' as the interval between every
# two values
x = random.randrange(0, 11, 2)
y = list(range(0, 11, 2))

print(x)    #  2
print(y)    # [0, 2, 4, 6, 8, 10]



# 4. random.randint()
# Returns a random integer in a given range
x = random.randint(3, 9)
print(x)    # 9



# 5. random.choice(myList)
# Returns a random element from the array 'myList'
myList = ["apple", "banana", "cherry"]
print(random.choice(myList))    # banana



# 6. random.uniform(a, b)
# Like random.random(), random.uniform() renturns a random float value
# within a given range
print(random.uniform(2, 5)) # 2.4150