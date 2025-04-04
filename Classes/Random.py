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



# 6. random.uniform(a, b)
# Like random.random(), random.uniform() renturns a random float value
# within a given range
print(random.uniform(2, 5)) # 2.4150



# 7. random.triangular(a, b, c)
# Returns a float value between 'a' and 'b' with 'c' deciding the higher probability of the generated number
# If the value 'c' is closer to that of 'a' than 'b', then the probality of the generated number to be closer
# to 'a' than 'b' is high
print(random.triangular(20, 60, 30))    # 45.0328



# 8. random.choice(s)
# Returns a random element from the given sequence s
print(random.choice([2, 4, 6, 8, 10]))  # 8
print(random.choice('WELCOME'))         # E



# 9. random.choices(list, weight, k)
# Returns a list of randomly selected elements from the given list 'list'
# 'list':       The specified list of elements
# 'weights':    A sequence that specifies the probability of each list element to be randomly selected
# 'k':          The number of elements in the generated list
print(random.choices([2, 4, 6, 8], weights=[1, 1, 1, 1], k=3))  # 4, 8, 2
print(random.choices('WELCOME', weights=[1, 1, 1, 1, 1, 1, 1], k=3))



# 10. random.shuffle(list)
# Shuffles the specified list
mylist = [2, 4, 6, 8]
random.shuffle(mylist)

print(mylist)   # [8, 4, 2, 6]



# 11. random.sample(list, k)
# Returns another list containing sample elements from the specifed list
# 'list':   Specified list
# 'k'   :   Number of sample elements in the returned list
print(random.sample([2, 4, 6, 8], 2))