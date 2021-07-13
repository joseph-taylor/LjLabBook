##############
# EXCEPTIONS #
##############
z = 8
# z = -1
if z < 0:
    # the program will end after printing this message
    raise Exception('Sorry, no numbers below zero')

var = 4
# var = 'hello'
if not type(var) is int:
    # the program will end after printing this message
    raise TypeError('Sorry, only integers are allowed')


##############
# TRY EXCEPT #
##############
x = 88

# lets you test a block of code for errors
try:
    print(x)

# lets you handle the error, without the program crashing
except NameError:
    print('Variable x is not defined')
except:
    print('Something else went wrong')

# (if specified) this code is executed if no errors are raised
else:
    x = x + 10
    print(x)

# (if specified) this code is executed regardless of whether there is an error
finally:
    print('This would often be used to close objects and clean up resources\n')


########
# WITH #
########
# used for resource management and exception handling
with open('dummy_file.txt', 'w') as file:
    file.write('Guten Tag')

# it is equivalent to the following...
'''
file = open('dummy_file.txt', 'w')
try:
    file.write('Guten Tag')
finally:
    file.close()
'''


####################
# LAMBDA FUNCTIONS #
####################
f = lambda x: x + 10
print(f(5))


###################
# ARGS and KWARGS #
###################
'''
These allow you to pass an unspecified number of arguments to a function:
*args    is used to send a non-keyworded variable length of arguments
**kwargs is used to send a keyworded (named) variable length of arguments
'''

class Animal:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

class Fish(Animal):
    def __init__(self, depth, **kwargs):
        super().__init__(**kwargs)
        self.depth = depth

animal = Animal('Tony', 300)
print()
print(animal.name)
print(animal.weight)

fish = Fish(1000, weight=2, name='Dory')
print()
print(fish.name)
print(fish.weight)
print(fish.depth)
